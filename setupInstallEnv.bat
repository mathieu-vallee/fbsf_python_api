@echo off

call %~dp0setupEnv.bat

rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rem Path for VISUAL compiler
rem ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
set CompilerPath="C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvarsall.bat"
if exist %CompilerPath% (
	call %CompilerPath% x64
) else (
	echo CompilerPath Invalid
	pause
	exit
)

echo %PATH%

@echo on