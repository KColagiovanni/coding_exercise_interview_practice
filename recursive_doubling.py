'''
Is taking $2,000,000,000 right now better than taking $1 that doubles every day?

Answer: Taking a dollar that doubles every day will get you over $2,000,000,000 on day 32. 
Realistically, after a couple months there isn't enough money in the world to give you the amount. After 60 days the 
amount would be $576,460,752,303,423,488. There is not currently even $1 quadrillion
'''

def double_recur(num, days):
    if (num / 2) < target:  # num/2 so the last value that is over the target is accounted for in the last iteration.
        if num == 0:
            days = 1
            double_recur(1, days)
        else:
            print(f'Days is: {days} | Amount is ${num}')
            days += 1
            return double_recur(num * 2, days)
    
if __name__ == '__main__':
    target = 2000000000
    days = 0
    amount = 0

    # Recursive method
    double_recur(amount, days)

    print('*' * 60)

    #Non-recursive method
    # while amount < target:  # While the amount is less than the target amount
    while days < 60:  # While the days are less than the amount. For seeing what the amunt would be in x number of days.
        if days == 0:
            days +=1
            amount +=1
        else:
            amount *= 2
            days += 1
        print(f'Days: {days} | Amount is: ${amount}')
