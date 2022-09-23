cmake_minimum_required(VERSION 3.10)

# Project definition
project(tutorial VERSION 1.0 DESCRIPTION "Tutorial project with trivial functionality." HOMEPAGE_URL "https://www.takushi.us")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# add the MathFunctions library
option(USE_MYMATH "Use tutorial provided math implementation" ON)
if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()

# create .h file from configurable .h.in file into output location
configure_file(include/tutorialConfig.h.in include/tutorialConfig.h)

add_executable(${PROJECT_NAME} tutorial.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIBS})

# add include directories ; this adds the binary directory
target_include_directories(tutorial PUBLIC
                            "${PROJECT_BINARY_DIR}"
                          )
