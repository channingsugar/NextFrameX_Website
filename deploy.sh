#!/bin/bash
# NextFrame 官网一键部署 → GitHub Pages (www.filmmmer.com)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

SITE_URL="https://www.filmmmer.com"
PAGES_URL="https://channingsugar.github.io/NextFrameX_Website/"
ACTIONS_URL="https://github.com/channingsugar/NextFrameX_Website/actions"
BRANCH="main"

SKIP_IMAGES=0
DRY_RUN=0
COMMIT_MSG=""

usage() {
  cat <<'EOF'
用法: ./deploy.sh [选项]

一键部署到 GitHub Pages（推送后自动构建，约 1–2 分钟上线）

选项:
  -m, --message MSG   指定 commit 信息
  --skip-images       跳过 WebP 图片压缩
  --dry-run           只预览，不 commit / push
  -h, --help          显示帮助

示例:
  ./deploy.sh
  ./deploy.sh -m "更新文案"
  ./deploy.sh --skip-images
EOF
}

log() { echo "▸ $*"; }
ok()  { echo "✅ $*"; }
warn(){ echo "⚠️  $*"; }
err() { echo "❌ $*" >&2; exit 1; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    -m|--message) COMMIT_MSG="${2:-}"; shift 2 ;;
    --skip-images) SKIP_IMAGES=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) err "未知参数: $1（使用 -h 查看帮助）" ;;
  esac
done

echo ""
echo "🚀 NextFrame 一键部署"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

command -v git >/dev/null || err "未找到 git"
git rev-parse --git-dir >/dev/null 2>&1 || err "当前目录不是 git 仓库"
git remote get-url origin >/dev/null 2>&1 || err "未配置 origin 远程仓库"

CURRENT_BRANCH="$(git branch --show-current)"
[[ "$CURRENT_BRANCH" == "$BRANCH" ]] || warn "当前分支为 $CURRENT_BRANCH，将推送到 origin/$BRANCH"

# ── 1. 压缩图片 ──
if [[ "$SKIP_IMAGES" -eq 0 ]]; then
  if command -v cwebp >/dev/null; then
    log "压缩图片 (WebP)..."
    if [[ "$DRY_RUN" -eq 1 ]]; then
      echo "   [dry-run] bash scripts/optimize-images.sh"
    else
      bash "$ROOT/scripts/optimize-images.sh"
      ok "图片已更新 → assets/imgs/opt/"
    fi
  else
    warn "未安装 cwebp，跳过图片压缩（macOS: brew install webp）"
  fi
else
  log "跳过图片压缩"
fi

# ── 2. 提交变更 ──
log "检查本地变更..."
git add -A
git add -u

if git diff --cached --quiet; then
  ok "没有新的变更需要提交"
else
  if [[ -z "$COMMIT_MSG" ]]; then
    COMMIT_MSG="Deploy $(date '+%Y-%m-%d %H:%M')"
  fi
  log "提交: $COMMIT_MSG"
  if [[ "$DRY_RUN" -eq 1 ]]; then
    git diff --cached --stat
    echo "   [dry-run] git commit + git push"
  else
    git commit -m "$COMMIT_MSG"
    ok "已提交"
  fi
fi

# ── 3. 推送到 GitHub ──
log "推送到 origin/$BRANCH ..."
if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "   [dry-run] git push origin $BRANCH"
else
  git push origin "$BRANCH"
  ok "已推送，GitHub Actions 正在部署..."
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 线上地址"
echo "   $SITE_URL"
echo "   $PAGES_URL"
echo ""
echo "📋 部署进度"
echo "   $ACTIONS_URL"
echo ""
if [[ "$DRY_RUN" -eq 0 ]]; then
  echo "⏱  通常 1–2 分钟后生效，手机请强制刷新缓存"
fi
echo "✨ 完成"
echo ""
