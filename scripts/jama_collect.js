(async () => {
  const query = new URLSearchParams({
    q: "RCT",
    f_SiteID: "3",
    f_ArticleTypeDisplayName: "Research",
    f_FreeAccessFilter: "true",
    rg_ArticleDate: "2024-01-01 TO 2025-12-31",
  });
  const origin = location.origin;
  const found = new Map();

  for (let page = 1; page <= 10; page += 1) {
    query.set("page", String(page));
    const html = await fetch(`${origin}/searchresults?${query}`).then((response) => response.text());
    const documentForPage = new DOMParser().parseFromString(html, "text/html");
    const cards = [...documentForPage.querySelectorAll('a[href*="/journals/jama/fullarticle/"][href*="resultClick=1"]')];
    if (!cards.length) break;
    let added = 0;
    for (const anchor of cards) {
      const card = anchor.closest("li");
      const entry = card?.innerText || "";
      if (!/Original Investigation/i.test(entry) || !/free access/i.test(entry)) continue;
      const url = anchor.href.replace("?resultClick=1", "");
      if (!found.has(url)) {
        found.set(url, { title: anchor.textContent.trim(), url, entry });
        added += 1;
      }
    }
    if (!added && page > 1) break;
  }

  async function fetchHtml(url) {
    for (let attempt = 0; attempt < 3; attempt += 1) {
      const response = await fetch(url);
      const html = await response.text();
      if (response.ok && /citation_doi|supplement-download/.test(html)) return html;
      await new Promise((resolve) => setTimeout(resolve, 500 * (attempt + 1)));
    }
    throw new Error(`Could not retrieve article HTML: ${url}`);
  }

  async function inspect(article) {
    const html = await fetchHtml(article.url);
    const articleDocument = new DOMParser().parseFromString(html, "text/html");
    const supplements = [...articleDocument.querySelectorAll("a.supplement-download")].map((anchor) => ({
      label: anchor.parentElement?.innerText.replace(/\s+/g, " ").trim() || "",
      href: anchor.href,
    }));
    const protocol = supplements.filter(({ label }) => /protocol/i.test(label));
    const electronic = supplements.filter(({ label }) =>
      !/(protocol|statistical analysis plan|data sharing statement|nonauthor collaborator|author list)/i.test(label),
    );
    const doi = articleDocument.querySelector('meta[name="citation_doi"]')?.content || "";
    return {
      ...article,
      doi,
      has_protocol: protocol.length > 0,
      has_electronic_supplement: electronic.length > 0,
      supplements,
    };
  }

  const inspected = [];
  const errors = [];
  const articles = [...found.values()];
  for (let start = 0; start < articles.length; start += 2) {
    const batch = await Promise.allSettled(articles.slice(start, start + 2).map(inspect));
    for (const result of batch) {
      if (result.status === "fulfilled") inspected.push(result.value);
      else errors.push(String(result.reason));
    }
  }
  const eligible = inspected.filter((article) => article.has_protocol && article.has_electronic_supplement);
  return JSON.stringify({
    original_investigations_checked: inspected.length,
    eligible_count: eligible.length,
    errors,
    eligible: eligible.map(({ title, url, doi, supplements }) => ({ title, url, doi, supplements })),
  });
})()
