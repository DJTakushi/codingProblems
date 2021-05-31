def solve_coin_change(denominations, amount, currentList=None):
    # TODO: Write - Your - Code
    if not denominations:
        return 0
    #print("amount="+str(amount)+" denominations="+str(denominations))
    if not currentList:
        currentList=[]
    #denominations.sort()
    output=solve_coin_change(denominations[0:len(denominations)-1],amount,list(currentList))

    subAmount=amount-denominations[-1]
    currentList.append(denominations[-1])
    while subAmount >= 0:
        #print("subAmount= "+str(subAmount))
        if subAmount==0:
            output+=1
            # print("0 at "+str(currentList))
        if subAmount >0:
            #can sub-amount be broken up by constitudents?
            output+=solve_coin_change(denominations[0:len(denominations)-1],subAmount,list(currentList))
        currentList.append(denominations[-1])
        subAmount-=denominations[-1]
    return output
