input = [(1,2),(1,3),(2,4),(4,6),(5,8),(2,7)]
flat = [item for tup in input for item in tup]
result = sorted(set(flat)) 
print(result)


# output = [1,2,3,4,5,6,7,8] sorted 