import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

Symbol_count = {
    "A": 2,
    "B":4,
    "C": 6,
    "D":8
}

Symbol_value = {
    "A": 10,
    "B":6,
    "C": 3,
    "D":1
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    slots = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            slots.append(symbol)
    columns= []
    for _ in range(cols):
        column = []
        copy_slots = slots[:]
        for _ in range(rows):
            value = random.choice(copy_slots)
            column.append(value)
            copy_slots.remove(value)
        columns.append(column)
    return columns

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("enter a amount that is greater than 0")
        else:
            print("make sure you enter a actual number")
    return amount

def get_number_lines():
    while True:
        amount = input("Enter the amount of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if amount.isdigit():
            amount = int(amount)
            if amount >=1 and amount<=3 :
                break
            else:
                print("enter a valid number of lines")
        else:
            print("make sure you enter a actual number")
    return amount

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def get_bet():
    while True:
        amount = input("Enter the amount you want to bet on each line $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_BET and amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${ MAX_BET}")
        else:
            print("make sure you enter a actual number")
    return amount

def spin(balance):
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"you dont have neough to bet that amount, your current balance is ${balance} and youre currently trying to bet ${total_bet} try again")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines your total bet is ${total_bet}")
    slots= get_slot_machine_spin(ROWS,COLS,Symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,Symbol_value)
    print(f"You have won {winnings} on lines", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to start q (to quit)")
        if answer == "q":
            break
        balance += spin(balance)

main()



