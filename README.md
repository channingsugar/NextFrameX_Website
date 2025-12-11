# NextFrameX Website

NextFrameX 官方网站 - 胶片暗房级的数字冲印工具

## 项目简介

NextFrameX 是为胶片摄影师而生的数字暗房应用，提供智能色罩去除、色偏矫正、边框识别和 16-bit 导出等功能。

## 技术栈

- 纯 HTML/CSS/JavaScript
- 响应式设计
- 支持深色模式

## 本地开发

直接在浏览器中打开 `index.html` 即可预览。

## 部署

### Vercel（推荐）

1. 安装 Vercel CLI：
   ```bash
   npm i -g vercel
   ```

2. 部署：
   ```bash
   vercel
   ```

### Netlify

1. 拖拽文件夹到 [Netlify Drop](https://app.netlify.com/drop)
2. 或使用 Netlify CLI：
   ```bash
   npm i -g netlify-cli
   netlify deploy --prod
   ```

### GitHub Pages

1. 在仓库 Settings → Pages 中启用
2. 选择分支和文件夹（通常是 `main` 分支的根目录）

## 文件结构

```
NextFrameX_Website/
├── index.html          # 主页面
├── README.md          # 项目说明
└── .gitignore         # Git 忽略文件
```

## 更新日志

- 2025-02-01: 初始版本发布

## 许可证

© NextFrame Studio
