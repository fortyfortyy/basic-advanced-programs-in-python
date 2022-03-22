import asyncio

from inventory import Inventory
from order import Order


def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n--------- Sides -----------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n--------- Drinks -----------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")


async def get_order(inventory, num_items):
    order = Order(inventory)
    tasks = []

    print('Please enter the number of items that you would like to add to your order. Enter q to complete your order.')
    while True:
        item_id = input('Enter an item number: ')
        if item_id == 'q':
            break

        if not item_id.isdigit():
            print("Please enter a valid number.")
            continue

        item_id = int(item_id)
        if item_id > num_items or item_id < 1:
            print(f'Please enter a number below {num_items + 1}.')
            continue

        add_to_order_task = asyncio.create_task(order.add_item(item_id))
        tasks.append(add_to_order_task)

    if item_id != 'q':
        print('Placing order...')

    for task in tasks:
        # if the task returns false we can not add the item to the order becaouse it's out of stock
        in_stock, item_id = await task

        if not in_stock:
            print(
                f"Unfortunately item number {item_id} is out of stock and has been removed from your order. Sorry!"
            )

    return order


def get_summary(order, sub_total, tax, total):
    print('\nHere is a summary of your order:\n')
    print(order)
    print(f"\nSubtotal: ${round(sub_total, 2)}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total}")


def purchase_order(total):
    answer = input(f"Would you like to purchase this order for ${round(total, 2)} (yes/no)? ").lower()

    if answer not in ['y', 'yes']:
        print('No problem, please come again!')
        return False

    print('Thank you for your order!')
    return True


async def main():
    print('Welcome to the Programming Burger Bar!')
    inventory = Inventory()

    print('Loading catalogue...')
    num_items, catalogue = await asyncio.gather(inventory.get_number_of_items(), inventory.get_catalogue())
    display_catalogue(catalogue)

    while True:
        order = await get_order(inventory, num_items)

        sub_total = order.get_price()
        if sub_total != 0:
            tax = round(sub_total * 0.05, 2)
            total = round(sub_total + tax, 2)

            get_summary(order, sub_total, tax, total)
            purchase = purchase_order(total)
            if purchase:
                order_again = input(
                    "Would you like to make another order (yes/no)? ").lower()
                if order_again not in ['y', 'yes']:
                    break
        else:
            break

        print()

    print('Goodbye!')


if __name__ == "__main__":
    asyncio.run(main())
