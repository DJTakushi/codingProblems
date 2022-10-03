list(APPEND SOURCE_FILES addTwoNumbers.cpp)
list(APPEND PUBLIC_HEADER_FILES "${PROJECT_BINARY_DIR}/addTwoNumbers/addTwoNumbers.h")

configure_file(addTwoNumbers.h.in addTwoNumbers.h)


set(LIB_NAME_STATIC "addTwoNumbersStatic")
add_library(${LIB_NAME_STATIC} ${SOURCE_FILES})
target_include_directories(${LIB_NAME_STATIC} PUBLIC "${PROJECT_BINARY_DIR}/addTwoNumbers")

set(LIB_NAME "addTwoNumbers")
add_library(${LIB_NAME} SHARED ${SOURCE_FILES})
target_include_directories(${LIB_NAME} PUBLIC "${PROJECT_BINARY_DIR}/addTwoNumbers")
# set_target_properties(${LIB_NAME} PROPERTIES PUBLIC_HEADER ${PUBLIC_HEADER_FILES})

# INTERFACE means things that consumers require but the producer doesn't.
# https://cmake.org/cmake/help/latest/guide/tutorial/Adding%20Usage%20Requirements%20for%20a%20Library.html
# target_include_directories(${LIB_NAME}
  # INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
# )

INSTALL(TARGETS ${LIB_NAME_STATIC} DESTINATION addTwo/addTwoNumbers)
INSTALL(TARGETS ${LIB_NAME} DESTINATION addTwo)
INSTALL(FILES ${PUBLIC_HEADER_FILES} DESTINATION addTwo/addTwoNumbers)
