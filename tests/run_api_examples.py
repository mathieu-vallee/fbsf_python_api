#!/usr/bin/python
import sys, random
import fbsf_api as m

def TestLoadSuccess(ac,av):
  st = m.FbsfStatus.FbsfUninitialized

  print("Starting Test1 - TestLoadSuccess")

  pComp = m.FbsfInstantiate("simul.xml", ac, av)
  assert(pComp is not None)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfReady)

  su = m.FbsfTerminate(pComp) 
  assert( su != m.FbsfSuccess.Failure)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfTerminated)

  [su,pComp] = m.FbsfFreeInstance(pComp)
  assert( su != m.FbsfSuccess.Failure and pComp is None)
 
  print("SUCCESS: TestLoadSuccess")
  return 0
  
def TestLoadFailure(ac,av):
  st = m.FbsfStatus.FbsfUninitialized

  print("Starting Test1 - TestLoadFailure")

  pComp = m.FbsfInstantiate("simulBof.xml", ac, av)
  assert(pComp is not None)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfUninitialized)

  m.FbsfTerminate(pComp) 
  assert( su != m.FbsfSuccess.Failure)

  [su,pComp] = m.FbsfFreeInstance(pComp)
  assert( su != m.FbsfSuccess.Failure and pComp is None)

  print("SUCCESS: TestLoadFailure")
  return 0
  
def TestSimpleSimu(ac,av):
  st = m.FbsfStatus.FbsfUninitialized
  timestep = 0.2
  timeOutCPUs = int(1e6)
  simuTimeString = "Simulation.Time"
  ZEValTime = -1
  
  print("Starting Test2 - TestSimpleSimu")

  pComp = m.FbsfInstantiate("simul.xml", ac, av)
  assert(pComp is not None)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st != m.FbsfStatus.FbsfUninitialized )
    
  [su,ZEValTime] = m.FbsfGetRealData(pComp, simuTimeString, ZEValTime)
  assert( su != m.FbsfSuccess.Failure and abs(ZEValTime) < 1e-9 )
        
  for y in range(10): 
    su = m.FbsfDoStep(pComp, timeOutCPUs)
    assert( su != m.FbsfSuccess.Failure)
    [su,st] = m.FbsfGetStatus(pComp, st)
    assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfReady)
    [su,ZEValTime] = m.FbsfGetRealData(pComp, simuTimeString, ZEValTime)
    assert( su != m.FbsfSuccess.Failure and abs(ZEValTime - (y+1)*timestep) < 1.e-6 )
    
  su = m.FbsfTerminate(pComp) 
  assert( su != m.FbsfSuccess.Failure)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfTerminated)

  [su,pComp] = m.FbsfFreeInstance(pComp)
  assert( su != m.FbsfSuccess.Failure and pComp is None )
  
  print("SUCCESS: TestSimpleSimu")
  return 0
  
def TestSimpleSimuFMU(ac,av):
  st = m.FbsfStatus.FbsfUninitialized
  timestep = 0.05
  timeOutCPUs = int(1e6)
  simuTimeString = "Simulation.Time"
  ZEValTime = -1

  print("Starting Test2b - TestSimpleSimuFMU")

  pComp = m.FbsfInstantiate("TestFMU_Crash2.xml", ac, av)
  assert(pComp is not None)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st != m.FbsfStatus.FbsfUninitialized )
    
  [su,ZEValTime] = m.FbsfGetRealData(pComp, simuTimeString, ZEValTime)
  assert( su != m.FbsfSuccess.Failure and abs(ZEValTime) < 1.e-9 )
    
  for y in range(10): 
    su = m.FbsfDoStep(pComp, timeOutCPUs)
    assert( su != m.FbsfSuccess.Failure)
    [su,st] = m.FbsfGetStatus(pComp, st)
    assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfReady )
    [su,ZEValTime] = m.FbsfGetRealData(pComp, simuTimeString, ZEValTime)
    assert( su != m.FbsfSuccess.Failure and abs(ZEValTime - (y+1) * timestep) < 1.e-6)
    
  su = m.FbsfTerminate(pComp)
  assert( su != m.FbsfSuccess.Failure ) 
  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfTerminated)

  [su,pComp] = m.FbsfFreeInstance(pComp)
  assert( su != m.FbsfSuccess.Failure and pComp is None)

  print("SUCCESS: TestSimpleSimuFMU")
  return 0
  
