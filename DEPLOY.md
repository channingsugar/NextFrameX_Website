# 发布 NextFrame 网站

## 本地检查

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build-site.py
python3 scripts/check-site.py
```

直接打开 `_site/index.html` 查看发布内容，或使用已安装的静态服务器服务 `_site/`。无需应用后端。

## GitHub Pages

仓库现有 `.github/workflows/pages.yml` 会在 `main` 推送或手动触发时：安装构建依赖 → 生成页面 → 检查链接 → 上传 `_site` → 发布。

保留 CNAME `www.filmmmer.com`。仅上传 `_site/`，不要把整个仓库作为发布目录，以免带上旧图和内部文档。

`deploy.sh` 沿用仓库原有提交及推送流程，现在先构建并检查。只有准备好对外发布时才执行；这次实现没有自动运行发布。

## 其他静态托管

构建命令为 `python3 scripts/build-site.py`，发布目录为 `_site`。先安装 requirements.txt 中依赖。所有页面使用相对资源路径，可部署到子路径；若换正式域名，请同步修改构建脚本中的 DOMAIN 与 CNAME。

## 内容更新

在 `content/guide` 与 `content/en/guide` 中编辑教程，在 `locales/*.json` 中编辑界面文案，然后重新构建。新增截图需记录来源、版本和用途，避免把算法预览标成应用界面截图。
