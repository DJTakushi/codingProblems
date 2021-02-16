from azBinTree import  *
#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def can_segment_string(s, dictionary):
    strLen=len(s)
    hashSet=set()
    for idx in range(strLen):
        markToContinue=False
        a=s[0:idx]
        b=s[idx:strLen]
        if a not in dictionary:
            hashSet.add(a)
            markToContinue=True
        if b not in dictionary:
            hashSet.add(b)
            markToContinue=True
        if not markToContinue:
            return True
    return False
def test_can_segment_string():
    dict={"apple","apple","pear","pie"}
    check(can_segment_string("applepie",dict),True)
    check(can_segment_string("applepeer",dict),False)
    dict={"peach","apple","pear","pie"}
    check(can_segment_string("applepie",dict),True)
    check(can_segment_string("applepeer",dict),False)
    dict={"hell","now","on","hello"}
    check(can_segment_string("hellonow",dict),True)


def check(result,expected):
    if result==expected:
        print("Pass")
    else:
        print("FAIL!!!  Expected "+str(expected)+", got "+str(result))
test_can_segment_string()
