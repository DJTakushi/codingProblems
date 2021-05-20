import ctypes
libc_prob = ctypes.CDLL("/codingProblems/dc55/problem.so")
libc_prob.printProb()
libc_main = ctypes.CDLL("/codingProblems/dc55/libmain_lib.so")
libc_main.main()
libc_main.unitTest()
libc_main.restype = ctypes.c_int
answer = libc_main.unitTest()
print("    In Python: unitTest returns "+ str(answer) + "successful cases")
