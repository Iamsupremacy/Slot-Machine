import random
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
print("-------------- Welcome to Slot Machine Game --------------")
def check_winning(columns, lines, bet, value):
    winning_lines = []
    winning = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += value[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
def deposit():
    while True:
        amount = input("How much amount would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("Please enter a valid input!")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) +"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid input!")
    return lines

def get_bet_ammount():
    while True:
        bet = input("Enter the amount of bet for each line ("+str(MIN_BET) + "-" + str(MAX_BET)+"$) ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid input!")
    return bet
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_ammount()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet, Your current balance is ${balance}")
        else:
            break
    print(f"You're betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won: ${winning}")
    print(f"You won on lines:", *winning_lines)
    return winning - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        play = input("Press enter to play(Q to quit).").lower()
        if play == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}.")
main()



