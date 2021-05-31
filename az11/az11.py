def get_all_subsets(v, sets):
  #v = list of elements
  #set = list of sets
  maxIndex=len(v)-1
  pow2=[]
  c=0
  while c <= maxIndex:
      pow2.append(pow(2,c))
      c+=1
  number=0
  listOLists=[]
  while number <= pow(2,maxIndex+1)-1:
      tempNumber=number
      idx=maxIndex
      myList=[]
      while idx >=0:
          difference=tempNumber-pow2[idx]
          #print("  number="+str(number)+" tempNumber="+str(tempNumber)+" difference="+str(difference))
          if difference >=0:
              myList.insert(0,True)
              tempNumber-=pow2[idx]
          else:
              myList.insert(0,False)
          idx-=1
      #print("number="+str(number)+" myList="+str(myList))
      listOLists.append(myList)
      number+=1
  for thisList in listOLists:
      thisSet=set()
      c=0
      for iter in thisList:
          if iter:
              thisSet.add(v[c])
          c+=1
      sets.append(thisSet)
  return sets
