@echo off
title AquaIntel - Advanced Groundwater Prediction System
color 0A

echo.
echo ========================================
echo   AQUAINTEL CAPSTONE PROJECT
echo   Advanced AI Groundwater Prediction
echo ========================================
echo.

echo [1/3] Checking Python environment...
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

echo [2/3] Activating environment...
call venv\Scripts\activate.bat

echo [3/3] Starting Advanced Backend API...
echo.
echo Backend will start on: http://localhost:8000
echo.
echo API Endpoints:
echo   - POST /api/v1/predict (Ensemble - 5 models)
echo   - POST /api/v1/predict/transformer (Attention mechanism)
echo   - POST /api/v1/predict/comprehensive (All models + satellite + 3D)
echo   - GET  /api/v1/satellite/{lat}/{lon} (Multi-source satellite)
echo   - GET  /api/v1/geospatial/{lat}/{lon} (3D geospatial analysis)
echo   - GET  /api/v1/model/status (Model health check)
echo.
echo Opening website in browser in 3 seconds...
timeout /t 3 /nobreak >nul

start "" "website\index.html"

echo.
echo Starting backend server...
echo Press Ctrl+C to stop the server
echo.

python backend\api\main.py

pause
