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
