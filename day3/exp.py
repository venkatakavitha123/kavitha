import arth
num_1=int(input())
while True:
    op=input()
    if op=="=":
        print("End of the calculator result:",num_1)
        break
    num_2 = int(input())
    if op=="+":
        num_1 =arth.add(num_1,num_2)
    if op=="-":
        num_1=arth.sub(num_1,num_2)
    if op=="*":
        num_1=arth.mul(num_1,num_2)
    if op=="/":
        num_1=arth.div(num_1,num_2)
    if op=="%":
        num_1=arth.mod(num_1,num_2)
    if op=="**":
        num_1=arth.pow(num_1,num_2)