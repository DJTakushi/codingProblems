#ifndef __MAIN_H__
#define __MAIN_H__
/*
Resources:
 https://realpython.com/python-bindings-overview/#strengths-and-weaknesses
   Interfacing python with c++ content - marshalling!
 https://stackoverflow.com/questions/34380569/export-c-function-to-python-using-ctypes-undefined-symbol
   extern C required to make external
  https://stackoverflow.com/questions/2164827/explicitly-exporting-shared-library-functions-in-linux
    __declspec(dllexport), but I'm not sure I need this content(?)
*/

#include <string>
/*
#if defined(_MSC_VER)
    //  Microsoft
    #define EXPORT __declspec(dllexport)
    #define IMPORT __declspec(dllimport)
#elif defined(__GNUC__)
    //  GCC
    #define EXPORT __attribute__((visibility("default")))
    #define IMPORT
#else
    //  do nothing and hope for the best?
    #define EXPORT
    #define IMPORT
    #pragma warning Unknown dynamic link import/export semantics.
#endif
#define MY_LIB_COMPILING 1
#if MY_LIB_COMPILING
#   define MY_LIB_PUBLIC EXPORT
#else
#   define MY_LIB_PUBLIC IMPORT
#endif*/
#define BUTT //__attribute__((visibility("default")))
//#define BUTT __attribute__((visibility("default")))
extern "C" {
  BUTT bool unitTest();
}
#endif
