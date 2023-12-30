#!/bin/sh
pyinstaller -F \
            -w \
            -i ./resource/icon.ico \
            --upx-dir ./utils/upx-4.2.1-amd64_linux/ \
            ./src/main.py