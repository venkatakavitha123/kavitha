a={1,2,3,4}
b={3,4,5,6}
b.add(8)
print("add:",b)
print("union:",a.union(b))
print("difference:",a.difference(b))
print("symm diff:",a.symmetric_difference(b))
b.discard(6)
print("discard:",b)