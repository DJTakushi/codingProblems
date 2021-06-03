def minCost(ia):
    idxSel=list()
    sum=0
    for level in ia:
        mini=0
        record=level[0]
        for i in range(len(level)):
            if level[i]<record:
                record = level[i]
                mini=i
        if len(idxSel)==0:
            idxSel.append(mini)
            sum+=record
        else:
            irev=len(idxSel)-1
            altSum=sum
            # if mini==idxSel[irev]:
            #     #calculate alternative path
            #     while mini==idxSel[irev] and irev>0:
            #         getNextMinI
            #     if altSum+sencond < sum+first: #compare: & select
            #I'm blanking here.
