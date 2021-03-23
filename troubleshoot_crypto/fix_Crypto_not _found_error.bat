@echo off
title CryptoFixer
echo Current Username: %username%
C:
set /p path=Enter Pythons Version [Python 3.8 = Python38]: 
cd /Users/%username%/AppData/Local/Programs/Python/%path%/Lib/site-packages
IF NOT %ERRORLEVEL% == 0 (
echo an error occurred, may you have another version of Python?
pause
GOTO END)
IF %ERRORLEVEL% == 0 (
RENAME crypto Crypto
echo process successfully finished!
pause
GOTO END)
