## Utilisation des tests

Après avoir installé l'API

1. Ouvrir un terminal dans essai_pybind
2. Taper les commandes
>setupEnv.bat
>cd ..\Fbsf-DevApi\Tests\testMini  
>set APP_HOME=.
>python ..\..\..\fbsf_python_api\tests\run_api_examples.py <i> 

### Avec i=0 
Starting Test1 - TestLoadSuccess
SUCCESS: TestLoadSuccess

### Avec i=1 
Starting Test1 - TestLoadFailure
Error: configuration provided is invalid
Error: no instance
Error: no instance
SUCCESS: TestLoadFailure

### Avec i=2 
Starting Test2 - TestSimpleSimu
SUCCESS: TestSimpleSimu

### Avec i=4 
Starting Test3 - TestWallClock
SUCCESS: TestWallClock

>cd Fbsf-DevApi\Tests\testFMU_1
>set APP_HOME=.
>python ..\..\..\fbsf_python_api\tests\test_api.py 

### Avec i=3 
Starting Test2b - TestSimpleSimuFMU
SUCCESS: TestSimpleSimuFMU
ok TestFMU_TestSaveRestoreState_Crash2_Radau (Log): Integration terminated successfully at T = 0.5
...

### Avec i=5 
TODO