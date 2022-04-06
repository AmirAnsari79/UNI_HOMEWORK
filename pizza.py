PRICE = {
    'size': {
        'small': 10,
        'normal': 12,
        'large': 15,
        'family': 20,
    },
    'food': {
        'cheese': 1,
        'pepperoni': 2,
        'ham': 3
    }
}


class Pizza:
    def __init__(self, size, cheese_toppings, pepperoni_toppings, ham_toppings):
        self.set_size(size)
        self.set_cheese_toppings(cheese_toppings)
        self.set_pepperoni_toppings(pepperoni_toppings)
        self.set_ham_toppings(ham_toppings)

    @classmethod
    def prompt(cls):
        try:
            size, cheese_toppings, pepperoni_toppings, ham_toppings = input(
                f'choice size {",".join(PRICE["size"])} and'
                f' choice cheese_toppings and'
                f' pepperoni_toppings and'
                f'ham_toppings : '
            ).split(' ')
            return cls(size, int(cheese_toppings), int(pepperoni_toppings), int(ham_toppings))
            # print(size, cheese_toppings, pepperoni_toppings, ham_toppings)
        except Exception as e:
            print(e, 'please again ')
            cls.prompt()

    def set_size(self, size):
        if size in PRICE['size']:
            self.__size = size
        else:
            print(f'Please select only the following options {PRICE["size"]}')
            self.prompt()

    def get_size(self):
        return self.__size

    def set_cheese_toppings(self, cheese_toppings):
        if 0 <= cheese_toppings <= 100:
            self.__cheese_toppings = cheese_toppings
        else:
            print('You can choose between 0 and 100 cheese please again')
            self.prompt()

    def get_cheese_toppings(self):
        return self.__cheese_toppings

    def set_pepperoni_toppings(self, pepperoni_toppings):
        if 0 <= pepperoni_toppings <= 100:
            self.__pepperoni_toppings = pepperoni_toppings
        else:
            print(f'You can choose between 0 and 100 pepperoni please again')
            self.prompt()

    def get_pepperoni_toppings(self):
        return self.__pepperoni_toppings

    def set_ham_toppings(self, ham_toppings):
        if 0 <= ham_toppings <= 100:
            self.__ham_toppings = ham_toppings
        else:
            print(f'You can choose between 0 and 100 ham please again')
            self.prompt()

    def get_ham_toppings(self):
        return self.__ham_toppings

    def calculate_the_cost(self):
        sums = PRICE['size'][self.get_size()] + ((PRICE['food']['cheese'] * self.get_cheese_toppings()) +
                                                 (PRICE['food']['pepperoni'] * self.get_pepperoni_toppings()) +
                                                 (PRICE['food']['ham'] * self.get_ham_toppings()))
        return sums

    def get_info(self):
        print(f"""
        size : {self.get_size()},
        cheese : {self.__cheese_toppings},
        ham : {self.__ham_toppings},
        pepperoni : {self.__pepperoni_toppings},
        """)


order_numbers = int(input('Please enter the order number'))
# order_numbers = int(input())
order_list = list(i for i in range(order_numbers))

for num in range(len(order_list)):
    order_list[num] = Pizza.prompt()

for num in range(len(order_list)):
    print(f'price is {order_list[num].calculate_the_cost()}')
    # print(order_list[num].calculate_the_cost())
