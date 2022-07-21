fbsf_api
==============

This a a fork of pybind/scikit_build_example:master to build the FBSF API using Pybind11

Installation
------------

1. clone this repository
2. open a terminal with a python install available 
(using a clean python install, virtual env or conda env is prefered)
3. setup environement variables for FBSF (see below)
4. `python -m pip install --upgrade pip`
5. `pip install pytest pybind11 cmake scikit-build`
6. `pip install ./fbsf_api`

Setting up link to FBSF
------------

You need a valid FBSF install with API properly compiled for this to work

If you have a variable FBSF_HOME pointing to your FBSF install, 
the following should set up the all the variables

call %FBSF_HOME%\QtVersion.bat
call %FBSF_HOME%\fbsfenv.bat release

You may also need to set up a compiler (e.g. using vcvarsall.bat)

The script setupEnv.bat provides some examples of how to do so (should be improved)

License
-------

pybind11 is provided under a BSD-style license that can be found in the LICENSE
file. By using, distributing, or contributing to this project, you agree to the
terms and conditions of this license.

Test call
---------

```python
import fbsf_api
pComp = m.FbsfInstantiate("simul.xml", ac, av)
```

See test/run_api_examples.py for more details
See also SampleTestResults.md for sample results