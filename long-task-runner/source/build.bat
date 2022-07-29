@echo off
pyinstaller main.spec
wsl mv ./dist/ltrun.exe ../release
wsl rm -rf ./dist/ ./build