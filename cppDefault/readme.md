# cppDefault
This is a default C++ development environment.

```
project
└───README.md
└───CMakeLists.txt (head Cmake file)    
└───.gitignore   
│
└───src (where solution is typically implemented)
│   └───solution.cpp
│   └───solution.h.in (configured by cmake into out/src)
│
└───tests (function and/or unit tests)
│   test.cpp
│
└───out (create this dir yourself and build content here)
```
