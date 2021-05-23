# Daily Coding Problem: Problem 55 [Easy]
This problem was asked by Microsoft.
Implement a URL shortener with the following methods:
  - shorten(url), which shortens the url into a six-character alphanumeric
      string, such as zLg6wl.
  - restore(short), which expands the shortened string into the original
      url. If no such shortened string exists, return null.
  Hint: What if we enter the same URL twice?

## Notes
First problem using python integration and a readme.md.  Would like to create a unified structure of solution/problem/main/unit-test that can be called and analyzed by a python script in the root directory.  Problem should likely just parse the readme.md file for the problem part.

#### Notable Resources:
1. https://realpython.com/python-bindings-overview/#strengths-and-weaknesses
    - Interfacing python with c++ content - marshalling!
2. https://stackoverflow.com/questions/34380569/export-c-function-to-python-using-ctypes-undefined-symbol
    - extern C required to make external
3.  https://stackoverflow.com/questions/2164827/explicitly-exporting-shared-library-functions-in-linux
    - _declspec(dllexport), but this seems to be related to visibility, an unrelated topic
4.  https://stackoverflow.com/questions/13445568/python-ctypes-how-to-free-memory-getting-invalid-pointer-error
    - example of freeing memroy
5.  https://stackoverflow.com/questions/1615813/how-to-use-c-classes-with-ctypes
    - accessing cpp objects in python difficult\]
    - possible with c-style linking!