def TestWallClock(ac,av):
  st = m.FbsfStatus.FbsfUninitialized
  timestep = 0.2
  timeOutCPUs = int(1e-8)
  simuTimeString = "Simulation.Time"
  ZEValTime = -1

  print("Starting Test3 - TestWallClock")

  pComp = m.FbsfInstantiate("simul.xml", ac, av)
  assert(pComp is not None)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st != m.FbsfStatus.FbsfUninitialized )
  
  [su,ZEValTime] = m.FbsfGetRealData(pComp, simuTimeString, ZEValTime)
  assert( su != m.FbsfSuccess.Failure and abs(ZEValTime) < 1.e-9)
  
  for y in range(10): 
    
    su = m.FbsfDoStep(pComp, timeOutCPUs)
    assert( su != m.FbsfSuccess.Failure )
    
    [su,st] = m.FbsfGetStatus(pComp, st)
    assert( su != m.FbsfSuccess.Failure )
    
    [su,ZEValTime] = m.FbsfGetRealData(pComp, simuTimeString, ZEValTime)
    assert( su != m.FbsfSuccess.Failure and abs(ZEValTime - (y+1) * timestep) < 1.e-6)
    
  su = m.FbsfTerminate(pComp) 
  assert( su != m.FbsfSuccess.Failure )
  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfTerminated)

  [su,pComp] = m.FbsfFreeInstance(pComp)
  assert( su != m.FbsfSuccess.Failure and pComp is None)

  print("SUCCESS: TestWallClock")
  return 0
  
def TestSaveRestore(ac,av):
  st = m.FbsfStatus.FbsfUninitialized
  timestep = 0.05
  timeOutCPUs = int(1e6)
  simuTimeString = "Simulation.Time"
  TimeInt = "OutPutTimeIntegrator"
  TimeValFMU = "Time"
  ZEkeys = {simuTimeString, TimeInt, TimeValFMU}
  ZEValTime = -1
  ZEFMUTimeInt = -1
  ZEFMUTime = -1
  ZEValTimeSave = -1
  ZEFMUTimeIntSave = -1
  ZEFMUTimeSave = -1
  pZEValRef = -1

  print("Starting Test4 - TestSaveRestore")

  pComp = m.FbsfInstantiate("TestFMU_Crash2.xml", ac, av)
  assert (pComp is not None)

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st != m.FbsfStatus.FbsfUninitialized )
    
  [su,pZEValRef] = m.FbsfGetRealData(pComp, simuTimeString, pZEValRef)
  assert( pZEValRef != -1 )
    
  su = m.FbsfDoStep(pComp, timeOutCPUs)
  assert( su != m.FbsfSuccess.Failure )

  [su,pZEValRef] = m.FbsfGetRealData(pComp, simuTimeString, pZEValRef)
    
  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfReady and abs(pZEValRef - expectedVal) > 1.e-5 )
    
  su = m.FbsfTerminate(pComp) 

  [su,st] = m.FbsfGetStatus(pComp, st)
  assert( su != m.FbsfSuccess.Failure and st == m.FbsfStatus.FbsfTerminated)

  [su,pComp] = m.FbsfFreeInstance(pComp)
  assert( su != m.FbsfSuccess.Failure and pComp is None)

  print("OK")
  return 0
	
if __name__ == '__main__':
  argc = len(sys.argv)
  if argc < 2:
    print("Need id of test to run")
    print("Usage ", sys.argv[0], " <args to pass to FBSF> ", " <id = 0 to 5> ")
    sys.exit()
  else:
    i = int(sys.argv[1])
    print("Running test ", i)
 # i= random.randrange(6)
 #  i = 0

  if i == 0:
    err = TestLoadSuccess(argc,sys.argv[:-1])
    if err: 
      print("TestLoadSuccess err="+str(err))
  elif i == 1:
    err = TestLoadFailure(argc,sys.argv[:-1])
    if err: 
      print("TestLoadFailure err="+str(err))
  elif i == 2:
    err = TestSimpleSimu(argc,sys.argv[:-1])
    if err: 
      print("TestSimpleSimu err="+str(err))
  elif i == 3:
    err = TestSimpleSimuFMU(argc,sys.argv[:-1])
    if err: 
      print("TestSimpleSimuFMU err="+str(err))
  elif i == 4:
    err = TestWallClock(argc,sys.argv[:-1])
    if err: 
      print("TestWallClock err="+str(err))
  elif i == 5:
    err = TestSaveRestore(argc,sys.argv[:-1])
    if err: 
      print("TestSaveRestore err="+str(err))
  sys.exit(err)
