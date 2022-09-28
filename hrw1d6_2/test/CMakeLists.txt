cmake_minimum_required(VERSION 3.10)
project(legoBlocksTest
  VERSION 1.0
  DESCRIPTION "counts ways a lego-wall can be built. Params [1] (m n) pair count [2-] pairs"
  HOMEPAGE_URL "https://www.hackerrank.com/dashboard")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

list(APPEND EXTRA_LIBS legoFunctions)
target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIBS})
target_include_directories(${PROJECT_NAME} PUBLIC
                            "${PROJECT_BINARY_DIR}"
                          )

add_executable(${PROJECT_NAME} test.cpp)
