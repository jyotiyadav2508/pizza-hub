"""
Import gspread, to access and update data in our spreadsheet and
import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
"""
import os
from time import sleep
# import uuid
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
RECEIPT_LIST = SHEET.worksheet("receipt")
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
    print(colored("Welcome to Pizza Hub!\n", 'green'))
    while True:
        start_order = input("\nTo order now, enter Y: ")
        print(start_order)
        if start_order.capitalize() == "Y":
            clear_screen()
            get_user_details()
            break
        else:
            print("Invalid input. Enter Y to order.\n")


def get_user_details():
    """
    Function to get user name and their type of order
    """
    user_data.clear()
    user_name = input("Enter your name: ")
    user_data.append(user_name)
    print(f"Welcome {user_name}!\n")
    # order_id = ORDER_ID
    # order_id += 1
    # print(order_id)
    # user_data.append(order_id)
    print(user_data)
    while True:
        delivery_type = input(
            "Order type:\nEnter D for Home delivery\nEnter P for Pickup: "
        )
        if delivery_type.capitalize() == "D":
            order_type = "Home delivery"
            user_data.append(order_type)
            print(f"Your selected delivery type is: {order_type}\n")
            address = input("Enter your Full Address: ")
            print(f"Your provided address: {address}")
            user_data.append(address)
            print(user_data)
            print("Loading menu...")
            sleep(1)
            clear_screen()
            display_menu_list()
            break
        elif delivery_type.capitalize() == "P":
            order_type = "Pickup"
            user_data.append(order_type)
            print(user_data)
            print(f"Your selected delivery type is: {order_type}")
            print("Loading menu...")
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        else:
            print("Invalid delivery type. Try again.")


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
    heading = MENU.get('A1:D2')
    print(heading)
    ORDER_LIST.append_row(heading[0])
    ORDER_LIST.append_row(heading[1])
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice.isdigit() is True:
            if (int(user_choice) >= 1) and (int(user_choice) <= MAX_MENU_ITEM):
                item_number = int(user_choice)

                add_item(item_number)
                print(order_data)
                print("Which other item would you like to add in your order?\n")
            else:
                print("\nInvalid input. Try again")
        elif user_choice.capitalize() == "P":
            print("Loading preview page....")
            sleep(1)
            clear_screen()
            preview_order()
            break
        elif user_choice.capitalize() == "Q":
            print("Back to home page...")
            sleep(1)
            clear_screen()
            welcome()
            break
        else:
            print("Invalid input.\n")


def add_item(item_number):
    """
    Function to append user's order list on order list sheet
    """
    cell = MENU.find(str(item_number))
    order_row = MENU.row_values(cell.row)
    row = order_row
    print(row)
    ORDER_LIST.append_row(row)


def preview_order():
    """
    Function to preview the user's order
    """
    user_order = ORDER_LIST.get_all_values()
    print("------Order Preview------\n")
    formatted_preview = tabulate(user_order)
    print(formatted_preview)
    print("\nTo remove an item, enter Item number\n")
    print("To add an item, enter A\n")
    print("To confirm order, enter C\n")
    print("To quit, enter Q\n")
    while True:
        preview_choice = input("Enter your choice: ")
        if preview_choice.isdigit() is True:
            if (int(preview_choice) >= 1 and int(preview_choice) <= MAX_MENU_ITEM):
                cell = ORDER_LIST.find(preview_choice)
                print(cell)
                if cell is not None:
                    # ORDER_LIST.batch_clear(["A" + str(cell.row) + ":" + "C" + str(cell.row)])
                    ORDER_LIST.delete_rows(cell.row)
                    print("Requested item removed!")
                    sleep(1)
                    clear_screen()
                    preview_order()
                else:
                    print("Item does not exist in the list")
            else:
                print("Invalid input")
        elif preview_choice.capitalize() == 'A':
            print("Loading menu page....")
            sleep(1)
            clear_screen()
            display_menu_list()
            break
        elif preview_choice.capitalize() == 'C':
            print("Loading reciept....")
            sleep(1)
            clear_screen()
            display_order_receipt()
            break
        elif preview_choice.capitalize() == 'Q':
            print("Loading home page....")
            ORDER_LIST.clear()
            sleep(1)
            clear_screen()
            welcome()
            break
        else:
            print("Invalid input")


def display_order_receipt():
    """
    Functon to display receipt with user datails and order list
    """
    print(f"User name: {user_data[0]}")
    # print(f"Order Id: {user_data[1]}")
    print(f"Order type: {user_data[1]}")
    if user_data[1] == "Home delivery":
        print(f"Address: {user_data[2]}")
    else:
        print("Address: The Pizza Hub")
    receipt = ORDER_LIST.get_all_values()
    price = ORDER_LIST.col_values(3)
    price.remove("Cost")
    price.remove("--------------------")
    total_price = 0
    for item in price:
        price = float(item.split("€")[1])
        total_price += price
        display_total_price = "€" + str(round(total_price, 2))
    print(tabulate(receipt, tablefmt="simple", numalign="center"))
    print(f"\nTotal price of your order: {display_total_price}\n")
    ORDER_LIST.clear()
    user_input = input("To quit, enter Q: ")
    if user_input.capitalize() == 'Q':
        ORDER_LIST.clear()
        clear_screen()
        welcome()


if __name__ == "__main__":
    welcome()
