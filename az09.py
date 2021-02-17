#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def printQuestion():
    print( "9.  How many ways can you make change with coins and a total amount\n"
            "    Suppose we have coin denominations of [1, 2, 5] and the total amount is 7.\n"
            "    We can make changes in the following 6 ways:\n"
            "    Denominations: 1,2,5\n"
            "    Amount: 7\n"
            "     1:  1,1,1,1,1,1,1\n"
            "     2:  1,1,1,1,1,2\n"
            "     3:  1,1,1,2,2\n"
            "     4:  1,2,2,2\n"
            "     5:  1,1,5\n"
            "     6:  2,5\n"
            "    Total Methods: 6\n"
            "  Runtime Complexity: Quadratic, O(m*n)\n"
            "  Memory Complexity: Linear, O(n)")

def solve_coin_change(denominations, amount, currentList=None):
    # TODO: Write - Your - Code
    if not denominations:
        return 0
    #print("amount="+str(amount)+" denominations="+str(denominations))
    if not currentList:
        currentList=[]
    #denominations.sort()
    output=solve_coin_change(denominations[0:len(denominations)-1],amount,currentList.copy())

    subAmount=amount-denominations[-1]
    currentList.append(denominations[-1])
    while subAmount >= 0:
        #print("subAmount= "+str(subAmount))
        if subAmount==0:
            output+=1
            print("0 at "+str(currentList))
        if subAmount >0:
            #can sub-amount be broken up by constitudents?
            output+=solve_coin_change(denominations[0:len(denominations)-1],subAmount,currentList.copy())
        currentList.append(denominations[-1])
        subAmount-=denominations[-1]

    return output

def test_solve_coin_change():
    testVector=[(([1,5,10],20),9)]
    testVector.append((([1,5,2],7),6))
    for iter in testVector:
        expectation=iter[1]
        result=solve_coin_change(iter[0][0],iter[0][1])
        if expectation==result:
            print("Pass.")
        else:
            print("FAIL!!!  Expected "+str(expectation)+" but received "+str(result))
    return


#printQuestion()
test_solve_coin_change()
