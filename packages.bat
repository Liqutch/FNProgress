@echo off
:: Check for Python Installation
py -3 --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.
IF EXIST "python-3.9.5-amd64.exe" (
    del "python-3.9.5-amd64.exe"
)

cls

ECHO Gerekli paketler yukleniyor...
TIMEOUT 3

py -3 -m pip install -U -r requirements.txt

ECHO Tamamlandi! Simdi main.py'yi calistirabilirsin.
PAUSE

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo Error^: Python yuklenmedi veya yola eklenmedi.
:: set mypath=%cd%
:: bitsadmin.exe /transfer "InstallPython" https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe %mypath%\PythonInstaller.exe

IF EXIST "python-3.9.5-amd64.exe" (
    echo Python Yukleyici hazir, simdi yukle ve/veya Python'u yola ekle.
) ELSE (
    echo Installing Python Installer now, this will take a minute or 2.
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe', 'python-3.9.5-amd64.exe')"
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe -OutFile python-3.9.5-amd64.exe"   
    echo Python Yukleyici hazir, simdi yukle ve/veya Python'u yola ekle.
)

cmd /k