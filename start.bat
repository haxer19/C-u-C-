@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
title TienThanh - Cau Ca PNV

:menu
cls
echo Yêu cầu: Python 3.11 - Nếu muốn sử dụng thư viện song song vui lòng qua server C4F
echo.
echo ==============================
echo       MENU CHỨC NĂNG
echo ==============================
echo 1 - Cài đặt thư viện
echo 2 - Chạy tool
echo 3 - Thay token
echo 99 - Thoát
echo.
set /p choice=">> "

if "!choice!"=="1" (
    if exist requirements.txt (
        echo Đang cài đặt thư viện...
        python -m pip install -r requirements.txt
        echo Cài đặt hoàn tất!
    )
    pause
    goto menu
)

if "!choice!"=="2" (
    if exist main.py (
        echo Đang chạy tool...
        start cmd /k python main.py
    )
    pause
    goto menu
)

if "!choice!"=="3" (
    set /p token="Nhập token: "
    echo { > config.json
    echo     "TOKEN": "!token!", >> config.json
    echo     "PREFIX": "kiz " >> config.json
    echo } >> config.json
    echo Done !!
    pause
    goto menu
)

if "!choice!"=="99" (
    exit
)

echo Vui lòng nhập lại.
pause
goto menu