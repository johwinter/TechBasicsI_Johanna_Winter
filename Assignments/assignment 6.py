"""
Assignment 6: Inventory Management Game
Scenario: We are at the supermarket with a shopping list of 5 items.
The basket only holds 5 items at a time, so we have to find everything on the list
and the goal is to head to the checkout to win.
"""

# CONSTANTS
MAX_INVENTORY_SIZE = 5

SHOPPING_LIST = ["bread", "milk", "eggs", "apple", "chocolate"]


# Game State
inventory = []

items_in_room = [
    {"name": "bread", "type": "food"},
    {"name": "milk", "type": "food"},
    {"name": "eggs", "type": "food"},
    {"name": "apple", "type": "food"},
    {"name": "chocolate", "type": "food"},
    {"name": "chips", "type": "food"},        # not on the list
    {"name": "soap", "type": "hygiene"},      # not on the list
    {"name": "magazine", "type": "readable"},  # not on the list
]

item_descriptions = {
    "bread": "A fresh loaf of bread. Smells great.",
    "milk": "A carton of whole milk.",
    "eggs": "A dozen eggs. Handle with care.",
    "apple": "A shiny red apple.",
    "chocolate": "A bar of dark chocolate. Tempting.",
    "chips": "A bag of salty chips. Not on your list.",
    "soap": "A bar of soap. Not on your list.",
    "magazine": "A gossip magazine. Not on your list.",
}
# HELPER FUNCTION
def find_item(items_list, item_name):
    """Searches a list of item-dictionaries for a matching name.
    Returns the item dictionary if found, otherwise None."""
    for item in items_list:
        if item["name"].lower() == item_name.lower():
            return item
    return None

# CORE ACTIONS
def show_room_items():
    """Prints all items currently on the shelf."""
    if not items_in_room:
        print("The shelf is empty.")
    else:
        print("Items on the shelf:")
        for item in items_in_room:
            print(f"  - {item['name']} ({item['type']})")


def pick_up(item_name):
    """Moves an item from the shelf into the basket, if possible."""
    item = find_item(items_in_room, item_name)

    if item is None:
        print(f"There is no '{item_name}' on the shelf.")
        return

    if len(inventory) >= MAX_INVENTORY_SIZE:
        print(f"Your basket is full ({MAX_INVENTORY_SIZE} items max). Drop something first.")
        return

    inventory.append(item)
    items_in_room.remove(item)
    print(f"You put {item['name']} in your basket.")


def drop(item_name):
    """Moves an item from the basket back onto the shelf."""
    item = find_item(inventory, item_name)

    if item is None:
        print(f"You don't have '{item_name}' in your basket.")
        return

    inventory.remove(item)
    items_in_room.append(item)
    print(f"You put {item['name']} back on the shelf.")


def show_inventory():
    """Prints the current contents of the basket."""
    print(f"Basket ({len(inventory)}/{MAX_INVENTORY_SIZE}):")
    if not inventory:
        print("  (empty)")
    else:
        for item in inventory:
            print(f"  - {item['name']} ({item['type']})")


def examine(item_name):
    """Prints a description of an item, whether on the shelf or in the basket."""
    item = find_item(inventory, item_name) or find_item(items_in_room, item_name)

    if item is None:
        print(f"You don't see any '{item_name}' to examine.")
        return

    description = item_descriptions.get(item["name"].lower(), "It looks unremarkable.")
    print(description)


def use(item_name):
    """Uses (eats/tries) an item from the basket. Eating a shopping-list
    item removes it from your basket, meaning you'll need to buy it again!"""
    item = find_item(inventory, item_name)

    if item is None:
        print(f"You don't have '{item_name}' in your basket to use.")
        return

    if item["type"] == "food":
        inventory.remove(item)
        print(f"You snack on the {item['name']} right there in the aisle. Oops, now it's gone!")
    else:
        print(f"You take a closer look at the {item['name']}, but there's nothing more to do with it.")


def checkout():
    """Checks whether the basket contains everything on the shopping list."""
    missing = [name for name in SHOPPING_LIST if find_item(inventory, name) is None]

    if not missing:
        print("The cashier scans your items... Payment successful!")
        return True
    else:
        print("You can't check out yet. Still missing:")
        for name in missing:
            print(f"  - {name}")
        return False


def show_help():
    """Prints the list of available commands."""
    print("Available commands:")
    print("  look               - show items on the shelf")
    print("  inventory          - show your basket")
    print("  pickup <item>      - put an item in your basket")
    print("  drop <item>        - put an item back on the shelf")
    print("  use <item>         - eat/use an item from your basket")
    print("  examine <item>     - examine an item closely")
    print("  checkout           - try to pay and finish shopping")
    print("  help               - show this help message")
    print("  quit               - exit the game")

# MAIN GAME LOOP
def main():
    print("Welcome to the supermarket!")
    print("Your shopping list: " + ", ".join(SHOPPING_LIST))
    print(f"Your basket holds a maximum of {MAX_INVENTORY_SIZE} items.")
    print("Type 'help' if you need a list of commands.\n")

    while True:
        command_line = input("> ").strip().lower()

        if not command_line:
            continue

        parts = command_line.split(maxsplit=1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        if command == "look":
            show_room_items()
        elif command == "inventory":
            show_inventory()
        elif command == "pickup":
            pick_up(argument)
        elif command == "drop":
            drop(argument)
        elif command == "use":
            use(argument)
        elif command == "examine":
            examine(argument)
        elif command == "checkout":
            if checkout():
                print("\n*** SHOPPING COMPLETE! You bought everything on your list. ***")
                break
        elif command == "help":
            show_help()
        elif command == "quit":
            print("You leave the supermarket empty-handed. Game over.")
            break
        else:
            print("Unknown command. Type 'help' to see what you can do.")


if __name__ == "__main__":
    main()

    # For this assignment I created a small text-based supermarket shopping game.
    # My idea was to give the inventory system a concrete context, where
    # you have a shopping list of 5 items and a basket that can hold a maximum
    # of 5 items, so managing space actually matters. I implemented the required
    # actions (pickup, drop, use, examine, show_inventory, show_room_items) plus
    # an extra checkout() function that checks whether the basket matches the
    # shopping list to decide if the player wins. I used Claude AI to help me
    # plan the structure and to test different scenarios
    # (like a full basket or a missing item at checkout) to make sure the game
    # behaves correctly in edge cases.
