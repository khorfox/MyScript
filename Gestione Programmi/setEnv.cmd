@echo off
for %%f in ("setEnv.cmd") DO @SET currDir_=%%~df%%~pf
set PATH=%currDir_%;%PATH%
for /D %%a in ("httpd*") DO @SET APACHE_INSTALL=%%~fa
set APACHE_HOME=%APACHE_INSTALL%\Apache24
set PATH=%APACHE_HOME%\bin;%PATH%
rem set MY_PROXY=http://TL001023:"slan55()"@lelapomi.telecomitalia.local:8080
rem set HTTP_PROXY=%MY_PROXY%
rem set HTTPS_PROXY=%MY_PROXY%
rem set http_proxy=%MY_PROXY%
rem set https_proxy=%MY_PROXY%
rem git config --global --unset http.proxy
rem git config --global http.proxy http://TL001023:"B1$$1ano"@lelaporm.telecomitalia.local:8080