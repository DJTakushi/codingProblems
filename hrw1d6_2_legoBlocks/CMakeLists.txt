cmake_minimum_required(VERSION 3.10)

project(legoBlocks
  VERSION 1.0
  DESCRIPTION "counts ways a lego-wall can be built. Params [1] (m n) pair count [2-] pairs"
  HOMEPAGE_URL "https://www.hackerrank.com/dashboard")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# set runtime path
SET(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/legoBlocks")

add_subdirectory(legoFunctions)
# add_subdirectory(interface)
# add_subdirectory(test)
list(APPEND EXTRA_LIBS legoFunctions)

# create .h file from configurable .h.in file into output location
configure_file(legoBlocksInterface/legoBlocksInterfaceConfig.h.in legoBlocksInterfaceConfig.h)

list(APPEND SOURCE_FILES legoBlocksInterface/legoBlocksInterface.cpp)
add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIBS})

# add include directories ; this adds the binary directory
target_include_directories(${PROJECT_NAME} PUBLIC "${PROJECT_BINARY_DIR}")

INSTALL(TARGETS ${PROJECT_NAME} DESTINATION legoBlocks)
INSTALL(FILES "${PROJECT_BINARY_DIR}/legoBlocksInterfaceConfig.h" DESTINATION legoBlocks/include)

# TODO test
