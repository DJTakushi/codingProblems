cmake_minimum_required(VERSION 3.10)
set(PNAME HelloWorld)
project(${PNAME} VERSION 1.0)

set(SOURCE
  ${SOURCE}
  main.cpp
)

add_executable(${PNAME} ${SOURCE})

target_include_directories( ${PNAME} PUBLIC "")
