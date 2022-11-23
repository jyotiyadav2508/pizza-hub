"""
Import gspread, to access and update data in our spreadsheet and
import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
"""
import os
from time import sleep
from datetime import datetime, timedelta
# import uuid
import random
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from termcolor import colored


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


def welcome():
    """
    Function to display home page
    """
    # words = "Welcome to Pizza Hub!\n"
    # for char in words:
    #     sleep(0.1)
    #     print(char, end='', flush=True)
    print(colored("Welcome to Pizza Hub!\n", 'yellow'))
    while True:
        start_order = input("\nTo order now, Please enter Y: ")
        print(start_order)
        if start_order.capitalize() == "Y":
            clear_screen()
            get_user_details()
            break
        else:
            print(colored(
                "Invalid input. Enter Y to start your order.\n", 'red'))


def get_user_details():
    """
    Function to get user name and their type of order
    """
    user_data.clear()
    user_name = input("Enter your name: ")
    # order_id = uuid.uuid1()
    # print(order_id)
    user_order_id = random.getrandbits(16)
    user_data.append(user_name)
    user_data.append(user_order_id)
    print(colored(f"\nWelcome {user_name}!\n", 'cyan'))
    while True:
        delivery_type = input(
            "Order type:\nEnter D for Home delivery\nEnter P for Pickup: "
        )
        if delivery_type.capitalize() == "D":
            order_type = "Home delivery"
            user_data.append(order_type)
            print(colored(
                f"\nYour selected delivery type is: {order_type}\n", 'cyan'))
            address = input("Enter your Full Address: ")
            print(colored(f"\nYour provided address: {address}\n", 'cyan'))
            user_data.append(address)
            print(colored("\nLoading menu...", 'green'))
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        elif delivery_type.capitalize() == "P":
            order_type = "Pickup"
            user_data.append(order_type)
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
    order_data.clear()
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice.isdigit() is True:
            if (int(user_choice) >= 1) and (int(user_choice) <= MAX_MENU_ITEM):
                item_number = int(user_choice)
                add_item(item_number)
                print(colored(
                    '\nWhich other item would you like to add'
                    ' in your order?\n', 'yellow'))
            else:
                print(colored("\nInvalid input. Try again\n", 'red'))
        elif user_choice.capitalize() == "P":
            print(colored("\nLoading preview page....", 'green'))
            sleep(2)
            clear_screen()
            preview_order()
            break
        elif user_choice.capitalize() == "Q":
            print(colored("\nBack to home page...", 'green'))
            sleep(1)
            clear_screen()
            welcome()
            break
        else:
            print(colored("\nInvalid input.\n", 'red'))


def add_item(item_number):
    """
    Function to append user's order list on order list sheet
    """
    cell = MENU.find(str(item_number))
    order_row = MENU.row_values(cell.row)
    row = order_row
    ORDER_LIST.append_row(row)


def preview_order():
    """
    Function to preview the user's order
    """
    user_order = ORDER_LIST.get_all_values()
    print(colored("------Order Preview------\n", 'cyan'))
    formatted_preview = tabulate(user_order, headers=[
        "Item", "Name", "Price"], tablefmt="simple", numalign="center")
    print(formatted_preview)
    print("\n\nTo remove an item, enter Item number\n")
    print("To add an item, enter A\n")
    print("To confirm order, enter C\n")
    print("To quit, enter Q\n")
    while True:
        preview_choice = input("Enter your choice: ")
        if preview_choice.isdigit() is True:
            if (int(preview_choice) >= 1 and int(preview_choice) <= MAX_MENU_ITEM):
                cell = ORDER_LIST.find(preview_choice)
                if cell is not None:
                    ORDER_LIST.delete_rows(cell.row)
                    print(colored("\nRequested item removed!", 'green'))
                    sleep(2)
                    clear_screen()
                    preview_order()
                else:
                    print(colored("\nItem does not exist in the list", 'red'))
            else:
                print(colored("\nInvalid input\n", 'red'))
        elif preview_choice.capitalize() == 'A':
            print(colored("\nLoading menu page....", 'green'))
            sleep(1)
            clear_screen()
            display_menu_list()
            break
        elif preview_choice.capitalize() == 'C':
            print(colored("\nLoading reciept....", 'green'))
            sleep(1)
            clear_screen()
            display_order_receipt()
            break
        elif preview_choice.capitalize() == 'Q':
            print(colored("\nLoading home page....", 'green'))
            ORDER_LIST.clear()
            sleep(1)
            clear_screen()
            welcome()
            break
        else:
            print(colored("\nInvalid input\n", 'red'))


def display_order_receipt():
    """
    Functon to display receipt with user datails and order list
    """
    print(colored("****Your Reciept****\n", 'yellow'))
    print(f"User name: {user_data[0]}")
    print(f"Order Id: {user_data[1]}")
    print(f"Order type: {user_data[2]}")
    print(f"Address: {user_data[3]}")
    order_time = datetime.now() + timedelta(hours=1)
    delivery_time = order_time + timedelta(minutes=30)
    pickup_time = order_time + timedelta(minutes=15)
    order_time = order_time.strftime("%d-%m-%Y  %H:%M:%S")
    delivery_time = delivery_time.strftime("%d-%m-%Y  %H:%M:%S")
    pickup_time = pickup_time.strftime("%d-%m-%Y  %H:%M:%S")

    print(f"Order time: {order_time}")
    if user_data[2] == "Home delivery":
        print(f"Delivery time: {delivery_time}\n")
    else:
        print(f"Pickup time: {pickup_time}\n")
    receipt = ORDER_LIST.get_all_values()
    price = ORDER_LIST.col_values(3)
    total_price = 0
    # delivery_charge = 5
    for item in price:
        price = float(item.split("€")[1])
        total_price += price
        display_total_price = "€" + str(round(total_price, 2))
    print(tabulate(receipt, headers=[
        "Item", "Name", "Price"], tablefmt="simple", numalign="center"))
    # if user_data[2] == "Home delivery":
    #     print(colored(
    #         f'\nThere is a delivey charge of €{float(delivery_charge):.2f}'))
    #     display_total_price = display_total_price + str(round(delivery_charge, 2))
    #     print(colored(
    #         f"\nTotal price of your order: {display_total_price}\n", 'yellow'))
    # else:
    print(colored(
            f"\nTotal price of your order: {display_total_price}\n", 'yellow'))
    print(colored("Thanks for your order. Enjoy your meal!\n", 'yellow'))
    # receipt_data = []
    # receipt_data.append(user_data)
    # receipt_data.append(receipt)
    # print(receipt)
    # print(receipt_data)
    i = 0
    while i < len(receipt):
        for item in receipt:
            receipt_data = []
            # user_data.append(item)
            # print(user_data)
            receipt_data = user_data + item
            RECEIPT_LIST.append_row(receipt_data)
            i += 1
    ORDER_LIST.clear()
    user_input = input("To quit, enter Q: ")
    if user_input.capitalize() == 'Q':
        ORDER_LIST.clear()
        clear_screen()
        welcome()


if __name__ == "__main__":
    welcome()