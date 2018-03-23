monthlyInterestRate = annualInterestRate / 12
lower = balance/12
upper = (balance * (1 + monthlyInterestRate) ** 12) / 12
initial_balance = balance * 1

while True:
    mid = (upper + lower) / 2
    for i in range(11): 
        balance = (balance - mid) * (1 + monthlyInterestRate)
    
    if abs(balance - mid) < 0.01:
        print('Lowest Payment: ' + str(round(mid,2)))
        break
    elif balance > mid:
        lower = mid
        balance = initial_balance 
    elif balance < mid:
        upper = mid
        balance = initial_balance
