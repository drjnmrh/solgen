@echo off

set OLD=%CD%

cd %~dp0
cd ..

call "python" -m pip install -e solgen

cd %OLD%
