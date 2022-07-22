@echo off

call %~dp0setupEnv.bat

cd %~dp0..\Fbsf-DevApi\Tests\testMini

set APP_HOME=. 

python ..\..\..\fbsf_python_api\tests\run_api_examples.py 0