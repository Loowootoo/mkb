# 個人知識庫

現代化的個人知識庫網站，可發佈於 GitHub Pages。

## 使用方式

1. 將此專案推到你的 GitHub 儲存庫（預設分支為 `main`）。
2. 在 GitHub 儲存庫設定中開啟 **Pages**，來源選擇 **GitHub Actions**。
3. 推送任何變更後，GitHub Actions 會自動建構並部署網站。

## 撰寫筆記

- 在 `docs/` 下新增 Markdown 檔案即可自動出現在網站導覽中。
- 在 `mkdocs.yml` 的 `nav` 欄位（若有設定）可調整頁面順序。
- 所有圖片與靜態資源請放在 `docs/assets/`。

## 本地預覽（選用）

若要在本機預覽，需先安裝 Python 與 mkdocs-material：

```bash
pip install mkdocs-material mkdocs-git-revision-date-localized-plugin
mkdocs serve
```

然後開啟 http://127.0.0.1:8000
