@echo off
color 0A
if exist %~dp0stop.flag del %~dp0stop.flag
call dc_env\Scripts\activate.bat
python EtereBot.py
pause
