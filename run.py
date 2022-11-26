"""
Import gspread to access and update data in our spreadsheet
Import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
Import os to clear screen
Import sleep from time to delay the display of the upcoming data
Import datetime and timedelta to show date and time in the receipt
Import random to generate random order id
Import pyfiglet to display the store name in art form
Import tabulate to display menu, preview and order receipt in
table format
Import colored from termcolor to provide feedback to the user in colored
text format
"""

import os
from time import sleep
from datetime import datetime, timedelta
import random
import gspread
import pyfiglet
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from termcolor import colored


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# To open google sheets after authentication
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pizza_hub")

# To acces the worksheets in google sheets
MENU = SHEET.worksheet("menu")
ORDER_LIST = SHEET.worksheet("order_list")

# Reduce the header and formatting row.
MAX_MENU_ITEM = len(MENU.get_all_values()) - 2

# Order receipt constants
DELIVERY_CHARGE = 5
DELIVERY_TIME = 30
PICKUP_TIME = 15

# Global variables
user_data = []  # Contains user name, user order id, order type and address
order_data = []  # Contains item number, item name, item price
# Contains item number, item name, item price for specific user order id
global_individual_user_data = []

WELCOME_MSG = """
Welcome to The Pizza Hub
Do you want to start your order now?
[Y] - Yes
[N] - No
"""

ORDER_OPTION_MSG = """
Enter your choice for order type -
[D] - For Home delivery
[P] - For Pickup:
"""

DISPLAY_MENU_MSG = """
[Item number] - To add item in your order list.
[P] - To preview your order
[Q] -  To quit
"""

PREVIEW_TEXT = """
[Item number] - To remove an item
[A] - To add an item
[C] - To confirm order
[Q] - To quit
"""


