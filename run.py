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

user_data = []
order_data = []


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
    user = UserOrder()
    user_name = input("Enter your name: ")
    # order_id = uuid.uuid1()
    # print(order_id)
    user_order_id = random.getrandbits(16)
    print(user_order_id)
    print(colored(f"\nWelcome {user_name}!\n", 'cyan'))
    while True:
        delivery_type = input(
            "Order type:\nEnter D for Home delivery\nEnter P for Pickup: "
        )
        if delivery_type.capitalize() == "D":
            order_type = "Home delivery"
            print(colored(
                f"\nYour selected delivery type is: {order_type}\n", 'cyan'))
            address = input("Enter your Full Address: ")
            print(colored(f"\nYour provided address: {address}\n", 'cyan'))
            print(colored("\nLoading menu...", 'green'))
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        elif delivery_type.capitalize() == "P":
            order_type = "Pickup"
            print(colored(
                f"\nYour selected delivery type is: {order_type}", 'cyan'))
            user_data.append("The Pizza Hub")
            print(colored("\nLoading menu...", 'green'))
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        else:
            print(colored("\nInvalid delivery type. Try again.\n", 'red'))


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
    order_item = UserOrder.add_item(self, item_number)
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice.isdigit() is True:
            if (int(user_choice) >= 1) and (int(user_choice) <= MAX_MENU_ITEM):
                item_number = int(user_choice)
                order_items.add_item(item_number)
                order_items.complete()
                print(order_items.items)
                print("Which other item would you like to add in your order?\n")
            else:
                print(colored("\nEntered item does not exists.", 'red'))
        elif user_choice.capitalize() == "P":
            print(colored("Loading preview page....", 'green'))
            sleep(2)
            clear_screen()
            break
        elif user_choice.capitalize() == "Q":
            print(colored("Back to home page...", 'green'))
            sleep(2)
            clear_screen()
            welcome()
            break
        else:
            print(colored("Invalid input.\n", 'red'))


class UserOrder:
    """
    Class that creates the user order instance
    """
    def __init__(self, user_name, order_type, address, user_id, food_item):
        """
        Class to create user instance
        """
        # instance attribute
        # self.user_name = None
        # self.id = None
        # self.order_type = None
        # self.address = None
        # # self.items = list()
        self.food_items = []
        self.user_name = user_name
        self.order_type = order_type
        self.address = address
        self.user_id = user_id
        

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
        self.food_item.append(item_number)

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
        for item in self.food_item:
            rows.append([self.id, self.user_name, self.address, self.order_type, food_item])
            print(rows)
        ORDER_LIST.append_row(rows[0])
        print(rows)

    # def _fetch_order(self):
    #     # Go to sheet

    # def preview_order(self):
    #     order_template = """
    #     Order ID: %s
    #     User Name: %s
    #     Order Type: %s
    #     Address: %s
    #     ----------------------------------------------
    #     Item Name   Item Price
    #     """
    #     item_teplate = """
    #     %s  %s
    #     """
    #     order_receipt = order_template % (self.id, self.user_name, self.order_type, self.address)
    #     total_price = 0
    #     for item in self.items:
    #         item_details = MENU.get(item)
    #         item_price = item_details[2]
    #         total_price += item_price
    #         order_receipt+=item_teplate % (item_details[1], item_details[2])

        # order_receipt += "Total price: %s" % total_price

    #     print(order_receipt)


def welcome():
    """
    Function to display home page
    """
    print(colored("Welcome to Pizza Hub!\n", 'green'))
    while True:
        start_order = input("To order now, enter Y: ")
        print(start_order)
        if start_order.capitalize() == "Y":
            clear_screen()
            get_user_details()
            break
        else:
            print(colored("Invalid input. Enter Y to start your order.\n", 'red'))


if __name__ == "__main__":
    welcome()
