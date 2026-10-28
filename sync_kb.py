#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知識庫同步腳本 (sync_kb.py)

功能：
1. 掃描 docs/ 下所有 Markdown 檔案
2. 為缺少 YAML frontmatter 的檔案補上 title 與 tags
3. 根據分組規則自動產生 mkdocs.yml 的 nav 區塊（主題分組）
4. 保留 mkdocs.yml 其他區塊（theme、plugins 等）不變

使用方式：
    python sync_kb.py
    git add -A && git commit -m "chore: 同步知識庫 frontmatter 與 nav" && git push
"""

from pathlib import Path
import re
import sys

# ==================== 設定區 ====================
DOCS_DIR = Path("docs")
MKDOCS_YML = Path("mkdocs.yml")

# 預設標籤（所有檔案都會加上）
DEFAULT_TAGS = ["筆記"]

# 分組規則：群組名稱 -> 檔名關鍵字清單（任一關鍵字匹配即歸入該群組，不區分大小寫）
# 請根據你的檔案命名習慣調整關鍵字
GROUP_RULES = {
    "演算法筆記": ["演算法", "algorithm", "a*", "遞增法"],
    "技術筆記": ["技術", "tech", "程式", "code"],
    "讀書筆記": ["讀書", "book", "閱讀"],
    "專案紀錄": ["專案", "project", "專題"],
}

# 不列入 nav 的檔案（例如 index.md 通常作為首頁，可單獨處理）
EXCLUDE_FILES = set()

# ==================== 工具函式 ====================

def has_frontmatter(text: str) -> bool:
    """檢查檔案是否已經有 YAML frontmatter（--- 開頭）"""
    return text.strip().startswith("---\n")


def extract_title_from_content(text: str) -> str | None:
    """從 Markdown 內容中提取第一個 # 標題作為頁面標題"""
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


def filename_to_title(name: str) -> str:
    """從檔名推斷標題（移除副檔名，底線與連字轉空格）"""
    title = Path(name).stem
    title = title.replace("_", " ").replace("-", " ")
    return title.strip()


def guess_tags(title: str, content: str) -> list[str]:
    """推測標籤。預設回傳 DEFAULT_TAGS，可在此擴充邏輯"""
    tags = list(DEFAULT_TAGS)
    return tags


def ensure_frontmatter(path: Path) -> bool:
    """
    若檔案沒有 frontmatter，則補上。
    回傳是否有修改。
    """
    text = path.read_text(encoding="utf-8")

    if has_frontmatter(text):
        return False

    # 標題：優先用內容 # 標題，否則用檔名
    title = extract_title_from_content(text) or filename_to_title(path.name)
    tags = guess_tags(title, text)

    # 建立 frontmatter 區塊
    tag_lines = "\n".join(f"  - {t}" for t in tags)
    fm = f"---\ntitle: {title}\ntags:\n{tag_lines}\n---\n\n"

    path.write_text(fm + text, encoding="utf-8")
    return True


def group_file(name: str) -> str | None:
    """根據檔名與分組規則，回傳所屬群組名稱；若無匹配則回傳 None"""
    lower = name.lower()
    for group, keywords in GROUP_RULES.items():
        for kw in keywords:
            if kw.lower() in lower:
                return group
    return None


def build_nav() -> str:
    """掃描 docs/ 並建構 nav YAML 字串"""
    files = sorted(
        [p for p in DOCS_DIR.iterdir() if p.suffix.lower() == ".md" and p.name not in EXCLUDE_FILES],
        key=lambda p: p.name,
    )

    groups: dict[str, list[Path]] = {}
    ungrouped: list[Path] = []

    for f in files:
        g = group_file(f.name)
        if g:
            groups.setdefault(g, []).append(f)
        else:
            ungrouped.append(f)

    lines = ["nav:"]

    # 未分組的檔案先列在最前（單層）
    for f in ungrouped:
        text = f.read_text(encoding="utf-8")
        title = extract_title_from_content(text) or filename_to_title(f.name)
        lines.append(f"  - {title}: '{f.name}'")

    # 有分組的檔案
    for group, members in groups.items():
        lines.append(f"  - {group}:")
        for f in sorted(members, key=lambda p: p.name):
            text = f.read_text(encoding="utf-8")
            title = extract_title_from_content(text) or filename_to_title(f.name)
            lines.append(f"      - {title}: '{f.name}'")

    return "\n".join(lines)


def replace_nav_in_mkdocs(new_nav: str) -> bool:
    """將 mkdocs.yml 中的 nav: 區塊替換為新內容，保留其他區塊不變"""
    text = MKDOCS_YML.read_text(encoding="utf-8")

    nav_start = re.search(r'^nav:\s*$', text, re.MULTILINE)

    if not nav_start:
        # 沒有 nav 區塊，在 theme: 前插入；若無 theme 則附加在檔尾
        theme_match = re.search(r'^theme:', text, re.MULTILINE)
        if theme_match:
            insert_pos = theme_match.start()
            new_text = text[:insert_pos] + new_nav + "\n\n" + text[insert_pos:]
        else:
            new_text = text.rstrip() + "\n\n" + new_nav + "\n"
        MKDOCS_YML.write_text(new_text, encoding="utf-8")
        return True

    # 有 nav 區塊：找到結束位置（下一個頂層 key，即行首無縮進的非空行）
    start_pos = nav_start.start()
    remainder = text[start_pos:]
    lines = remainder.splitlines(keepends=True)

    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() and not line.startswith((" ", "\t")):
            end_idx = i
            break

    # 計算絕對結束位置
    if end_idx is None:
        abs_end = len(text)
    else:
        abs_end = start_pos + sum(len(l) for l in lines[:end_idx])

    new_text = text[:start_pos] + new_nav + "\n" + text[abs_end:]
    MKDOCS_YML.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    if not DOCS_DIR.exists():
        print(f"錯誤：找不到 {DOCS_DIR} 資料夾，請在專案根目錄執行此腳本。")
        sys.exit(1)

    if not MKDOCS_YML.exists():
        print(f"錯誤：找不到 {MKDOCS_YML}，請確認在專案根目錄執行。")
        sys.exit(1)

    # 1. 補全所有 MD 檔案的 frontmatter
    changed = 0
    for f in sorted(DOCS_DIR.glob("*.md")):
        if ensure_frontmatter(f):
            changed += 1
            print(f"[frontmatter] 已補全: {f.name}")

    if changed:
        print(f"共補全 {changed} 個檔案的 frontmatter")
    else:
        print("[frontmatter] 所有檔案已有 frontmatter，無需變更")

    # 2. 重新產生 nav 並寫入 mkdocs.yml
    new_nav = build_nav()
    replace_nav_in_mkdocs(new_nav)
    print("[nav] 已更新 mkdocs.yml 導覽欄")


if __name__ == "__main__":
    main()
