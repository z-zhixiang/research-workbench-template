# 【填写:项目名】项目导航

> 这是人和 AI 的统一入口。开始工作先读本文件,再按任务类型进入对应目录;不要把研究产出或临时文件直接放在仓库根目录。

## 当前状态

| 项目 | 当前结论 |
|---|---|
| 活跃方向 | 【填写】 |
| 当前聚焦 | 【填写】 |
| 方法候选 | 【填写;未经验证的写"工作假设"】 |
| 论文类型 | 【填写:例如方法设计 / 实证评估 / 综述】 |
| 发表目标 | 【填写,或"待确认"】 |
| 时间约束 | 【填写,或"待确认"】 |
| 计算 / 资源约束 | 【填写】 |

最新进展以 [`research-log.md`](research-log.md) 最末条目为准;方向性结论以导师确认优先。

## 开始工作时的阅读顺序

1. `PROJECT.md`:判断当前阶段、目标与入口。
2. `CONTEXT.md`:统一术语。
3. `research-log.md`:读取最近进展,避免重复工作。
4. 与当前任务直接相关的笔记、论文笔记或实验目录。
5. `docs/adr/`:已经确定、不应被静默推翻的决策。

## 核心入口

| 想找什么 | 去哪里 |
|---|---|
| 项目时间线与当前进度 | `research-log.md` |
| 研究想法与方案比较 | `research-notes/brainstorming/` |
| 相关工作与核验 | `research-notes/related-work/` |
| 逐篇论文笔记 / PDF | `papers/reading-notes/`、`papers/submitted-pdfs/` |
| 实验 | `experiments/{序号}-{名称}/` |
| 论文草稿 / 图 / 投稿包 | `writing/drafts/`、`writing/figures/`、`writing/submissions/` |
| BibTeX | `references/citations.bib` |
| 路由与管理规则 | `docs/agents/` |
| 项目决策记录 | `docs/adr/` |
| 临时文件、缓存、本地工具 | `.local/`(git 忽略) |

## 路径纪律

- 根目录只放入口和配置:`PROJECT.md`、`CONTEXT.md`、`CLAUDE.md`、`AGENTS.md`、`research-log.md`、`.gitignore`。
- 研究产出必须进入既定目录,**不得写入 `.local/`**;临时下载、转换中间产物统一放 `.local/`。
- 拿不准分类的想法先进 `research-notes/brainstorming/`,文件名带日期,不要新建含义模糊的目录。
- 新实验用 `experiments/{三位序号}-{英文短名}/`,目录内至少有 `README.md`:问题、输入、命令、指标、结论。
- 完成重要工作后,在 `research-log.md` 追加日期、结论、产出路径。

详细规则见 `docs/agents/repository-routing.md`。

## 当前下一步

1. 【填写】
