"""
Import gspread, to access and update data in our spreadsheet and
import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
"""
import os
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pizza_hub')

MENU = SHEET.worksheet('menu')
ORDER = SHEET.worksheet('order')
RECEIPT = SHEET.worksheet('receipt')
MAX_MENU_ITEM = 15


def clear_screen():
    """
    Function to clear screen
    """
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def welcome():
    """
    Function to display home page
    """
    print("Welcome to Pizza Hub!\n")
    while True:
        start_order = input("To order now, enter Y: ")
        print(start_order)
        if start_order == 'y' or start_order == 'Y':
            clear_screen()
            get_user_details()
            break
        else:
            print("Invalid input. Enter Y to order.\n")


def get_user_details():
    """
    Function to get user name and their type of order
    """
    input("Enter your name: ")
    while True:
        order_type = input("Order type:\n For Home delivery, enter D and For Pickup, enter P: ")
        if order_type == 'D' or order_type == 'd':
            print("Your selected delivery type is: Home delivery\n")
            address = input("Enter your Full Address: ")
            print(f"Your provided address: {address}")
            print("Loading menu...")
            sleep(5)
            clear_screen()
            display_menu_list()
            break
        elif order_type == 'P' or order_type == 'p':
            print("Your selected delivery type is: Pickup")
            print("Loading menu...")
            sleep(5)
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
    show_menu = MENU.get_all_values()
    formatted_menu = (tabulate(show_menu))
    print(formatted_menu)
    print("\nEnter Item number to add item to order list.")
    print("Enter P to preview your order")
    print("Enter Q to quit\n")
    user_action()


def user_action():
    """
    Function to display user action after getting the menu
    """
    # while True:
    #     user_choice = input("Enter your choice: ")
    #     if user_choice == 'q' or user_choice == 'Q':
    #         print("Back to home page...")
    #         sleep(2)
    #         clear_screen()
    #         welcome()
    #         break 
    #     elif user_choice == 'p' or user_choice == 'P':
    #         print("Loading preview page....")
    #         sleep(2)
    #         clear_screen()
    #         preview_order_list()
    #         break
        # else:
        #     print("Invalid input")
        
    while True:
        user_choice = input("Enter your choice: ")
        if (int(user_choice) >= 1) and (int(user_choice) <= MAX_MENU_ITEM):
            cell = MENU.find(user_choice)
            added_item = MENU.get('B' + str(cell.row))
            cost_item = MENU.get('C' + str(cell.row))
            print(f"\nYou added: {added_item[0][0]}, price:{cost_item[0][0]}\n")
            print("Which other item would you like to add in your order?\n")
            break
        else:
            print("Invalid input. Try again.")


def preview_order_list():
    """
    Function to display formatted order list of user's selected item
    """


user_action()
# welcome()