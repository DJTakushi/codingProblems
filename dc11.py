def printProblem():
    print("Problem #11 [Medium]\n"
            "This problem was asked by Twitter.\n"
            "Implement an autocomplete system. That is, given a query\n"
            "string s and a set of all possible query strings, return all\n"
            "strings in the set that have s as a prefix.\n"
            "For example, given the query string de and the set of strings\n"
            "[dog, deer, deal], return [deer, deal].\n"
            "Hint: Try preprocessing the dictionary into a more efficient\n"
            "data structure to speed up queries.")

           #    []
           #     |
           #     d
           #    / \
           #   o   e
           #  /   / \
           # g   e   a
           #    /     \
           #   r       l
class node:
    def __init__(self,remainder,value=None):
        self.value=value
        self.children=dict() #key = letter, child node
        self.add(remainder)
    def add(self,inString):
        if not inString:
            return
        letter=inString[0]
        remainder=inString[1:]
        if letter in self.children.keys():
            self.children[letter].add(remainder)
        else:
            self.children[letter]=node(letter,remainder)
    def getAll(self,theList=None):
        if not theList:
            theList=list():
        for i in self.children:


import unittest
class myTest(unittest.TestCase):
    def test_node(self):
        headNode=node("dog")
if __name__=="__main__":
    unittest.main()
