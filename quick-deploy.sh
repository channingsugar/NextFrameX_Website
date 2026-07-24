#!/bin/bash
# 兼容旧入口，转发到 deploy.sh
exec "$(cd "$(dirname "$0")" && pwd)/deploy.sh" "$@"
