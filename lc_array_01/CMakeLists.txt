cmake_minimum_required(VERSION 3.27)

add_library(sol "remove_duplicates_from_sorted_array.cpp")

add_executable(test test.cpp)
target_link_libraries(test PUBLIC sol)
