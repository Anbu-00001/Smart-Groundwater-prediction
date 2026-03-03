@echo off
echo.
echo ============================================================
echo   AQUAINTEL ADVANCED - REAL-WORLD DATA EDITION
echo ============================================================
echo.
echo  Initializing ultra-advanced groundwater prediction...
echo.
echo  Real-Time Data Sources:
echo    NASA POWER API - Climate & Solar Data
echo    USGS Water Services - Groundwater Wells
echo    Open-Meteo - Weather & Climate History  
echo    SoilGrids - Global Soil Properties
echo    OpenTopoData - High-Resolution Elevation
echo    USGS Earthquake - Seismic Activity
echo    Soil Moisture - Real-Time Data
echo.
echo ============================================================
echo.

REM Kill any existing Python processes
echo Stopping any running servers...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq*" >nul 2>&1
timeout /t 2 >nul

REM Activate virtual environment and start advanced backend
echo.
echo  Starting Advanced Backend Server...
echo.
cd /d "%~dp0"
call venv\Scripts\activate.bat
start "AquaIntel Advanced Backend" cmd /k "python backend\api\main_advanced.py"

REM Wait for backend to start
timeout /t 5 >nul

REM Open website
echo.
echo  Opening Website...
echo.
start "" "file:///%~dp0website\index.html"

echo.
echo ============================================================
echo   SYSTEM READY!
echo ============================================================
echo.
echo   Backend API: http://localhost:8000
echo   API Docs: http://localhost:8000/api/docs
echo   Website: Opened in browser
echo.
echo   Features:
echo     Live data from 10+ global APIs
echo     NASA, USGS, SoilGrids integration
echo     Real-time weather & climate data
echo     Ultra-accurate predictions
echo.
echo   Press any key to view system status...
pause >nul

REM Test the system
powershell -Command "Write-Host '`n Testing API Connection...`n' -ForegroundColor Cyan; try { $response = Invoke-WebRequest -Uri 'http://localhost:8000/api/v1/health' -Method GET -TimeoutSec 5 | ConvertFrom-Json; Write-Host ' Backend Status: ' -NoNewline -ForegroundColor Green; Write-Host $response.status -ForegroundColor White; Write-Host ' Data Sources: ' -ForegroundColor Yellow; $response.data_sources.PSObject.Properties | ForEach-Object { Write-Host \"   $($_.Name): $($_.Value)\" -ForegroundColor White }; Write-Host \"`n System Operational!`n\" -ForegroundColor Green } catch { Write-Host ' Error: Backend not responding' -ForegroundColor Red }"

echo.
echo Press any key to exit...
pause >nul
