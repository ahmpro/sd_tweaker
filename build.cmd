@echo off
echo It's simple example how to make single exe and copy to deploy dir on Windows
echo used py2exe to build and UPX for minify size
goto end

set project=sd_tweaker
set sourcepath=D:\some_source_path\%project%
set deploypath=C:\some_deploy_path\

python setup.py py2exe
C:\upx\upx.exe "%sourcepath%\dist\%project%.exe"
xcopy "%sourcepath%\dist\%project%.exe" "%deploypath%\%project%" /Y
:end
pause