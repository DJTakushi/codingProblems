# dc22
Daily Coding Problem: Problem #22 [Medium] \
This problem was asked by Microsoft. \
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string \"thequickbrownfox\", you should return ['the', 'quick', 'brown', 'fox']. \
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string \"bedbathandbeyond\", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

## Notes
Naive algorithm would be to evaluate the start of the string until x chars until gets a hit in the word list.  Then remove that word. \
HOWEVER, we'd have troulbe if it misidentified a word, shown below
- dict: the theatre
- input = "theatre"

'the' gets selected, but "atre" remains, which isn't covered - fails \

Will have to somehow backtrack or open up multiple paths just go back to last word and try again.  Do this clause until you make it or fail.
