#!/bin/bash

# NextFrameX Website 快速部署脚本

echo "🚀 NextFrameX Website 部署助手"
echo "================================"
echo ""

# 检查是否已配置远程仓库
if git remote | grep -q "origin"; then
    echo "✅ 已检测到远程仓库:"
    git remote -v
    echo ""
    read -p "是否推送到远程仓库? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📤 正在推送到远程仓库..."
        git push -u origin main
        echo "✅ 推送完成！"
    fi
else
    echo "⚠️  尚未配置远程仓库"
    echo ""
    echo "请先执行以下命令添加远程仓库："
    echo "  git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git"
    echo ""
    echo "或者运行以下命令查看部署指南："
    echo "  cat DEPLOY.md"
fi

echo ""
echo "📝 当前提交历史："
git log --oneline -5

echo ""
echo "✨ 完成！"

