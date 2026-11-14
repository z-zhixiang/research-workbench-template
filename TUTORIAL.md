# 零基础教程:搭一套自己的研究工作台

预计 1 小时。**你做第 1~4 步**(装软件、复制文件夹、打开、填几行字),第 5 步起交给 AI。软件界面的文字会随版本变化,以你屏幕上为准。

## 先认识三个词

| 词 | 一句话解释 |
|---|---|
| **vault** | Obsidian 里「一个文件夹 = 一个知识库」。你打开哪个文件夹,哪个就是 vault |
| **总纲(`SYSTEM.md`)** | 写明这套系统放哪、各部分怎么分工、AI 该守什么规矩。AI 每次干活先读它 |
| **路由表** | 「什么类型的文件放哪个目录」的唯一对照表,避免乱放 |

## 第 1 步:装两个软件

- Zotero:官网 zotero.org 下载安装。
- Obsidian:官网 obsidian.md 下载安装。

两者个人使用通常免费,以官网为准。

✅ **检查点**:两个软件都能打开。

## 第 2 步:复制模板

1. 在本仓库页面点绿色的 **Code → Download ZIP**,解压。(会用 git 的话直接 clone。)
2. 把解压后的 **`template`** 文件夹复制到你想放的位置,改名为 `research-workbench`。
3. 不要放在带你真实姓名的公开云盘共享目录里。

✅ **检查点**:`research-workbench` 里能看到 `SYSTEM.md`、`knowledge-base/`、`research-project/`。

## 第 3 步:用 Obsidian 打开知识库

Obsidian 启动页选 **Open folder as vault**(打开文件夹作为知识库),选 `research-workbench/knowledge-base`。

✅ **检查点**:左侧文件列表里有 `raw`、`wiki`、`outputs`、`journal` 和一个 `CLAUDE.md`。

> `CLAUDE.md` 是写给 AI 的说明书,你也可以读。

## 第 4 步:填总纲

用任何文本编辑器打开 `research-workbench/SYSTEM.md`,把第一节里的 `【填写:…】` 换成你的实际情况(这套东西放在哪台电脑、哪个目录)。**不确定的就留着,别乱填。**

✅ **检查点**:第一节没有残留的 `【填写:…】`。

## 第 5 步:交给 AI

打开 Claude Code(或其他能读写文件的 AI),进入 `research-workbench` 目录,发:

> 请先读 `SYSTEM.md`,再读 `knowledge-base/CLAUDE.md` 和 `research-project/PROJECT.md`。然后问我几个问题,帮我把这些文件里的 `【填写:…】` 补完。我没告诉你的信息不要编造,不知道就写 `待确认`。

## 第 6 步:第一周怎么用

| 你想做 | 放哪里 | 对 AI 说 |
|---|---|---|
| 读一篇论文 | PDF 放进 Zotero;值得沉淀的原文再复制一份到 `knowledge-base/raw/` | 「把 raw 里的新论文整理进 wiki」 |
| 问自己知识库里的问题 | — | 「根据我的知识库回答:……」(答案会写进 `outputs/`) |
| 记今天的进度 | `knowledge-base/journal/` | 「我今天做了……,帮我记成日志」 |
| 记一个研究想法 | `research-project/research-notes/brainstorming/` | 「把这个想法记下来,文件名带日期」 |
| 做一次实验 | `research-project/experiments/` 下新建编号目录 | 「按路由表给这次实验建目录」 |
| 写论文 | `research-project/writing/drafts/` | — |

**Zotero 和 Obsidian 怎么衔接?** 目前没有定成规则。一个简单做法(**只是建议,尚未固化**):在每个 wiki 页面末尾的"来源文件"里写上这篇文献在 Zotero 里的标题或引用键,方便回查。想把它变成规则,按总纲第五节:先告诉 AI,你同意后再改规则文件。

## 常见问题

| 现象 | 怎么办 |
|---|---|
| AI 把文件放到了奇怪的地方 | 让它重新读 `SYSTEM.md` 和对应层的规则文件,并指出路由表里对应的目录 |
| AI 想新建一套自己的目录或笔记系统 | 拒绝。总纲第五节规定不新建平行体系 |
| 想改规则 | 告诉 AI 你要改什么。它应该先征得你同意,再改**规则文件本身**,而不是只在对话里"破例" |
| 担心隐私 | AI 读到的内容会发给模型服务;只让它在 `research-workbench` 里干活,不要把私人材料放进来 |
| 整理没有自动发生 | 正常。默认没有自动触发,需要你开口 |
