@echo off
set /p confirm=Are you sure you want to run WSLRAG? (y/n): 
if /i "%confirm%"=="y" (
    wsl -d Ubuntu-22.04
) else (
    echo Operation canceled by user.
)
