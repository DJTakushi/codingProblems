def sumEvenFib(maxNum):
    a,b=1,2
    sum=0
    while b <= maxNum:
        if b%2==0:
            sum+=b
        temp=a
        a=b
        b=b+temp
    return sum
