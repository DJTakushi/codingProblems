def printProblem():
    print("Daily Coding Problem: Problem #22 [Medium]\n"
            "This problem was asked by Microsoft.\n"
            "Given a dictionary of words and a string made up of those words\n"
            "(no spaces), return the original sentence in a list. If there is\n"
            "more than one possible reconstruction, return any of them. If\n"
            "there is no possible reconstruction, then return null.\n"

            "For example, given the set of words 'quick', 'brown', 'the',\n"
            "'fox', and the string \"thequickbrownfox\", you should return\n"
            "['the', 'quick', 'brown', 'fox'].\n"
            "Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',\n"
            "and the string \"bedbathandbeyond\", return either ['bed', 'bath',\n"
            "'and', 'beyond] or ['bedbath', 'and', 'beyond'].")
# Naive algorithm would be to evaluate the start of the string until x chars until
# gets a hit in the word list.  Then remove that word.
# HOWEVER, we'd have troulbe if it misidentified a word, shown below
#
# dict: the theatre
# input = "theatre"
# the gets selected, but "atre" remains, which isn't covered - fails
#
# Will have to somehow backtrack or open up multiple paths
# just go back to last word and try again.  Do this clause until you make it or fail.

def stringToWordList(wordList,crushedString):
    if crushedString in wordList:
        return [crushedString]
    for i in range(len(crushedString)):
        if crushedString[0:i] in wordList:
            outList=stringToWordList(wordList,crushedString[i:])
            if outList == -1:
                continue
            else:
                outList.insert(0,crushedString[0:i])
                return outList
    return -1

import unittest
class myTest(unittest.TestCase):
    def testThis(self):
        wordList = ['quick', 'brown', 'the','fox']
        cStr="thequickbrownfox"
        expectation=['the','quick','brown','fox']
        self.assertEqual(expectation,stringToWordList(wordList,cStr))

        wordList=['the','theatre']
        cStr='theatre'
        expectation=['theatre']
        self.assertEqual(expectation,stringToWordList(wordList,cStr))
if __name__=="__main__":
    unittest.main()
