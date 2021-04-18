# Create a library called "Hello" which includes the source file "hello.cxx".
# The extension is already found. Any number of sources could be listed here.
set(PNAME hello)
set(CMAKE_BUILD_TYPE Release)

add_library (${PNAME} SHARED hello.cpp)

# Make sure the compiler can find include files for our Hello library
# when other libraries or executables link to Hello
target_include_directories (${PNAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
