#!/bin/bash

# 激活Python虚拟环境
source ./venv/bin/activate

# 运行main.py，并将输出重定向到log.txt
nohup python3 interference/app.py >> log.txt 2>&1 &
