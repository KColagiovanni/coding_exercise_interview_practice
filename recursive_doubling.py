def double_recur(num, days):
    if (num / 2) < target:
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
    while amount < target:  # While the amount is less than the target amount
    # while days < 60:  # While the days are less than the amount.
        if days == 0:
            days +=1
            amount +=1
        else:
            amount *= 2
            days += 1
        print(f'Days: {days} | Amount is: ${amount}')
