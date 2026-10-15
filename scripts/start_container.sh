#!/bin/bash
set -e

cd /home/ubuntu/student-result-predictor

docker build -t student-result-predictor:latest .

docker rm -f student-app 2>/dev/null || true

docker run -d \
    --name student-app \
    --restart unless-stopped \
    -p 5000:5000 \
    student-result-predictor:latest

