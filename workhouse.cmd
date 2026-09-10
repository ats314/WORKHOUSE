@echo off
setlocal
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "TARGET_DIR=%~dp0REPO"
if not exist "%TARGET_DIR%\pyproject.toml" set "TARGET_DIR=%~dp0"
pushd "%TARGET_DIR%"
uv run --no-sync workhouse %*
set "ERR=%ERRORLEVEL%"
popd
exit /b %ERR%