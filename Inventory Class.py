class Inventory:
    """
    Simple program that handles the management of inventory for a company.
    """
    def __init__(self, max_capacity):
        self.items_capacity = 0
        self.max_capacity = max_capacity
        self.items = {}

    def add_item(self, name, price, quantity):
        if name in self.items:
            return False

        if quantity + self.items_capacity > self.max_capacity:
            return False

        self.items[name] = {'name': name, 'price': price, 'quantity': quantity}
        self.items_capacity += quantity
        return True

    def delete_item(self, name):
        if name in self.items:
            self.items_capacity -= self.items[name]['quantity']
            del self.items[name]
            return True

        return False

    def get_items_in_price_range(self, min_price, max_price):
        items = list(filter(lambda item: min_price <= self.items[item]['price'] <= max_price, self.items))
        return items

    def get_most_stocked_item(self):
        if len(self.items) < 1:
            return None
        items = sorted(self.items, key=lambda item: self.items[item]['quantity'])
        return items[::-1][0]


i = Inventory(4)
i.add_item('Chocolate', 4.99, 1)
i.delete_item('Chocolate')
i.delete_item('Chocolate')
i.delete_item('Bread')
i.add_item('Chocolate', 4.99, 2)
i.add_item('Bread', 4.99, 2)
a = i.get_most_stocked_item()
print(a)