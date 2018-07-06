@ECHO OFF

pushd %~dp0

REM Command file for Sphinx API autodocumentation

if "%SPHINXAPIDOC%" == "" (
	set SPHINXAPIDOC=sphinx-apidoc
)
set SOURCEDIR=..\bitcoin
set BUILDDIR=.
set SPHINXAPIDOCOPTS=-e -M

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-apidoc' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXAPIDOC environment variable to point
	echo.to the full path of the 'sphinx-apidoc' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXAPIDOC% %SPHINXAPIDOCOPTS% -o %BUILDDIR% %SOURCEDIR%
del modules.rst
goto end

:end
popd
