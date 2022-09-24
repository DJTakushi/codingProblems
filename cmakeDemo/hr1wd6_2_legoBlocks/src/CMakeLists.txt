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

install(TARGETS ${PROJECT_NAME} DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/include/tutorialConfig.h"
  DESTINATION include
  )

enable_testing()

# does it run
add_test(NAME RunsBlank COMMAND tutorial)
add_test(NAME Runs COMMAND tutorial 25)

# does the usage message work
add_test(NAME Usage COMMAND tutorial 25)
set_tests_properties(Usage
  PROPERTIES PASS_REGULAR_ESPRESSION "tutorial *"
  )

# define a function to simplify adding tests
function(do_test target arg result)
  add_test(NAME Comp${arg} COMMAND ${target} ${arg})
  set_tests_properties(Comp${arg}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result}
    )
endfunction()

# do a bunch of result based tests
do_test(Tutorial 4 "4 is 2")
do_test(Tutorial 9 "9 is 3")
do_test(Tutorial 5 "5 is 2.236")
do_test(Tutorial 7 "7 is 2.645")
do_test(Tutorial 25 "25 is 5")
do_test(Tutorial -25 "-25 is (-nan|nan|0)")
do_test(Tutorial 0.0001 "0.0001 is 0.01")
