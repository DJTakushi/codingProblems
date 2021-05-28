def find_sum_of_two(A, val):
    hashSet=set()
    for i in A:
        compliment=val-i
        if compliment in hashSet:
            return True
        hashSet.add(i)
    return False
