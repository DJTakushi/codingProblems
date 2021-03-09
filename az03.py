#https://www.educative.io/blog/crack-amazon-coding-interview-questions
import azLinkedList as azll
def printPrompt():
    print("Merge two sorted linked lists\n"
            "Given two sorted linked lists, merge them so that the\n"
            "resulting linked list is also sorted. Consider two sorted\n"
            "linked lists and the merged list below them as an example.\n"
            "   head1->4->8->15->19->NULL\n"
            "   head2->7->9->10->16->NULL\n"
            "   head1->4->7->8->9->10->15->16->19->NULL\n"
            "Linear, O(m + n)O(m+n) where m and n are lengths of both\n"
            "linked lists")

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
  return head1

import takTest as tt
def functionWrapper(data):
    return merge_sorted(data.arr1,data.arr2)
class fdata(tt.tData):
    def __init__(self,arr1,arr2):
        self.arr1=arr1
        self.arr2=arr2
class TestMe(tt.tunittest):
    def makeTestVector(self):
        self.functionWrapper=functionWrapper
        tv=list()
        tv.append(tt.testCase(fdata([4,8,15,19],[7,9,10,16]),[4,7,8,9,10,15,16,19]))
        return tv
if __name__ == "__main__":
    tt.unittest.main()
