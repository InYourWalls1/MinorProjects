@echo off
setlocal

set "BASEDIR=%~dp0"

set "LNK=%BASEDIR%\Dice.lnk"

::relative icon path
set "REL_ICON=dice.ico"
set "ICON=%BASEDIR%%REL_ICON%"

::create a temporary VBscript to modify the link, could have done it all in VBscript now that i think about it - oh well too late now bye
> "%temp%\modifica_icon.vbs" echo Set oWS = CreateObject("WScript.Shell")
>> "%temp%\modifica_icon.vbs" echo Set lnk = oWS.CreateShortcut("%LNK%")
>> "%temp%\modifica_icon.vbs" echo lnk.TargetPath = "%BASEDIR%dice.py"
>> "%temp%\modifica_icon.vbs" echo lnk.WorkingDirectory = "%BASEDIR%"
>> "%temp%\modifica_icon.vbs" echo lnk.IconLocation = "%ICON%"
>> "%temp%\modifica_icon.vbs" echo lnk.Save

cscript //nologo "%temp%\modifica_icon.vbs"

del "%temp%\modifica_icon.vbs"
endlocal