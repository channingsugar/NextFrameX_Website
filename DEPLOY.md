# 部署指南

## 📦 Git 仓库已初始化

本地 Git 仓库已创建并完成初始提交。

## 🔗 连接到远程仓库

### 方法一：在 GitHub 上创建新仓库

1. 访问 [GitHub](https://github.com) 并登录
2. 点击右上角 "+" → "New repository"
3. 仓库名称：`NextFrameX_Website`（或你喜欢的名称）
4. 选择 Public 或 Private
5. **不要**初始化 README、.gitignore 或 license（我们已经有了）
6. 点击 "Create repository"

### 方法二：连接到现有仓库

如果你已经有远程仓库，使用以下命令连接：

```bash
cd /Users/chill/Desktop/FILM_CODING/NextFrameX_Website

# 添加远程仓库（替换 YOUR_USERNAME 和 REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 或者使用 SSH
git remote add origin git@github.com:YOUR_USERNAME/REPO_NAME.git

# 推送到远程仓库
git branch -M main
git push -u origin main
```

## 🚀 快速部署到 Vercel

### 步骤 1：推送代码到 GitHub

```bash
# 如果还没有添加远程仓库，先添加
git remote add origin https://github.com/YOUR_USERNAME/NextFrameX_Website.git
git branch -M main
git push -u origin main
```

### 步骤 2：在 Vercel 部署

1. 访问 [vercel.com](https://vercel.com) 并登录（使用 GitHub 账号）
2. 点击 "Add New Project"
3. 导入你的 GitHub 仓库 `NextFrameX_Website`
4. 配置：
   - Framework Preset: Other
   - Root Directory: `./`
   - Build Command: （留空）
   - Output Directory: （留空）
5. 点击 "Deploy"
6. 几秒钟后，网站就会上线！

### 步骤 3：自定义域名（可选）

1. 在 Vercel 项目设置中，进入 "Domains"
2. 添加你的自定义域名
3. 按照提示配置 DNS 记录

## 🌐 部署到 Netlify

### 方法一：通过 Git 部署

1. 访问 [netlify.com](https://netlify.com) 并登录
2. 点击 "Add new site" → "Import an existing project"
3. 连接 GitHub 并选择仓库
4. 配置：
   - Build command: （留空）
   - Publish directory: （留空）
5. 点击 "Deploy site"

### 方法二：拖拽部署

1. 访问 [app.netlify.com/drop](https://app.netlify.com/drop)
2. 直接拖拽 `NextFrameX_Website` 文件夹
3. 立即部署完成！

## 📝 更新网站

每次更新网站后，使用以下命令：

```bash
cd /Users/chill/Desktop/FILM_CODING/NextFrameX_Website

# 查看更改
git status

# 添加更改
git add .

# 提交更改
git commit -m "更新描述"

# 推送到远程仓库
git push
```

如果使用 Vercel 或 Netlify，推送后会自动重新部署！

## ✅ 检查清单

- [x] Git 仓库已初始化
- [x] 初始提交已完成
- [ ] 已创建 GitHub 仓库
- [ ] 已连接到远程仓库
- [ ] 已推送到 GitHub
- [ ] 已部署到 Vercel/Netlify
- [ ] 网站可以正常访问

## 🎯 下一步

1. 在 GitHub 上创建仓库并推送代码
2. 选择部署平台（推荐 Vercel）
3. 配置自定义域名（可选）
4. 开始更新网站内容！

---

**提示**：如果遇到问题，检查：
- Git 是否已配置用户信息：`git config --global user.name` 和 `git config --global user.email`
- 是否有 GitHub 访问权限
- 网络连接是否正常
