#Written by Kira Damo
#homework 1
#Calculating total cost of buying number of shares
#Calculating cost of selling number of shares including brokerage fee
#Calculating amount of gain or loss

print('Stock Trading Calculations')

shares = eval(input('Number of shares: '))
buyPrice = eval(input('Buy price of one share: '))
sellPrice = eval(input('Sell price of one share: '))

fee = 3/100

initialBuyPrice = shares * buyPrice
totalBuyPrice = initialBuyPrice +(fee*initialBuyPrice)
initialSellPrice = shares * sellPrice
totalSellPrice = initialSellPrice - (fee*initialSellPrice)

print('Amount invested in stock buy trade (includes fee): ', totalBuyPrice)
print('Amount received in stock sell trade (includes fee): ', totalSellPrice)

gain = round((totalSellPrice - totalBuyPrice), 2)

print('The result of the trades is a gain (or loss) of: ',gain, 'dollars')

#testcase indicating a loss
#buyPrice: 80.00
#sellPrice: 65.00
#if buyPrice > sellPrice, then result should be a loss

