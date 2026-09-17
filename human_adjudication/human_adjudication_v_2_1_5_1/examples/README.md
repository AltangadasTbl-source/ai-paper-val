# 2019 Checker 阶段测试样例

直接打开 [2019 TEST Checker ready](human_adjudication_v_2_1_5_1_2019_TEST_checker_ready.xlsx) 即可测试，无需先填初审或运行交接命令。

- 10 篇论文、71 条候选的初审已全部 Complete=yes，初审快照已带入。
- 初审统一设为 exclude，仅作模拟占位；这不表示论文候选应被排除。领域保留原建议值，不适用判断使用默认值。
- Setup 已填 TEST_primary_2019 和 TEST_checker_2019；复核结果为空，复核 Complete=no。
- Start、姓名和每条初审备注明确标注 SYNTHETIC TEST DATA ONLY。样例仅用于操作测试，不用于研究结果。
- [2019 TEST Primary complete](human_adjudication_v_2_1_5_1_2019_TEST_primary_complete.xlsx) 是对应的已完成初审样例，可用于重新测试 prepare-checker。

## 可测试的操作

1. 打开任意 C_ 论文表，向右查看 M 列 Primary assessment：应显示 exclude 和模拟数据说明。
2. 在 N 列 Checker result 选 agree，F 列 Complete 选 yes。D–E、H–L 和 R 列 留空即可继承初审；本行无需复核意见。
3. 换一行选 disagree，填写 Checker comment 并设 Complete=yes。此行在共同讨论解决前保持 unresolved。
4. 把该行 Discussion resolution 设 resolved，并在 Resolution note 记录模拟参与人和结论；最终 disposition 不为 discuss 时可解决此行。
5. 测试改判时可设置 Disposition=retain 和 Review domain=statistical_results，再填 Statistcal_or_numerical issue 与 Substantiveness。原初审 exclude 的不适用值不能提供这两个新答案；非 agree 需要说明。
6. 将编辑后的样例另存副本，运行 validate 检查。尚未复核的其他行显示 PENDING 是正常状态。

```bash
python3 human_adjudication/human_adjudication_v_2_1_5_1/build_v_2_1_5_1.py validate my_2019_checker_test.xlsx --report my_2019_test_validation.xlsx
```

样例生成器为 [build_example_2019.py](../build_example_2019.py)，拒绝覆盖已有样例。四份正式年度模板仍为空白，位于上一级目录。
