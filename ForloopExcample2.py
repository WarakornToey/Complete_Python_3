
inputRound = int(input("Plaese Input Number : "))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("X"+str(x+1)+":"))
    sum += inputNumber
    print("Total = ",sum)
'''
start = int(input("Start : "))
step = int(input("Step : "))
for i in range(5):
    result=0
    result += str(start + step * i + 1 )
    print(result)
    #print(start+step*i,end=" ")
 '''