def clear_screen():
    """
    Clears the console
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def tabulate_data(user_info):
    """
    Formats the data in table form
    """
    format_data = tabulate(
        user_info,
        headers=["Item", "Name", "Price"],
        tablefmt="simple",
        numalign="center",
    )
    print(format_data)


def get_individual_user_data():
    """
    Get individual user's order data from worksheet
    'order_list' with unique order Id
    """
    individual_user_data = []
    for row in ORDER_LIST.get_all_values():
        for item in row:
            if item == str(user_data[1]):
                row.pop(7)  # to remove order status
                del row[0:4]  # to remove user data
                individual_user_data.append(row)
    return individual_user_data


def display_order_receipt():
    """
    Displays order receipt with user data, order data,
    order date & time, pickup / delivery date & time,
    delivery charge and total price
    """
    # Display user data
    print(colored("****Your Reciept****\n", "yellow"))
    print(f"User name: {user_data[0]}")
    print(f"Order Id: {user_data[1]}")
    print(f"Order type: {user_data[2]}")
    print(f"Address: {user_data[3]}")
    # Display date & time for order receipt
    order_time = datetime.now()
    delivery_time = order_time + timedelta(minutes=DELIVERY_TIME)
    pickup_time = order_time + timedelta(minutes=PICKUP_TIME)
    order_time = order_time.strftime("%H:%M:%S  %d-%m-%Y")
    delivery_time = delivery_time.strftime("%H:%M:%S  %d-%m-%Y")
    pickup_time = pickup_time.strftime("%H:%M:%S  %d-%m-%Y")
    print(f"Order time: {order_time}\n")
    total_price = 0  # initialize total price
    local_user_data = get_individual_user_data()
    # Calculating total price for order receipt
    for item in local_user_data:
        price = float(item[2].split("€")[1])
        total_price += price
        display_total_price = "€" + str(round(total_price, 2))
    tabulate_data(local_user_data)
    if user_data[2] == "Home delivery":
        print(
            colored(
                f"\nDelivey charge: €{float(DELIVERY_CHARGE):.2f}", "yellow"
            )
        )
        display_total_price = "€" + str(total_price + DELIVERY_CHARGE)
        print(
            colored(
                f"Total price of your order: {display_total_price}", "yellow"
            )
        )
    else:
        print(
            colored(
                f"\nTotal price of your order: {display_total_price}", "yellow"
            )
        )
    if user_data[2] == "Home delivery":
        print(
            colored(
                f"Your order will be delivered at {delivery_time}\n", "yellow"
            )
        )
    else:
        print(
            colored(
                f"Your order will be ready for Pickup at {pickup_time}",
                "yellow",
            )
        )
    print(colored("\nThanks for your order. Enjoy your meal!", "green"))
    while True:
        end = input("\nEnter Q to quit:\n")
        if end.capitalize() == "Q":
            clear_screen()
            print(colored("\nThanks for visiting us!\n", "yellow"))
            sleep(2)
            clear_screen()
            break


def append_order_status(order_request):
    """
    Update order status in worksheet 'order_list'
    when user Confirms / Cancels the order
    """
    cells_list = ORDER_LIST.findall(str(user_data[1]))
    for cell in cells_list:
        # Locating cell for order status corresponding to order id
        confirmation_cell = "H" + str(cell.row)
        if order_request.capitalize() == "C":
            ORDER_LIST.update(confirmation_cell, "Confirmed")
        elif order_request.capitalize() == "Q":
            ORDER_LIST.update(confirmation_cell, "Cancelled")


def remove_item(item):
    """
    Removes an item from user's order list on preview page
    """
    # Find cell of selected item and specific order id in worksheet order list
    item_cell_list = ORDER_LIST.findall(str(item))
    order_id_cell_list = ORDER_LIST.findall(str(user_data[1]))
    # Finding row of the specific order id and store in a list
    order_id_index = []
    for order_id_cell in order_id_cell_list:
        order_id_index.append(order_id_cell.row)
    # Finding row of the specific item and store in a list
    item_index = []
    for item_cell in item_cell_list:
        item_index.append(item_cell.row)
    # Convert both list into set to find common row
    order_id_set = set(order_id_index)
    item_set = set(item_index)
    if order_id_set & item_set:
        remove_row_set = order_id_set & item_set
        remove_row_list = list(remove_row_set)
        # Remove the desired row from worksheet
        for item in remove_row_list:
            ORDER_LIST.delete_rows(item)
            print(colored("\nRemoving requested item...", "green"))
            sleep(2)
            clear_screen()
    else:
        print(colored("\nItem does not exist in the order list", "red"))
        sleep(2)


def preview_order():
    """
    Previews user's order list
    """
    local_user_data = get_individual_user_data()
    i = True
    while True:
        # Tabulate order list when function is called first time
        if i:
            print(colored("------Order Preview------\n", "yellow"))
            tabulate_data(local_user_data)
            print(PREVIEW_TEXT)
            i = False
        preview_option = input("Enter your choice:\n")
        # Evaluating user input for digit and character
        if preview_option.isdigit():
            preview_option = int(preview_option)
            # Validating user input for removing the item
            if (preview_option) >= 1 and (preview_option) <= MAX_MENU_ITEM:
                remove_item(preview_option)
                local_user_data = get_individual_user_data()
                clear_screen()
                tabulate_data(local_user_data)
                print(PREVIEW_TEXT)
            else:
                print(colored("\nInvalid item number\n", "red"))
        elif preview_option.capitalize() == "A":
            print(colored("\nLoading menu page....", "green"))
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        elif preview_option.capitalize() == "C":
            local_user_data = get_individual_user_data()
            # Evaluating order list whether empty or not
            if bool(local_user_data):
                append_order_status(preview_option)
                print(colored("\nLoading reciept....", "green"))
                sleep(2)
                clear_screen()
                display_order_receipt()
                break
            else:
                print(colored("\nNo item in the order list", "red"))
        elif preview_option.capitalize() == "Q":
            append_order_status(preview_option)
            print(colored("\nThanks for visiting us!", "green"))
            sleep(2)
            clear_screen()
            break
        else:
            print(colored("\nInvalid input\n", "red"))


def add_item(item_number):
    """
    Appends user data, order data and order status in google sheets worksheet
    """
    cell = MENU.find(str(item_number))
    order_row = user_data + MENU.row_values(cell.row) + ["Processing"]
    ORDER_LIST.append_row(order_row)


def user_action():
    """
    Displays user action after getting the menu.
    """
    item_number = 0
    while True:
        user_choice = input("Enter your choice:\n")
        # Evalauates whether input is digit or a character
        if user_choice.isdigit():
            user_choice = int(user_choice)
            # Validates and adds the item to the order list
            if user_choice >= 1 and user_choice <= (MAX_MENU_ITEM):
                item_number = user_choice
                add_item(item_number)
                print(
                    colored(
                        "\nSelected item added to your order list", "yellow"
                    )
                )
            else:
                print(
                    colored(
                        "\nSelected item doesn't exist in the menu.\n", "red"
                    )
                )
        elif user_choice.capitalize() == "P":
            # item_number is used to display order list empty message
            # when user enter 'P' without adding an item
            if item_number == 0:
                print(
                    colored(
                        "Order list is empty. Please add an item.\n", "yellow"
                    )
                )
            else:
                print(colored("\nLoading preview page....", "green"))
                sleep(2)
                clear_screen()
                preview_order()
                break
        elif user_choice.capitalize() == "Q":
            append_order_status(user_choice)
            print(colored("\nThanks for visiting us!\n", "yellow"))
            sleep(2)
            clear_screen()
            break
        else:
            print(colored("\nInvalid input.\n", "red"))


def display_menu_list():
    """
    Fetches pizza menu from google sheets worksheet 'menu' and displays it
    in formatted table form to user.
    """
    display_menu = MENU.get_all_values()
    print(tabulate(display_menu))
    print(DISPLAY_MENU_MSG)
    user_action()


def get_user_details():
    """
    Gets user details like user name, order type, address and
    appends them in user data list along with user order Id
    """
    user_data.clear()
    user_name = input("Enter your name:\n")
    user_data.append(user_name)
    # Generates random order id for the specific user
    user_order_id = random.getrandbits(16)
    user_data.append(user_order_id)
    print(colored(f"\nWelcome {user_name}!\n", "yellow"))
    while True:
        delivery_type = input(ORDER_OPTION_MSG).capitalize()
        if delivery_type not in ("D", "P"):
            print(colored("\nInvalid delivery type. Try again.\n", "red"))
            continue

        if delivery_type == "D":
            order_type = "Home delivery"
            user_data.append(order_type)
            print(
                colored(f"Selected delivery type is: {order_type}\n", "yellow")
            )
            address = input("Enter your Address:\n")
            print(colored(f"\nYour provided address is {address}\n", "yellow"))
            user_data.append(address)
        elif delivery_type == "P":
            order_type = "Pickup"
            user_data.append(order_type)
            print(
                colored(f"\nSelected delivery type is: {order_type}", "yellow")
            )
            user_data.append("The Pizza Hub")

        print(colored("\nLoading menu...", "green"))
        sleep(2)
        clear_screen()
        display_menu_list()
        break


def welcome():
    """
    Function to display home page
    """
    title = "The Pizza Hub"
    print(colored(pyfiglet.figlet_format(title), "green"))
    print(colored(WELCOME_MSG, "yellow"))
    while True:
        start_order = input("\nEnter your choice:\n")
        if start_order.capitalize() == "Y":
            clear_screen()
            get_user_details()
            break
        elif start_order.capitalize() == "N":
            print(colored("\nThanks for visiting us!\n", "yellow"))
            sleep(2)
            clear_screen()
            break
        else:
            print(colored("Invalid input. Enter Y to start.\n", "red"))


if __name__ == "__main__":
    welcome()
