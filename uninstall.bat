@echo off

set OLD=%CD%

cd %~dp0
cd ..

call "python" -m pip uninstall -y solgen

cd %OLD%
