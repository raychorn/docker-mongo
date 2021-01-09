@echo off

virtualenv --python C:\Python38\python3.8.exe -v .venv

./.venv/bin/activate.cmd
pip install --upgrade pip

