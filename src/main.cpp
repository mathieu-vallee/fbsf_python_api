#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "FbsfApi.h"
#include <tuple>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {

     py::enum_<FbsfStatus>(m, "FbsfStatus")
    .value("FbsfUninitialized", FbsfUninitialized )
    .value("FbsfReady",  FbsfReady  )
    .value("FbsfProcessing",  FbsfProcessing  )
    .value("FbsfTimeOut", FbsfTimeOut )
    .value("FbsfFailedStep",  FbsfFailedStep  )
    .value("FbsfTerminated",  FbsfTerminated  )
    .export_values();
    
     py::enum_<FbsfSuccess>(m, "FbsfSuccess")
    .value("Success", Success )
    .value("Failure",  Failure  )
    .export_values();

    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: fbsf_api

        .. autosummary::
           :toctree: _generate

           FbsfInstantiate
           FbsfGetStatus
           FbsfTerminate
           FbsfFreeInstance
           FbsfGetRealData
    )pbdoc";
    
    m.def("FbsfInstantiate", [](char* fileName, int ac, std::vector<std::string> av) {
    	std::vector<char *> cstrs;
    	cstrs.reserve(av.size());
    	for (auto &s : av) cstrs.push_back(const_cast<char *>(s.c_str()));
    	return FbsfInstantiate(QString(fileName), ac, cstrs.data());
    });
    
    m.def("FbsfGetStatus", [](FbsfComponent pcomp,FbsfStatus st){
        FbsfSuccess su = FbsfGetStatus(pcomp,&st);
        return std::tuple<FbsfSuccess,FbsfStatus> {su,st};
    });
    
    m.def("FbsfTerminate", &FbsfTerminate, R"pbdoc(
        FbsfTerminate

        Some other explanation about the FbsfTerminate function.
    )pbdoc");

    m.def("FbsfFreeInstance", [](FbsfComponent pcomp) {
        FbsfSuccess su = FbsfFreeInstance(&pcomp);
        return std::tuple<FbsfSuccess,FbsfComponent> {su,pcomp};
    });
    
    m.def("FbsfGetRealData", [](FbsfComponent pcomp,std::string name,double val) {
        FbsfSuccess su = FbsfGetRealData(pcomp,name.c_str(),&val);
        return std::tuple<FbsfSuccess,double> {su,val};
   });
   
    m.def("FbsfGetIntegerData", [](FbsfComponent pcomp,std::string name,int val) {
        FbsfSuccess su = FbsfGetIntegerData(pcomp,name.c_str(),&val);
        return std::tuple<FbsfSuccess,int> {su,val};
   });
   
    m.def("FbsfDoStep", &FbsfDoStep, R"pbdoc(
        FbsfDoStep

        Some other explanation about the FbsfDoStep function.
    )pbdoc");
    
    m.def("FbsfSaveState", &FbsfSaveState, R"pbdoc(
        FbsfSaveState

        Some other explanation about the FbsfSaveState function.
    )pbdoc");
    
    m.def("FbsfRestoreState", &FbsfRestoreState, R"pbdoc(
        FbsfRestoreState

        Some other explanation about the FbsfRestoreState function.
    )pbdoc");


#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
