from collections import defaultdict

keys = [42, 45, 7, 61, 32, 4, 13, 27, 48]
m = 16
hash = [float('inf')]*m

def count_collisions(hash):
    counter = 0
    for _, val in hash.items():
        if len(val) > 1:
            counter += 1

    return counter

def linear_hash(hash, keys):
    collisions = 0
    idx = 0
    for key in keys:
        hash_val = (key + idx)%m
        while hash[hash_val] != float('inf'):
          collisions += 1
          print("Collision in key :: ", hash_val)
          print("Existing value :: ",hash[hash_val])
          idx += 1
          print("Incrementing index :: ",idx)
          hash_val = (key + idx)%m

          if idx == m:
              break

        idx = 0
        hash[hash_val] = key
        print("Added ",key," to hash table at :: ", hash_val)

    return (hash, collisions)

def quadratic_hash(hash, keys):
  collisions = 0
  idx = 0
  for key in keys:
    hash_val = (key + (idx // 2) + ((idx**2)//2))%m
    while hash[hash_val] != float('inf'):
      collisions += 1
      print("Collision in key :: ", hash_val)
      print("Existing value :: ",hash[hash_val])
      idx += 1
      print("Incrementing index :: ",idx)
      hash_val = (key + (idx // 2) + ((idx**2)//2))%m

      if idx == m:
        break

    idx = 0
    hash[hash_val] = key
    print("Added ",key," to hash table at :: ", hash_val)

  return (hash, collisions)

def double_hash(hash, keys):
    collisions = 0
    idx = 0
    for key in keys:
        hash_val_2 = (key % (m-1))+1
        hash_val_1 = (key + (idx * hash_val_2)) % m
        while hash[hash_val_1] != float('inf'):
          collisions += 1
          print("Collision in key :: ", hash_val_1)
          print("Existing value :: ",hash[hash_val_1])
          idx += 1
          print("Incrementing index :: ",idx)
          hash_val_2 = (key % (m-1))+1
          hash_val_1 = (key + (idx * hash_val_2)) % m

          if idx == m:
            break

        idx = 0
        hash[hash_val_1] = key
        print("Added ",key," to hash table at :: ", hash_val_1)

    return (hash, collisions)

# res, collisions = linear_hash(hash, keys)
# print([(idx, item) for idx, item in enumerate(res)])
# print(collisions)

# hash = [float('inf')]*m
# res, collisions = quadratic_hash(hash, keys)
# print([(idx, item) for idx, item in enumerate(res)])
# print(collisions)

hash = [float('inf')]*m
res, collisions = double_hash(hash, keys)
print([(idx, item) for idx, item in enumerate(res)])
print(collisions)