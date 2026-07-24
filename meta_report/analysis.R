#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(ggplot2))

args <- commandArgs(trailingOnly = TRUE)
root <- if (length(args) >= 1) normalizePath(args[[1]]) else normalizePath(".")
out <- file.path(root, "meta_report")
figdir <- file.path(out, "figures")
dir.create(figdir, recursive = TRUE, showWarnings = FALSE)

d <- read.csv(file.path(out, "audit_findings.csv"), stringsAsFactors = FALSE,
              check.names = FALSE)

article_order <- unique(d$article)
severity_order <- c("Minor", "Major")
category_order <- c(
  "Presentation inconsistency",
  "Statistical reporting inconsistency",
  "Cross-document inconsistency",
  "Arithmetic inconsistency",
  "Participant flow inconsistency"
)

article_counts <- as.data.frame.matrix(table(d$article, d$severity))
for (x in severity_order) if (!x %in% names(article_counts)) article_counts[[x]] <- 0
article_counts$article <- rownames(article_counts)
article_counts$total <- article_counts$Major + article_counts$Minor
article_counts <- article_counts[match(article_order, article_counts$article),
                                 c("article", "Major", "Minor", "total")]
write.csv(article_counts, file.path(out, "article_counts.csv"), row.names = FALSE)

category_counts <- as.data.frame(table(
  category = factor(d$category, levels = category_order),
  severity = factor(d$severity, levels = severity_order)
))
category_counts <- category_counts[category_counts$Freq > 0, ]
write.csv(category_counts, file.path(out, "category_counts.csv"), row.names = FALSE)

split_tags <- function(column) {
  pairs <- do.call(rbind, lapply(seq_len(nrow(d)), function(i) {
    tags <- strsplit(d[[column]][i], "; ", fixed = TRUE)[[1]]
    data.frame(article = d$article[i], severity = d$severity[i], tag = tags,
               stringsAsFactors = FALSE)
  }))
  findings <- aggregate(article ~ tag, pairs, length)
  names(findings)[2] <- "finding_mentions"
  papers <- aggregate(article ~ tag, pairs, function(x) length(unique(x)))
  names(papers)[2] <- "papers"
  merge(findings, papers, by = "tag")
}

artifact_counts <- split_tags("artifact_tags")
artifact_counts <- artifact_counts[order(-artifact_counts$finding_mentions), ]
write.csv(artifact_counts, file.path(out, "artifact_counts.csv"), row.names = FALSE)

mechanism_counts <- split_tags("mechanism_tags")
mechanism_counts <- mechanism_counts[order(-mechanism_counts$finding_mentions), ]
write.csv(mechanism_counts, file.path(out, "mechanism_counts.csv"), row.names = FALSE)

font_family <- "Noto Sans CJK SC"
major_color <- "#B23A48"
minor_color <- "#4C78A8"

save_both <- function(plot, stem, width, height) {
  ggsave(file.path(figdir, paste0(stem, ".pdf")), plot, width = width,
         height = height, units = "in", device = cairo_pdf)
  ggsave(file.path(figdir, paste0(stem, ".png")), plot, width = width,
         height = height, units = "in", dpi = 220, bg = "white")
}

long_articles <- rbind(
  data.frame(article = article_counts$article, severity = "Major",
             count = article_counts$Major),
  data.frame(article = article_counts$article, severity = "Minor",
             count = article_counts$Minor)
)
long_articles$severity <- factor(long_articles$severity,
                                 levels = c("Major", "Minor"))
long_articles$article <- factor(long_articles$article,
                                levels = rev(article_order))
p1 <- ggplot(long_articles, aes(article, count, fill = severity)) +
  geom_col(width = 0.72) +
  coord_flip() +
  scale_fill_manual(values = c(Major = major_color, Minor = minor_color)) +
  scale_y_continuous(breaks = 0:10, expand = expansion(mult = c(0, .02))) +
  labs(x = NULL, y = "Retained findings", fill = NULL,
       title = "Major and Minor findings by article") +
  theme_minimal(base_family = font_family, base_size = 9) +
  theme(panel.grid.major.y = element_blank(),
        legend.position = "top",
        plot.title = element_text(face = "bold", size = 12))
save_both(p1, "article_findings", 7.2, 6.8)

category_counts$category <- factor(category_counts$category,
                                   levels = rev(category_order))
category_counts$severity <- factor(category_counts$severity,
                                   levels = c("Major", "Minor"))
p2 <- ggplot(category_counts, aes(category, Freq, fill = severity)) +
  geom_col(width = 0.67) +
  coord_flip() +
  geom_text(aes(label = Freq), position = position_stack(vjust = 0.5),
            color = "white", family = font_family, size = 3.2) +
  scale_fill_manual(values = c(Major = major_color, Minor = minor_color)) +
  scale_y_continuous(expand = expansion(mult = c(0, .04))) +
  labs(x = NULL, y = "Retained findings", fill = NULL,
       title = "Audit categories and severity") +
  theme_minimal(base_family = font_family, base_size = 9.5) +
  theme(panel.grid.major.y = element_blank(),
        legend.position = "top",
        plot.title = element_text(face = "bold", size = 12))
save_both(p2, "category_severity", 7.2, 4.2)

artifact_counts$tag <- factor(artifact_counts$tag,
                              levels = rev(artifact_counts$tag))
p3 <- ggplot(artifact_counts, aes(tag, finding_mentions)) +
  geom_col(fill = "#59A14F", width = 0.66) +
  geom_text(aes(label = paste0(finding_mentions, " / ", papers, " papers")),
            hjust = -0.08, family = font_family, size = 3.1) +
  coord_flip() +
  scale_y_continuous(limits = c(0, max(artifact_counts$finding_mentions) * 1.24),
                     expand = expansion(mult = c(0, 0))) +
  labs(x = NULL, y = "Findings involving the artifact (multi-label)",
       title = "Where problems surfaced") +
  theme_minimal(base_family = font_family, base_size = 9.5) +
  theme(panel.grid.major.y = element_blank(),
        plot.title = element_text(face = "bold", size = 12))
save_both(p3, "artifact_involvement", 7.2, 4.4)

heat <- as.data.frame(table(
  article = factor(d$article, levels = article_order),
  category = factor(d$category, levels = category_order)
))
names(heat)[3] <- "count"
p4 <- ggplot(heat, aes(category, article, fill = count)) +
  geom_tile(color = "white", linewidth = 0.35) +
  geom_text(aes(label = ifelse(count == 0, "", count)),
            family = font_family, size = 2.7) +
  scale_fill_gradient(low = "#F4F7FA", high = "#4C78A8",
                      breaks = 0:max(heat$count)) +
  scale_x_discrete(labels = c(
    "Presentation inconsistency" = "Presentation",
    "Statistical reporting inconsistency" = "Statistical",
    "Cross-document inconsistency" = "Cross-document",
    "Arithmetic inconsistency" = "Arithmetic",
    "Participant flow inconsistency" = "Participant flow"
  )) +
  labs(x = NULL, y = NULL, fill = "Count",
       title = "Error-category profile by article") +
  theme_minimal(base_family = font_family, base_size = 8.7) +
  theme(panel.grid = element_blank(),
        axis.text.x = element_text(angle = 28, hjust = 1),
        plot.title = element_text(face = "bold", size = 12))
save_both(p4, "category_heatmap", 7.5, 6.2)

cat("Wrote analysis tables and figures to", out, "\n")
