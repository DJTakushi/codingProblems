cmake_minimum_required(VERSION 3.10)

project(lp
  VERSION 1.0
  DESCRIPTION "find the longest palindromic substring"
  HOMEPAGE_URL "https://leetcode.com/problems/longest-palindromic-substring/")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# set runtime path
SET(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/${PROJECT_NAME}")

add_subdirectory(longestPalindromicSubstring)
add_subdirectory(tests)
list(APPEND EXTRA_LIBS longestPalindromicSubstring)

# # create .h file from configurable .h.in file into output location
# TODO - resume here before initial commit
configure_file(interface/interface.h.in interface.h)
#
list(APPEND SOURCE_FILES interface/interface.cpp)
add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIBS})

# add include directories ; this adds the binary directory
target_include_directories(${PROJECT_NAME} PUBLIC "${PROJECT_BINARY_DIR}")

INSTALL(TARGETS ${PROJECT_NAME} DESTINATION lp)
INSTALL(FILES "${PROJECT_BINARY_DIR}/interface.h" DESTINATION lp/include)
