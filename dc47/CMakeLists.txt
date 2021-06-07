cmake_minimum_required(VERSION 3.10)
project(problem VERSION 1.0)
add_library (problem SHARED prob.cpp)
target_include_directories (problem PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(problem PROPERTIES PREFIX "") #set prefix to blank

add_library (solution SHARED solution.cpp)
target_include_directories (solution PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(solution PROPERTIES PREFIX "") #set prefix to blank

#add_library (unittest SHARED test.cpp)
#target_include_directories(test PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
#set_target_properties(unittest PROPERTIES PREFIX "") #set prefix to blank


add_executable(main main.cpp)
target_link_libraries(main LINK_PUBLIC problem solution)
