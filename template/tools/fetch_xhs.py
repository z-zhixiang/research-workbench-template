#!/usr/bin/env python3
"""抓取小红书分享链接 -> Markdown（标题/作者/正文/标签/评论/图片），无需登录。

用法:
  fetch_xhs.py '<分享文案或链接>' [--out DIR] [--anon] [--no-images] [--stdout]

  --anon       评论者昵称匿名化（用于公开截图/证据）
  --no-images  不下载图片，只记录地址
  --stdout     只打印 Markdown，不落盘

默认 --out 是 knowledge-base/raw/web（请在工作台根目录运行）；目标目录已存在时不会覆盖。
仅供个人归档：请遵守平台条款，尊重作者版权，不要转发抓取到的内容。
遇到验证码/风控时脚本会停下，不会绕过。

控制台输出的 URL 会对 xsec_token 等分享参数打码。
原理: 分享短链跳转到笔记页，页面服务端直出 window.__INITIAL_STATE__，里面有正文和首屏评论。
退出码: 0 成功, 2 没拿到笔记数据（风控/验证码/改版），此时请改用截图, 3 目标目录已存在（不覆盖）。
"""
import argparse, datetime, json, pathlib, re, sys, urllib.parse, urllib.request

UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")
LINK_RE = re.compile(r"https?://(?:xhslink\.(?:com|cn)|(?:www\.)?xiaohongshu\.com)/[^\s\"<>，。]+")
SECRET_KEYS = ("xsec_token", "shareRedId", "share_id", "apptime", "track_code")


def say(step, msg):
    print(f"[{step}] {msg}", flush=True)


def mask(url):
    for k in SECRET_KEYS:
        url = re.sub(rf"({k}=)[^&]+", r"\1***", url)
    return url


def get(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
        return (r.geturl(), data if binary else data.decode("utf-8", "replace"))


def parse_state(page):
    m = re.search(r"__INITIAL_STATE__=(\{.*?\})</script>", page, re.S)
    if not m:
        return None
    s = re.sub(r"(?<=[:\[,])undefined(?=[,\]}])", "null", m.group(1))
    return json.loads(s)


def safe(name, n=40):
    return re.sub(r'[\\/:*?"<>|\s]+', "_", name).strip("_")[:n] or "untitled"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text")
    ap.add_argument("--out", default="knowledge-base/raw/web")
    ap.add_argument("--anon", action="store_true")
    ap.add_argument("--no-images", action="store_true")
    ap.add_argument("--stdout", action="store_true")
    a = ap.parse_args()

    m = LINK_RE.search(a.text)
    if not m:
        say("1/5 提取链接", "没有在输入里找到小红书链接")
        sys.exit(1)
    src = m.group(0).rstrip(".,)")
    say("1/5 提取链接", mask(src))

    final, page = get(src)
    say("2/5 跟随跳转", f"-> {mask(final)}  (页面 {len(page)} 字符)")

    state = parse_state(page)
    data = ((state or {}).get("noteData") or {}).get("data") or {}
    note = data.get("noteData")
    if not note or not note.get("title") and not note.get("desc"):
        hint = "疑似验证码/风控" if re.search("验证|captcha", page) else "页面结构可能已改版"
        say("3/5 解析笔记", f"失败：{hint}。请改用截图转发。")
        sys.exit(2)
    desc = (note.get("desc") or "").strip()
    tags = [t.get("name") for t in note.get("tagList", []) if t.get("name")]
    imgs = [(i.get("urlDefault") or i.get("url")) for i in note.get("imageList", [])]
    say("3/5 解析笔记", f"标题={note.get('title')!r} 作者={note.get('user', {}).get('nickName')!r} "
                        f"类型={note.get('type')} 正文={len(desc)}字 图片={len(imgs)}张 标签={tags}")

    cd = data.get("commentData") or {}
    names = {}

    def who(c):
        u = c.get("user", {})
        n = u.get("nickName") or u.get("nickname") or "?"
        if not a.anon:
            return n
        return names.setdefault(n, f"用户{chr(65 + len(names) % 26)}{len(names) // 26 or ''}")

    def loc(c):
        return f"（{c['ipLocation']}）" if c.get("ipLocation") and not a.anon else ""

    clines = []
    for c in cd.get("comments", []):
        clines.append(f"- **{who(c)}**{loc(c)}：{c.get('content')}")
        for s in c.get("subComments", []):
            clines.append(f"    - **{who(s)}**{loc(s)}：{s.get('content')}")
    say("4/5 解析评论", f"总数 {cd.get('commentCount', '?')}，页面内拿到 {len(clines)} 条（含回复）")

    today = datetime.date.today().isoformat()
    slug = f"{today}-{safe(note.get('title') or desc[:20])}"
    md = [
        "---",
        f"title: {note.get('title')}",
        f"author: {note.get('user', {}).get('nickName')}",
        f"source: {src if not a.anon else mask(src)}",
        f"platform: xiaohongshu",
        f"fetched: {today}",
        f"tags: {tags}",
        "---",
        "",
        desc,
        "",
        "## 图片",
    ]
    outdir = None
    if not a.stdout:
        outdir = pathlib.Path(a.out).expanduser() / slug
        if (outdir / "note.md").exists():
            say("5/5 写入", f"已存在，不覆盖：{outdir}")
            sys.exit(3)
        outdir.mkdir(parents=True, exist_ok=True)
    for i, u in enumerate(imgs):
        if outdir and not a.no_images:
            fn = f"img{i}.jpg"
            (outdir / fn).write_bytes(get(u, binary=True)[1])
            md.append(f"![]({fn})")
        else:
            md.append(f"- {u}")
    md += ["", "## 评论（首屏）"] + (clines or ["（无）"])
    text = "\n".join(md) + "\n"

    if a.stdout:
        print(text)
    else:
        (outdir / "note.md").write_text(text, encoding="utf-8")
        say("5/5 写入", f"{outdir}/note.md" + ("" if a.no_images else f"（含 {len(imgs)} 张图）"))


if __name__ == "__main__":
    main()
