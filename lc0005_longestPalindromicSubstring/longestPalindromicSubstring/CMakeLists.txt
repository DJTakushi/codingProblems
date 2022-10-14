list(APPEND SOURCE_FILES longestPalindromicSubstring.cpp)
list(APPEND PUBLIC_HEADER_FILES "${PROJECT_BINARY_DIR}/longestPalindromicSubstring/longestPalindromicSubstring.h")

configure_file(longestPalindromicSubstring.h.in longestPalindromicSubstring.h)

set(LIB_NAME_STATIC "longestPalindromicSubstringStatic")
add_library(${LIB_NAME_STATIC} ${SOURCE_FILES})
target_include_directories(${LIB_NAME_STATIC} PUBLIC "${PROJECT_BINARY_DIR}/longestPalindromicSubstring")

set(LIB_NAME "longestPalindromicSubstring")
add_library(${LIB_NAME} SHARED ${SOURCE_FILES})
target_include_directories(${LIB_NAME} PUBLIC "${PROJECT_BINARY_DIR}/longestPalindromicSubstring")
# set_target_properties(${LIB_NAME} PROPERTIES PUBLIC_HEADER ${PUBLIC_HEADER_FILES})

# INTERFACE means things that consumers require but the producer doesn't.
# https://cmake.org/cmake/help/latest/guide/tutorial/Adding%20Usage%20Requirements%20for%20a%20Library.html
# target_include_directories(${LIB_NAME}
  # INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
# )

INSTALL(TARGETS ${LIB_NAME_STATIC} DESTINATION lp/longestPalindromicSubstring)
INSTALL(TARGETS ${LIB_NAME} DESTINATION lp)
INSTALL(FILES ${PUBLIC_HEADER_FILES} DESTINATION lp/longestPalindromicSubstring)
