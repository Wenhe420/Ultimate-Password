from random import randint
min = 1
max = 500
S = randint(min,max)
RS = 0
print(str(min) + '-' + str(max))
RS = input("A:")
if int(RS) > int(S):
    max = RS
    print(str(min) + '-' + str(max))
if int(RS) < int(S):
    min = RS
    print(str(min) + '-' + str(max))
def F():
    global min
    global max
    global RS
    if int(RS) > int(S):
        max = RS
        print(str(min) + '-' + str(max))
    if int(RS) < int(S):
        min = RS
        print(str(min) + '-' + str(max))

def T():
    global S
    global RS
    if int(RS) == int(S):
        print("pass")
        exit(0)
        
while True:
    RS = input("A:")
    T()
    F()