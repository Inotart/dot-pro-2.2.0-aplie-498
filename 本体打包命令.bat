@echo off
cd /d %~dp0
del main.exe > nul
echo ת    ... 
move dist\*.exe dist\..
choice /t 1 /d y /n > nul
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q __pycache__
del /f /s /q *.spec
pyinstaller --clean -Fc  --version-file=file_version_info.txt main.py -i logo.ico --add-data fbconn.dll;. --add-data libfbconn.so;.
move dist\*.exe dist\..
echo      
pause