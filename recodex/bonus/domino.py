def get_tuples(arr):
  res = []
  
  for i in range(0, len(arr), 2):
    res.append((arr[i], arr[i + 1]))
    
  return res

nums = list(map(int, input().split()))[1:]
dominos = get_tuples(nums)


