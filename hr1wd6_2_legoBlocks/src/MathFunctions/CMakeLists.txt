add_library(MathFunctions mysqrt.cxx)
target_include_directories(MathFunctions
  # adds to consumers(who include this), but not the producer (this library)
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)

install(TARGETS MathFunctions DESTINATION lib)
install(FILES MathFunctions.h DESTINATION include)
