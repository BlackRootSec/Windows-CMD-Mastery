@echo off
setlocal
rem Low-impact learning example. Prints basic context only; it changes no system configuration.
echo Windows CMD Mastery - first session
echo.
echo Current directory:
cd
echo.
echo Account identity:
whoami
echo.
echo Windows version string:
ver
echo.
echo Script finished.
endlocal
exit /b 0
