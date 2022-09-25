cmake_minimum_required(VERSION 3.10)

project(legoBlocks
  VERSION 1.0
  DESCRIPTION "counts ways a lego-wall can be built. Params [1] (m n) pair count [2-] pairs"
  HOMEPAGE_URL "https://www.hackerrank.com/dashboard")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_subdirectory(v)
list(APPEND EXTRA_LIBS getVector)

# create .h file from configurable .h.in file into output location
configure_file(include/config.h.in include/config.h)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIBS})

# add include directories ; this adds the binary directory
target_include_directories(${PROJECT_NAME} PUBLIC
                            "${PROJECT_BINARY_DIR}"
                          )

install(TARGETS ${PROJECT_NAME} DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/include/config.h"
  DESTINATION include
  )

# TODO test
