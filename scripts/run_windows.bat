@echo off
:: Neural Elon – Windows launcher
cd /d "%~dp0\.."
echo.
echo  Neural Elon is starting...
echo.

:: If you use a virtual environment, uncomment the next 2 lines:
:: if exist venv\Scripts\activate.bat (
::     call venv\Scripts\activate.bat
:: )

python -m src.main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo  Something went wrong (error code: %ERRORLEVEL%)
    pause
) else (
    echo.
    echo  Goodbye, rocketeer!
)

pause