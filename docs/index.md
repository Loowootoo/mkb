# 歡迎來到我的知識庫

這是一個基於 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 建立的個人知識庫，全部內容以 Markdown 撰寫，並透過 GitHub Actions 自動部署到 GitHub Pages。

## 快速導覽

- [關於這個知識庫](./about.md)
- [入門範例](./getting-started.md)
- [所有標籤](../tags.html)

## 如何撰寫新筆記

在 `docs/` 資料夾下新增 Markdown 檔案，例如 `docs/my-note.md`，並在檔案頂端加入標題與標籤：

```markdown
# 我的筆記標題

這是筆記內容。你可以加入 [內部連結](./index.md) 與程式碼區塊。

```python
print("Hello, knowledge base!")
```

**標籤：** #筆記 #範例
```

提交並推送到 GitHub 後，網站會自動重新建構與部署。
