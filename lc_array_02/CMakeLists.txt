cmake_minimum_required(VERSION 3.27)
project(lc_array_02)
add_library(sol "stock_trader.cpp")

add_executable(test test.cpp)

find_library(gtest libgtest.a)
find_library(gtest_main libgtest_main.a)

target_link_libraries(test PRIVATE gtest gtest_main PUBLIC sol)
