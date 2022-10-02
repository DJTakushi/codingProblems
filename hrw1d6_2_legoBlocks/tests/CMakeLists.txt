cmake_minimum_required(VERSION 3.10)
project(lbTest
  VERSION 1.0
  DESCRIPTION "tests liblegoFunctions.so by default and lb with 'i' option"
  HOMEPAGE_URL "https://www.hackerrank.com/dashboard")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

list(APPEND SOURCE_FILES test.cpp testHelper.cpp)

# list(APPEND EXTRA_LIBS legoFunctions)
# target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIBS})

# target_include_directories(${PROJECT_NAME} PUBLIC
#                             "${PROJECT_BINARY_DIR}"
#                           )

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME}
  PUBLIC "${PROJECT_BINARY_DIR}/.."
  PRIVATE ${CMAKE_CURRENT_SOURCE_DIR} )
target_link_libraries(${PROJECT_NAME} PUBLIC legoFunctions)

INSTALL(TARGETS ${PROJECT_NAME} DESTINATION lb)
