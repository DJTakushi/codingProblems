cmake_minimum_required(VERSION 3.10)

project(test_cppDefault
  VERSION 1.0
  DESCRIPTION "DEFAULT: tests solution.so by default and interface with 'i' option"
HOMEPAGE_URL "https://www.takushi.us")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

list(APPEND SOURCE_FILES test.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME}
  PUBLIC "${PROJECT_BINARY_DIR}/.."
  PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} )

target_link_libraries(${PROJECT_NAME} PUBLIC solution)

INSTALL(TARGETS ${PROJECT_NAME} DESTINATION cppDefault)#install directory
