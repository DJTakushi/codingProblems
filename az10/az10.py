def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
  print("v="+str(v)+" k="+str(k)+" result="+str(result))
  if not v:
    return result

  n = len(v)
  # count is number of permutations starting with first digit (selectable indexes or"block_size")
  count = factorial(n - 1)
  selected = (k - 1) // count
  print("  count="+str(count)+" selected="+str(selected))

  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  result=find_kth_permutation(v, k, result)
  return result
