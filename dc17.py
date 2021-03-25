
def printProblem():
    print("Daily Coding Problem: Problem #17 [Hard]\n"
            "This problem was asked by Google.\n"
            "Suppose we represent our file system by a string in the\n"
            "following manner:\n"
            "The string \"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\" represents:\n"
            "dir\n"
            "  subdir1\n"
            "  subdir2\n"
            "    file.ext\n"
            "The directory dir contains an empty sub-directory subdir1 and a\n"
            "sub-directory subdir2 containing a file file.ext.\n"
            "The string \"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\" \n"
            "represents:\n"
            "dir\n"
            "    subdir1\n"
            "        file1.ext\n"
            "        subsubdir1\n"
            "    subdir2\n"
            "        subsubdir2\n"
            "            file2.ext\n"
            "The directory dir contains two sub-directories subdir1 and\n"
            "subdir2. subdir1 contains a file file1.ext and an empty\n"
            "second-level sub-directory subsubdir1. subdir2 contains a\n"
            "second-level sub-directory subsubdir2 containing a file file2.ext.\n"

            "We are interested in finding the longest (number of characters)\n"
            "absolute path to a file within our file system. For example, in\n"
            "the second example above, the longest absolute path is\n"
            "\"dir/subdir2/subsubdir2/file2.ext\", and its length is 32\n"
            "(not including the double quotes).\n"

            "Given a string representing the file system in the above format,\n"
            "return the length of the longest absolute path to a file in the\n"
            "abstracted file system. If there is no file in the system,\n"
            "return 0.\n"

            "Note:\n"
            "The name of a file contains at least a period and an extension.\n"
            "The name of a directory or sub-directory will not contain a period.")

def maxFilePathLen(fs):
    recordString = ""
    path=list()
    eList=fs.split("\\")
    while len(eList) != 0:
        if len(path)==0:
            path.append(eList.pop(0))
        level=0
        while eList[0] == "n" or eList[0] == "t":#get level from markers
            eList.pop(0)
            level+=1
        while len(path)>level: #trim current path until appropriate
            path.pop(-1)
        name=eList.pop(0)
        name=name[1:] #get rid of starting t
        path.append(name)
        if "." in name:
            fileString=""
            for i in range(len(path)):
                fileString+=path[i]
                if i < len(path)-1:
                    fileString+="/"
            if len(fileString)>len(recordString):
                recordString=fileString
    return len(recordString)



import unittest
class myTest(unittest.TestCase):
    def testThis(self):
        self.assert(32, maxFilePathLen("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
if __name__=="__main__":
    unittest.main()
