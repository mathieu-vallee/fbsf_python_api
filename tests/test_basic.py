#!/usr/bin/python
import sys
import fbsf_api as m

def Test1a(ac,av):
  failure = 0
  st = m.FbsfStatus.FbsfUninitialized
  while True:
    print("Starting Test1a")

    pComp = m.FbsfInstantiate("simul.xml", ac, av)
    if(pComp == 0): failure += 1
    if(failure): break

    [su,st] = m.FbsfGetStatus(pComp, st)
    if( su == m.FbsfSuccess.Failure or st != m.FbsfStatus.FbsfReady): failure += 2
    if(failure): break

    su = m.FbsfTerminate(pComp) 
    if( su == m.FbsfSuccess.Failure): failure += 4
    if(failure): break

    [su,st] = m.FbsfGetStatus(pComp, st)
    if( su == m.FbsfSuccess.Failure or st != m.FbsfStatus.FbsfTerminated): failure += 8
    if(failure): break

    [su,pComp] = m.FbsfFreeInstance(pComp)
    if( su == m.FbsfSuccess.Failure or pComp ): failure += 16
    if(failure): break

  return failure
	
if __name__ == '__main__':
  argc = len(sys.argv)
  err = Test1a(argc,sys.argv)
  if err: print("Test1a err" + err)
  sys.exit(err)
