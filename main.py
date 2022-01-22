#Test program

stocksInput = []
weightInput = []
overallWeight = 0

def stocksInputFn():
    print('Enter in a Stock: ')
    stockI = input()
    print(stockI)
    stocksInput.append(stockI)
    print(stocksInput)
    print('Enter the weight of ' + str(stockI))

    if overallWeight>1.0:
        stocksInput.remove(stockI)

def wieghtInputFn():
    global overallWeight
    weight1 = float(input())
    print(weight1)
    weightInput.append(weight1)
    print(weightInput)
    overallWeight+=weight1
    print(str(overallWeight))

    if overallWeight>1.0:
        print('Porfolio Weight needs to be 1.0')
        weightInput.remove(weight1)
        overallWeight-=weight1

while overallWeight < 1.0:
    stocksInputFn()
    wieghtInputFn()
    print(overallWeight)

print(stocksInput)
print(weightInput)



    #print('Your overall portfolio weight is :' + str(overallWeight))
    #if overallWeight==1.0:
     #   print('Your portfolio is perfect')
      #  break
    #if overallWeight>1.0:
     #   print('Your current portfolio weight it greater than 1')
      #  weightInput.remove(weightInput)

##
500
Ny
