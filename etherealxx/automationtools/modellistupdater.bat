@echo off
set curdir=%~dp0
set file_path="%~1"
set file_path=%file_path:"=%
set file_path=%file_path:\=\\%
set file_path=%file_path: =^ %
set file_name=%~n0
python "%curdir%%file_name%.py"
echo.
pause