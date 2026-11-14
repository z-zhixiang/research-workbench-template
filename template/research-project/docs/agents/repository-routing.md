# 仓库文件路由规则

本文件是 AI 和人工整理文件时的唯一分类规则。目标:任何产出都能通过"它是什么"直接确定路径,而不是按工具、会话或日期随意新建目录。

## 决策顺序

1. 它是最终研究证据,还是临时产物?临时产物进入 `.local/`。
2. 如果是研究证据,按下表进入唯一目录。
3. 仍无法判断:原创分析进 `research-notes/brainstorming/`,外部资料进 `references/`,**不要写到根目录**。

## 唯一路由表

| 内容类型 | 唯一路径 | 命名建议 |
|---|---|---|
| 论文 PDF | `papers/submitted-pdfs/` | `{标识}-{ShortTitle}.pdf` |
| 阅读笔记 | `papers/reading-notes/` | `{主题或简称}-{YYYY-MM-DD}.md` |
| 未确认想法、推导、方案比较 | `research-notes/brainstorming/` | `{主题}-{YYYY-MM-DD}.md` |
| 综述、领域地图、相关工作核验 | `research-notes/related-work/` | `{主题}-{YYYY-MM-DD}.md` |
| 实验代码、配置、日志、结果 | `experiments/{三位序号}-{英文短名}/` | 一个问题一个目录 |
| 论文正文等写作源稿 | `writing/drafts/` | 语义化文件名,版本交给 git |
| 图表源文件与发布图 | `writing/figures/` | 同一图的不同格式用同一主文件名 |
| 投稿包、审稿回复 | `writing/submissions/` | `{venue}-{year}/` |
| BibTeX | `references/citations.bib` | 稳定的 citation key |
| 外部报告、截图、模板 | `references/` | 按来源或用途建子目录 |
| 跨实验复用的脚本 | `scripts/` | `{动作}-{对象}.py`;单次实验的代码不放这里 |
| 项目状态 | `research-log.md` | 追加日期、结论、证据路径 |
| AI 与管理规则 | `docs/agents/` | 每个文件只管一种规则 |
| 长期项目决策 | `docs/adr/` | `{四位序号}-{英文短名}.md` |
| 临时抓取、缓存、中间文件、本地工具 | `.local/` | 不进入 git |

## 实验目录最低要求

`experiments/{三位序号}-{英文短名}/README.md` 至少写明:问题、输入、运行命令、指标、结论(没跑完写"待验证")。
