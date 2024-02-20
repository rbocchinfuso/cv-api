@echo off

echo Commit on GitHub/GitLab
echo.

set /p comment="Enter comment: "
git.exe add .
git.exe commit -m "%comment%"
git.exe push

echo.
echo All done :)

pause
