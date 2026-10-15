#!/bin/bash
set -e

if ! command -v docker >/dev/null 2>&1; then
    apt-get update
    apt-get install -y docker.io
fi

systemctl enable --now docker
