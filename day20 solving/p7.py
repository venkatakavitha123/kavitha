import json
inp = '{"name":"alice","age":30}'
result1 = json.loads(inp)
result2 = json.dumps(result1)
print(result2)
