@echo off
title Existing Network Monitoring System (http://127.0.0.1:8000)
cd /d "%~dp0"
echo ========================================================
echo Starting Unified Network Monitoring System...
echo Web Application: http://127.0.0.1:8000
echo (Python ICMP and ML Engine merged in background)
echo ========================================================
echo.
call npm run dev:all
pause
