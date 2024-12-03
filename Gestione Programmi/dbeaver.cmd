set JAVA_HOME=C:\Java\jdk1.8.0_161
set PATH=%JAVA_HOME%\bin;%PATH%
for %%f in ("setEnv.cmd") DO @SET currDir_=%%~df%%~pf
start dbeaver-cli.exe -data mydata