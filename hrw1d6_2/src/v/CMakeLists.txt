set(LIB_NAME "legoFunctions")
add_library(${LIB_NAME} v.cpp)
target_include_directories(${LIB_NAME}
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)
INSTALL(TARGETS ${LIB_NAME} DESTINATION lib)
install(FILES v.h DESTINATION ${LIB_NAME}/include)
