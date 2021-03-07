d="2. Determine if the sum of two integers is equal to the given value\n"
d=d+"Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:\n"
d=d+"[5,7,1,2,8,4,3] targetsum=10  --> Yes(7+3, 2+8)\n"
d=d+"[5,7,1,2,8,4,3] targetsum=19  --> No\n"
d=d+"Complete in O(n)\n"
d=d+"HINT!!!  A set can be checked for a value with complexity O(1)!!!"
print(d)
tv=[]
tv.append(([5,7,1,2,8,4,3],10,True))
tv.append(([5,7,1,2,8,4,3],19,False))

def find_sum_of_two(A, val):
    hashSet=set()
    for i in A:
        compliment=val-i
        if compliment in hashSet:
            return True
        hashSet.add(i)
    return False

for test in tv:
    if (test[2]==find_sum_of_two(test[0],test[1])):
        print("Pass")
    else:
        print("FAIL!!!!!")
