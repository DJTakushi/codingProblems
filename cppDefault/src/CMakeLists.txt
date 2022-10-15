list(APPEND SOURCE_FILES solution.cpp)
list(APPEND PUBLIC_HEADER_FILES "${PROJECT_BINARY_DIR}/src/solution.h")

configure_file(solution.h.in solution.h)


set(LIB_NAME_STATIC "solutionStatic")
add_library(${LIB_NAME_STATIC} ${SOURCE_FILES})
target_include_directories(${LIB_NAME_STATIC} PUBLIC "${PROJECT_BINARY_DIR}/src")

set(LIB_NAME "solution")
add_library(${LIB_NAME} SHARED ${SOURCE_FILES})
target_include_directories(${LIB_NAME} PUBLIC "${PROJECT_BINARY_DIR}/src")
# set_target_properties(${LIB_NAME} PROPERTIES PUBLIC_HEADER ${PUBLIC_HEADER_FILES})

# INTERFACE means things that consumers require but the producer doesn't.
# https://cmake.org/cmake/help/latest/guide/tutorial/Adding%20Usage%20Requirements%20for%20a%20Library.html
# target_include_directories(${LIB_NAME}
  # INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
# )

INSTALL(TARGETS ${LIB_NAME_STATIC} DESTINATION cppDefault/solution)
INSTALL(TARGETS ${LIB_NAME} DESTINATION cppDefault)
INSTALL(FILES ${PUBLIC_HEADER_FILES} DESTINATION cppDefault/solution)
