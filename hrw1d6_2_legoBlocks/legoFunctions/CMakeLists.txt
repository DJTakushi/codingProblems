list(APPEND SOURCE_FILES legoFunctions.cpp)
list(APPEND PUBLIC_HEADER_FILES legoFunctions.h)

configure_file(legoFunctions.h legoFunctions.h)

# option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

set(LIB_NAME_STATIC "legoFunctionsStatic")
add_library(${LIB_NAME_STATIC} ${SOURCE_FILES})

set(LIB_NAME "legoFunctions")
add_library(${LIB_NAME} SHARED ${SOURCE_FILES})
# set_target_properties(${LIB_NAME} PROPERTIES PUBLIC_HEADER ${PUBLIC_HEADER_FILES})

# INTERFACE means things that consumers require but the producer doesn't.
# https://cmake.org/cmake/help/latest/guide/tutorial/Adding%20Usage%20Requirements%20for%20a%20Library.html
# target_include_directories(${LIB_NAME}
  # INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
# )

INSTALL(TARGETS ${LIB_NAME_STATIC} DESTINATION legoBlocks/legoFunctions)
INSTALL(TARGETS ${LIB_NAME} DESTINATION legoBlocks/legoFunctions)
INSTALL(FILES ${PUBLIC_HEADER_FILES} DESTINATION legoBlocks/legoFunctions)
