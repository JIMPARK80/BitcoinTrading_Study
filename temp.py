# greeting
print("================== # greeting ===================")
def hello2():
    print("Hello World")
hello2()

# calculation
print("================== # calculation ===================")
def cal1():
    print(3 + 5)
    print(5 - 3)
    print(5 / 3)
    print(5 * 3)
cal1()

# variable
print("================== # variable ===================")
def bit01():
    bit = 9751000
    print(bit * 3)
bit01()

# indexing
print("================== # indexing ===================")
def bit02():
    myCoin = "Bitcoin"
    print(myCoin[0])
    print(myCoin[1])
    print(myCoin[3])
    print(myCoin[-1])
    print(myCoin[-2])
bit02()

# slicing
print("================== # slicing ===================")
def bit02():
    myCoin = "hello jim"
    currency1 = "etc_ktw"
    currency2 = "eth_ktw"
    currency3 = "btc_ktw"
    print(myCoin[:5])
    print(myCoin[:7])
    print(myCoin[6:])
    print(myCoin[-5:])
    print(currency1[:3])
    print(currency2[:3])
    print(currency3[:3])
bit02()

# len
print("================== # len ===================")
def bit03():
    myCoin = "hello World"
    print(len(myCoin))
bit03()

# list
print("================== list ===================")
def bit04():
    myCoin = ["bitcoin", "ethereum", "ripple" ]
    print(myCoin)
    print(myCoin[0],myCoin[2])
    print(myCoin[:-1])
    print(myCoin[1:])
bit04()

# list modify
print("================== list modify ===================")
def bit05():
    portfolio = ["bitcoin","ethereum","ripple"]
    print(portfolio)
    portfolio[0] = "bitcash"
    print(portfolio)
    # *.append()
    portfolio.append("solana")
    print(portfolio)
    portfolio.append("dogdge coin")
    print(portfolio)
    # *.insert()
    portfolio.insert(0, "Dash")
    print(portfolio)
    # del
    del portfolio[1]
    print(portfolio)
    portfolio.insert(1, "bitcoin")
    print(portfolio)
bit05()

# max/min value
print("================== max/min value ===================")
def bit06():
    find_bitCoin_Close = [45000,43000,42000,47500,43200]
    print(max(find_bitCoin_Close))
    print(min(find_bitCoin_Close))
bit06()

# average
print("================== average ===================")
def bit07():
    a = [1,2,3,4]
    average = sum(a)/len(a)
    print(average)
bit07()

# dict
print("================== dict ===================")
def bit08():
    prices = {}
    prices['BTC'] = 45000
    prices['XRP'] = 1.2
    print(prices)
    # dict indexing
    print(prices['BTC'])
    print(prices['XRP'])
    # dict data adding
    prices['ETH'] = 2200
    print(prices)
    print(prices['ETH'])
    print(prices.keys())
    print(prices.values())
bit08()

# if statements
print("================== if statements ===================")
def bit09():
    bitcoin_ma5 = 43000
    bitcoin_price = 43500
    bitcoin_target = 45300
    if bitcoin_price >= bitcoin_ma5 and bitcoin_price < bitcoin_target:
        print("bullish trend and volatility breakthrough strategy conditions are met")
bit09()

# practice01
print("================== practice01 ===================")

def practice01():
    num1 = 10
    num2 = 20
    print(max(num1, num2))
practice01()

# practice02
print("================== practice02 ===================")
def practice02():
    score_stu = 91
    if(score_stu >= 90 and score_stu <= 100):
        print("A grade")
    elif (score_stu >= 80 and score_stu <= 89):
        print("B grade")
    elif (score_stu >= 60 and score_stu <= 79):
        print("C grade")
    elif (score_stu >= 50 and score_stu <= 59):
        print("D grade")
    else:
        print("F")
practice02()
# repeat statements
# [for] variable [in] data structure
print("================== repeat statement ===================")
def bit10():
    for value in ['A', 'B', 'C', 'D', 'E' ]:
        print(value)
bit10()

def bit11():
    bitcoin =  [45000, 43200, 44500, 48522, 42150, 45212]
    for close in bitcoin:
        print(close)
    print("max close:", max(bitcoin))
    print("min close:" , min(bitcoin))
bit11()

# range , [for] num [in] [range()]
print("================== for range  ===================")
def bit12():
    number = [1, 2, 3, 4, 5, 6, 7]
    for number in range(1,6):
        print(number)
    # range and offset
    for number in range(1,7,2):
        print(number)
bit12()

# for & dict {}
#  binding key and value using [for] ~ [in] ~.items() 
print("================== for & dict  ===================")
print("====#  binding key and value using [for] A, B [in] dict.items() --> print(A , B) ===")
def bit13():
    cur_price = {"BTC" : 45000, "XRP": 1.2, "ETH": 2200, "DASH": 200}
    for ticker, price in cur_price.items():
        print(ticker, price)
bit13()
print("====#  binding key and value using [for] A [in] dict --> print(A, dict[A]) ===")
def bit14():
    cur_price = {"BTC" : 45000, "XRP": 1.2, "ETH": 2200, "DASH": 200}
    for ticker in cur_price:
        print(ticker, cur_price[ticker])
bit14()

print(" =========== while =============== ")
print(" =========== # while, while True: --> use if statement, then use break and incremental =============== ")
def bit15():
    num = 1
    while True:
        if num == 12:
            break
        print(num)
        num = num + 1
bit15()
