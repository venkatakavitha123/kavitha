#class Solution:
 #   def secondHighest(self, s: str) -> int:
s = "bdd12g43hh"
digits = set()
for i in s:
    if i.isdigit():
        digits.add(int(i))
    sorted_digits = sorted(digits,reverse=True)
    if len(sorted_digits) >= 2:
        print(sorted_digits[1])
    else:
        print(-1)
        
        