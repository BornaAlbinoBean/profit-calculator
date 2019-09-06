command = ''
profit_min = 250
while True:
    command = input('<Command Console> ').lower()
    if command == 'start':
        cost = int(input('what was the price? '))
        profit_margin = int(input('What do you want your profit margin to be in percentage? '))
        profit = cost * (profit_margin / 100)
        sell_price = cost + profit
        if profit < profit_min:
            print('you will want a higher margin')
            new_margin = int(input('what do you want for the new margin in percentage? '))
            new_profit = cost * (new_margin / 100)
            new_sell_price = new_profit + cost
            print(f'Profit: {new_profit}')
            print(f'What you will need to sell it at: {new_sell_price}')
        elif profit > profit_min and command == 'start':
            print(f'Profit: {profit}')
            print(f'What you will need to sell it at: {sell_price}')
        else:
            print('whaaat?')
    elif command == 'matrix':
        print('The Matrix has loaded')
    elif command == 'help':
        print('''
        help - shows this message
        start - begins calculator
        quit - quits program
        matrix - begins the matrix
        ''')
    elif command == 'quit':
        print('goodbye')
        break
    else:
        print('what?  I DONT UNDERSTAND?!?!')
