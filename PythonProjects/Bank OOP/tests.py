class Account:
    def __init__(self):
        self.name = input('Name: ')
        self.balance = int(input('Balance: '))
        self.card = input('Main card: ')
        self.all_cards = {self.card: self.balance}

    def deposit(self, card, amount):
        try:
            self.all_cards[card] +=amount
            print(f'Money successfully credited to card {card}')
        except KeyError as e:
            print(f'You do not have such card: {e}')

    def withdraw(self, card, amount):
        try:
            if self.all_cards[card] >= amount:
                self.all_cards[card] -= amount
                print(f'Money successfully withdrawn\nCard: {card}, balance: {self.all_cards[card]} | -{amount}')
            else:
                print(f'Not enough money\nYour balance: {self.all_cards[card]}')
        except KeyError as e:
            print(f'You do not have such card: {e}')

    def add_card(self, card):
        self.all_cards[card] = 0
        print(f'Card {card} added successfully')

    def get_balance(self):
        for key, value in self.all_cards.items():
            print(f'Card: {key}\nBalance: {value}\n')

    def transfer(self, card_from, card_to, amount):
        try:
            if self.all_cards[card_from] >= amount:
                self.all_cards[card_from] -=amount
                self.all_cards[card_to] +=amount
                print(f'The money has been successfully credited to card {card_to} ')

            else:
                print(f'Not enough money\nCard: {card_from}\nbalance: {self.all_cards[card_from]}')
        except KeyError as e:
            self.all_cards[card_from] += amount
            print(f'You do not have such card: {e}')

if __name__ == '__main__':
    user = Account()
    while True:
        command = input('Command: ')
        if command == 'deposit':
            user.deposit(card=input('Card: '), amount=int(input('Amount: ')))
        elif command == 'withdraw':
            user.withdraw(card=input('Card:'), amount=int(input('Amount: ')))
        elif command == 'add card':
            user.add_card(card=input('Card: '))
        elif command == 'balance':
            print()
            user.get_balance()
        elif command == 'transfer':
            user.transfer(card_from=input('Your card: '),
                          card_to=input('Enrollment card: '),
                          amount=int(input('Amount: ')))