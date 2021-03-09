from azBinTree import  *
#https://www.educative.io/blog/crack-amazon-coding-interview-questions
stoopid=True
def level_order_traversal(root):
  result = ""
  if root==None:
      return
  levelQueue=[]
  levelQueue.append(root)
  while(len(levelQueue)):
      thisNode=levelQueue.pop(0)
      if not stoopid:
          if result=="":
              result=str(thisNode.data)
          else:
              result+=" "+str(thisNode.data)
      else:
          result+=str(thisNode.data)+" "
      if thisNode.left:
          levelQueue.append(thisNode.left)
      if thisNode.right:
          levelQueue.append(thisNode.right)
  return result

#this is what's listed online, but I don't understand why they use this
#also, their dequeue seems ridiculous
def level_order_traversalR(root):
  if root == None:
    return
  result = ""
  queues = [deque(), deque()]

  current_queue = queues[0]
  next_queue = queues[1]

  current_queue.append(root)
  level_number = 0

  while current_queue.list:
    temp = current_queue.popleft()
    result += str(temp.data) + " "

    if temp.left != None:
      next_queue.append(temp.left)

    if temp.right != None:
      next_queue.append(temp.right)

    if not current_queue.list:
      level_number += 1
      current_queue = queues[level_number % 2]
      next_queue = queues[(level_number + 1) % 2]
  return result

def test_order_traversal():
    head=node(100)
    node2=head.createLeft(50)
    node2.createLeft(25)
    node2.createRight(75)
    node2=head.createRight(200)
    node2.createRight(350)
    received=level_order_traversalR(head)
    expected="100 50 200 25 75 350 "#example online ends with an excessive space at the end.  C'MON, MAN!!!
    if received==expected:
        print("Pass")
    else:
        print("FAIL!!!")
        print("  Expected = \""+expected+"\"")
        print("  Received = \""+received+"\"")

test_order_traversal()
import takTest as tt
def functionWrapper(data):
    return find_sum_of_two(data.arr,data.target)
class fdata(tt.tData):
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
class TestMe(tt.tunittest):
    def makeTestVector(self):
        self.functionWrapper=functionWrapper
        tv=list()
        tv.append(tt.testCase(fdata([5,7,1,2,8,4,3],10),True))
        tv.append(tt.testCase(fdata([5,7,1,2,8,4,3],19),False))
        return tv
if __name__ == "__main__":
    tt.unittest.main()
