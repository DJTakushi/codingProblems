import azLinkedList as azll

d="3. Merge two sorted linked lists\n"
d=d+"  Given two sorted linked lists, merge them so that the resulting linked list is also sorted. Consider two sorted linked lists and the merged list below them as an example.\n"
d=d+"   head1->4->8->15->19->NULL"
d=d+"   head2->7->9->10->16->NULL"
d=d+"   head1->4->7->8->9->10->15->16->19->NULL"
d=d+"  Linear, O(m + n)O(m+n) where m and n are lengths of both linked lists"

tv=[]
tv.append(([4,8,15,19],[7,9,10,16],[4,7,8,9,10,15,16,19]))

def merge_sorted2(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
  if head1 == None:
    return head2
  elif head2 == None:
    return head1

  mergedHead = None;
  if head1.data <= head2.data:
    mergedHead = head1
    head1 = head1.next
  else:
    mergedHead = head2
    head2 = head2.next

  mergedTail = mergedHead

  while head1 != None and head2 != None:
    temp = None
    if head1.data <= head2.data:
      temp = head1
      head1 = head1.next
    else:
      temp = head2
      head2 = head2.next

    mergedTail.next = temp
    mergedTail = temp

  if head1 != None:
    mergedTail.next = head1
  elif head2 != None:
    mergedTail.next = head2
  return mergedHead

def merge_sorted(head1, head2):
  out=[]
  h1idx=0
  h2idx=0
  while (h1idx != (len(head1)) and h2idx != (len(head2))):
      if head1[h1idx] <= head2[h2idx]:
          out.append(head1[h1idx])
          h1idx+=1
      else:
          out.append(head2[h2idx])
          h2idx+=1
  while h1idx != (len(head1)):
      out.append(head1[h1idx])
      h1idx+=1
  while h2idx != (len(head2)):
      out.append(head2[h2idx])
      h2idx+=1

  head1=out
  #TODO: Write - Your - Code
  return head1

for test in tv:
    ll0=azll.linkedList(test[0])
    ll1=azll.linkedList(test[1])
    product=merge_sorted2(ll0.head,ll1.head)
    pyList=[]
    product.returnList(pyList)
    if test[2]==pyList:
        print("Pass")
    else:
        print("FAIL!!!!!")
        print(" expected "+str(test[2]))
        print(" received "+str(pyList))
