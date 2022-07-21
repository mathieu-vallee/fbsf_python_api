cmake_minimum_required(VERSION 3.15...3.22)

project(fbsf_api VERSION "0.0.1")

set(FBSF_HOME $ENV{FBSF_HOME})

# find qt package
find_package(Qt5Core REQUIRED)
set(QT_CORE_TARGET Qt5::Core)

if(SKBUILD)
  # Scikit-Build does not add your site-packages to the search path
  # automatically, so we need to add it _or_ the pybind11 specific directory
  # here.
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c
            "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE _tmp_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
  list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()

# Now we can find pybind11
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/main.cpp )
target_link_libraries(_core PRIVATE ${QT_CORE_TARGET} 
                      ${FBSF_HOME}/lib/release/FbsfApi.lib)

target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

include_directories(${FBSF_HOME}/FbsfFramework/FbsfApi)

install(TARGETS _core DESTINATION .)
