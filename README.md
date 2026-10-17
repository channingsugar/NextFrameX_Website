# NextFrame 中文网站

产品首页、下载页与 15 篇人工使用教程。静态 HTML，可直接打开 `index.html` 阅读；搜索也可在本地文件模式使用，不依赖第三方服务。

## 修改与构建

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build-site.py
python3 scripts/check-site.py
```

- `content/guide/*.md`：中文教程；`content/en/guide/*.md`：英文教程。修改后重新构建。
- `locales/zh.json`、`locales/en.json`：导航、首页、下载页和界面文案。
- `templates/home.html`、`templates/download.html`：首页和下载页结构，文案来自 locale。
- 中文页面保持原地址。英文页面在 `en/`，导航中的语言切换指向同一页的另一种语言。
- `assets/css/site.css`、`assets/js/site.js`：共享样式与轻量交互。
- `scripts/build-site.py`：导航、章节目录、全文搜索数据与静态页面生成；下载/作者地址集中配置。
- `assets/media/`：本次新增真实截图与引擎预览；来源见 `docs/ASSET-SOURCES.md`。
- `guide/`、`download/`、`index.html`：生成页面，保留在仓库便于本地预览。
- `_site/`：发布产物，只包含公开页面和它们引用的资源。

首屏保留桌面鼠标横移、手机页面滚动联动样片，并补充前后按钮。正文使用自然滚动。遵守减少动态效果偏好；无 JS 时正文和普通链接可用。

## 发布

GitHub Pages 工作流构建并验证 `_site/` 后上传。保留原域名和备案。部署不上传旧截图、源码、内部规划文档。详见 `DEPLOY.md`。本次改动未推送或发布。
