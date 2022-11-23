"""
Import gspread, to access and update data in our spreadsheet and
import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
"""
import os
from time import sleep
import uuid
import random
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from termcolor import colored

# import pyfiglet


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pizza_hub")

MENU = SHEET.worksheet("menu")
ORDER_LIST = SHEET.worksheet("order_list")
RECEIPT_LIST = SHEET.worksheet("receipt_lists")
MAX_MENU_ITEM = 15


def clear_screen():
    """
    Function to clear screen
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def get_user_details():
    """
    Function to get user details for required data
    """
    ORDER_LIST.clear()
    user_name = input("Enter your name: ")
    user_name = UserOrder.new(user_name)
    # order_id = uuid.uuid1()
    # print(order_id)
    user_order_id = random.getrandbits(16)
    print(user_order_id)
    print(colored(f"\nWelcome {user_name}!\n", "cyan"))
    while True:
        delivery_type = input(
            "Order type:\nEnter D for Home delivery\nEnter P for Pickup: "
        )
        if delivery_type.capitalize() == "D":
            order_type = "Home delivery"
            print(
                colored(
                    f"\nYour selected delivery type is: {order_type}\n", "cyan"
                )
            )
            address = input("Enter your Full Address: ")
            print(colored(f"\nYour provided address: {address}\n", "cyan"))
            print(colored("\nLoading menu...", "green"))
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        elif delivery_type.capitalize() == "P":
            order_type = "Pickup"
            print(
                colored(
                    f"\nYour selected delivery type is: {order_type}", "cyan"
                )
            )
            print(colored("\nLoading menu...", "green"))
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        else:
            print(colored("\nInvalid delivery type. Try again.\n", "red"))


def display_menu_list():
    """
    Function to fetch data from google spreadsheet and display it
    in formatted tabulate form to user
    """
    display_menu = MENU.get_all_values()
    formatted_menu = tabulate(display_menu)
    print(formatted_menu)
    print("\nEnter Item number to add item to order list.")
    print("Enter P to preview your order")
    print("Enter Q to quit\n")
    user_action()


def user_action():
    """
    Function to display user action after getting the menu
    """
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice.isdigit() is True:
            if (int(user_choice) >= 1) and (int(user_choice) <= MAX_MENU_ITEM):
                item_number = int(user_choice)
                order_items = UserOrder()
                order_items.add_item(item_number)
                order_items.complete()
                print(order_items.food_items)
                print("Which other item would you like to add in your order?\n")
            else:
                print(colored("\nEntered item does not exists.", "red"))
        elif user_choice.capitalize() == "P":
            print(colored("Loading preview page....", "green"))
            sleep(2)
            clear_screen()
            break
        elif user_choice.capitalize() == "Q":
            print(colored("Back to home page...", "green"))
            sleep(2)
            clear_screen()
            welcome()
            break
        else:
            print(colored("Invalid input.\n", "red"))


class UserOrder:
    """
    Class that creates the user order instance
    """

    # def __init__(self, user_name, order_type, address, user_id, food_item):
    def __init__(self):
        """
        Class to create user instance
        """
        # instance attribute
        self.user_name = None
        self.user_id = None
        self.order_type = None
        self.address = None
        self.food_items = list()
        # self.food_items = []
        # self.user_name = user_name
        # self.order_type = order_type
        # self.address = address
        # self.user_id = user_id

    @classmethod
    def new(cls, user_name):
        """
        Class method for new user
        """
        new_order = cls()
        new_order.user_name = user_name
        return new_order

    @classmethod
    def existing(cls, order_id):
        """
        Class method for exixting user
        """
        existing_order = cls()
        existing_order.id = order_id
        self._fetch_order()
        return existing_order

    def add_item(self, item_number):
        """
        Function that add user's selected item in the list food_item
        """
        self.food_items.append(item_number)

    def complete(self):
        """
        Function that generates id
        """
        if self.user_id:
            return

        self.user_id = uuid.uuid1()
        # save info to worksheet
        print(self.user_id)
        rows = []
        # self.food_items = []
        for item in self.food_items:
            rows.append(
                [
                    self.user_id,
                    self.user_name,
                    self.address,
                    self.order_type,
                    food_items,
                ]
            )
        #     print(item)
        # ORDER_LIST.append_row(rows[0])
        # print(rows)

    # def _fetch_order(self):
    # Go to sheet
    # user_order = ORDER_LIST.get_all_values()

    def preview_order(self):
        """
        Function to preview user order
        """
        user_order = ORDER_LIST.get_all_values()
        print(colored("------Order Preview------\n", "cyan"))
        formatted_preview = tabulate(
            user_order,
            headers=["Item", "Name", "Price"],
            tablefmt="simple",
            numalign="center",
        )
        print(formatted_preview)
        # order_receipt = order_template % (self.user_id, self.user_name, self.order_type, self.address)
        total_price = 0
        for item in self.food_items:
            item_details = MENU.get(item)
            item_price = item_details[2]
            total_price += item_price
            # order_receipt+=item_teplate % (item_details[1], item_details[2])

        # order_receipt += "Total price: %s" % total_price

    #     print(order_receipt)


def welcome():
    """
    Function to display home page
    """
    print(colored("Welcome to Pizza Hub!\n", "green"))
    while True:
        start_order = input("To order now, enter Y: ")
        print(start_order)
        if start_order.capitalize() == "Y":
            clear_screen()
            get_user_details()
            break
        else:
            print(
                colored("Invalid input. Enter Y to start your order.\n", "red")
            )
    # Workflow

    # 1. Welcome user
    # 2. Get User details
    # 3. User options - loop
    #   a. Place order
    #   b. Preview order
    #   c. exit

    user_name = input("Enter your name: ")
    order = UserOrder.new(user_name)

    # Place order Workflow
    # 1. Select delivery method
    # 2. Address
    # 3. While user wants to add more items:
    #   a. Show menu
    #   b. Select item
    #   c. Append item to current order
    # 4. Generate order id
    # 5. Update order in Google sheet
    # 6. Share order id/details to user

    order.order_type = "D"
    order.address = "<enterd address>"
    order.add_item(item_number)
    order.complete()
    order.preview_order()

    # Preview order Workflow
    # 1. Ask user for order id
    # 2. Get all rows from sheet against that order id
    # 3. Get all rows corresponding to unique items from menu
    # 4. Compute the final amount and show to user.

    order = UserOrder.existing(order_id)
    order.preview_order()


if __name__ == "__main__":
    welcome()
