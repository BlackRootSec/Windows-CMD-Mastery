@echo off
setlocal
rem Demonstrates required-argument validation without executing user-supplied input.
rem It reports the supplied label only; do not treat this as a universal escaping library.
if "%~1"=="" (
  echo Usage: %~nx0 LABEL
  echo Supply a non-empty label as the first argument.
  endlocal
  exit /b 2
)
echo Label received. No command will be constructed from this value.
endlocal
exit /b 0
