post = [
    {"user":"alice","post":"hi"},
    {"user":"bob","post":"hello"},
    {"user":"alice","post":"again"},
    {"user":"x","post":"xyz"},
    {"user":"bob","post":"again"}
]

freq_map ={}
for i in post:
    user = i["user"]
    if user in freq_map:
       freq_map[user] += 1
    else:
        freq_map[user] = 1
print(freq_map)

   # if i[user] in freq_map:
    #    freq_map[i["user"]] = freq_map[i["user"]]+1
    #else:
     #   freq_map[i["user"]] = 1
#print(freq_map)


        