l=[11,12,15,22,35,35,60,75,75, 75,80]
print(set(l))
freq_max = 0
freq_max_element = 0
freq_map = {}
for i in range(len(l)):
    if l[i] not in freq_map:
        freq_map[l[i]] = 1
    else:
        freq_map[l[i]] += 1
print(freq_map)


for key in freq_map:
    if freq_map[key] > freq_max:
        freq_max = freq_map[key]
        freq_max_element = key
print(freq_max_element)