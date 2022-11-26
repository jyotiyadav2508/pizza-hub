"""
Import gspread, to access and update data in our spreadsheet and
import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
"""
import os
from time import sleep
from datetime import datetime, timedelta
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
MAX_MENU_ITEM = len(MENU.get_all_values())

user_data = []
order_data = []
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
Item number] - To remove an item
[A] - To add an item
[C] - To confirm order
[Q] - To quit
"""


def clear_screen():
    """
    Clear the current open screen
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def get_user_details():
    """
    Get user name and order type
    """
    user_data.clear()
    user_name = input("Enter your name: ")
    user_order_id = random.getrandbits(16)
    user_data.append(user_name)
    user_data.append(user_order_id)
    order_data.append(user_order_id)
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
                colored(
                    f"Your selected delivery type is: {order_type}\n", "yellow"
                )
            )
            address = input("Enter your Address: ")
            print(colored(f"\nYour provided address is {address}\n", "yellow"))
            user_data.append(address)
        elif delivery_type == "P":
            order_type = "Pickup"
            user_data.append(order_type)
            print(
                colored(
                    f"\nYour selected delivery type is: {order_type}", "yellow"
                )
            )
            user_data.append("The Pizza Hub")

        print(colored("\nLoading menu...", "green"))
        sleep(2)
        clear_screen()
        display_menu_list()
        break


def display_menu_list():
    """
    Fetches pizza menu from google spreadsheet and display it
    in formatted tabulate form to user.
    """
    display_menu = MENU.get_all_values()
    # formatted_menu = tabulate(display_menu)
    # print(formatted_menu)
    print(tabulate(display_menu))
    print(DISPLAY_MENU_MSG)
    user_action()


def user_action():
    """
    Displays user action after getting the menu.
    """
    item_number = 0
    # order_data.clear()
    while True:
        # item_number = 0
        user_choice = input("Enter your choice: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >= 1 and user_choice <= len(MENU.get_all_values()):
                item_number = user_choice
                add_item(item_number)
                print(
                    colored(
                        "\nSelected item saved in your order list", "yellow"
                    )
                )
            else:
                print(colored("\nItem doesn't exist in the menu.\n", "red"))
        elif user_choice.capitalize() == "P":
            if item_number == 0:
                print(
                    colored("Your list is empty. Please add items.\n", "yellow")
                )

            else:
                print(colored("\nLoading preview page....", "green"))
                sleep(2)
                clear_screen()
                preview_order()
                break
        elif user_choice.capitalize() == "Q":
            print(colored("\nThanks for visiting us\n", "yellow"))
            sleep(2)
            clear_screen()
            break
        else:
            print(colored("\nInvalid input.\n", "red"))


def add_item(item_number):
    """
    Append user's order in google spreed sheet
    """
    cell = MENU.find(str(item_number))
    order_row = user_data + MENU.row_values(cell.row) + ["Processing"]
    # order_row.append(order_data[0])
    # ORDER_LIST.append_row(user_data)
    ORDER_LIST.append_row(order_row)
    # print(order_row)


def preview_order():
    """
    Preview user's order list
    """
    local_user_data = get_individual_user_data()
    # for row in ORDER_LIST.get_all_values():
    #     for item in row:
    #         if item == str(order_data[0]):
    #             row.pop(7)
    #             del row[0:4]

    #             individual_user_data.append(row)
    #     print(individual_user_data)
    #     tabulate_preview(individual_user_data)
    i = True
    while True:
        # for row in ORDER_LIST.get_all_values():
        #     for item in row:
        #         if item == str(order_data[0]):
        #             row.pop(7)
        #             del row[0:4]

        #             individual_user_data.append(row)
        # print(individual_user_data)
        # tabulate_preview(individual_user_data)
        # print(colored("------Order Preview------\n", "cyan"))
        # formatted_preview = tabulate(
        #     individual_user_data,
        #     headers=["Item", "Name", "Price"],
        #     tablefmt="simple",
        #     numalign="center"
        # )
        if i:
            tabulate_preview(local_user_data)
            print(PREVIEW_TEXT)
            i = False
        # clear_screen()

        preview_option = input("Enter your choice: ")
        if preview_option.isdigit():
            preview_option = int(preview_option)
            if (preview_option) >= 1 and (preview_option) <= len(
                MENU.get_all_values()
            ):
                remove_item(preview_option)
                local_user_data = get_individual_user_data()
                clear_screen()
                tabulate_preview(local_user_data)
                print(PREVIEW_TEXT)
                # cell = ORDER_LIST.find(str(preview_option))
                # if cell is not None:
                #     ORDER_LIST.delete_rows(cell.row)
                #     print(colored("\nRequested item removed!", "green"))
                #     sleep(2)
                #     clear_screen()
                # else:
                #     print(colored("\nItem does not exist in the list", "red"))
            else:
                print(colored("\nInvalid item number\n", "red"))
        elif preview_option.capitalize() == "A":
            print(colored("\nLoading menu page....", "green"))
            sleep(2)
            clear_screen()
            display_menu_list()
            break
        elif preview_option.capitalize() == "C":
            append_order_confirmation()
            print(colored("\nLoading reciept....", "green"))
            sleep(2)
            clear_screen()
            display_order_receipt()
            break
        elif preview_option.capitalize() == "Q":
            print(colored("\nThanks for visiting us!", "green"))
            sleep(2)
            clear_screen()
            break
        else:
            print(colored("\nInvalid input\n", "red"))


def remove_item(item):
    cell = ORDER_LIST.find(str(item))
    if cell is not None:
        ORDER_LIST.delete_rows(cell.row)
        print(colored("\nRemoving requested item...", "green"))
        sleep(2)
        clear_screen()
        # preview_order()
    else:
        print(colored("\nItem does not exist in the list", "red"))
        sleep(2)


def tabulate_preview(user_info):
    print(colored("------Order Preview------\n", "cyan"))
    formatted_preview = tabulate(
        user_info,
        headers=["Item", "Name", "Price"],
        tablefmt="simple",
        numalign="center",
    )
    print(formatted_preview)


def get_individual_user_data():
    individual_user_data = []
    for row in ORDER_LIST.get_all_values():
        for item in row:
            if item == str(order_data[0]):
                row.pop(7)
                del row[0:4]
                # print(row)
                individual_user_data.append(row)
        # tabulate_preview(individual_user_data)
    return individual_user_data


def append_order_confirmation():
    """
    Function
    """
    cells_list = ORDER_LIST.findall(str(order_data[0]))
    # print(cells_list)
    for cell in cells_list:
        # print(cell)
        confirmation_cell = "H" + str(cell.row)
        ORDER_LIST.update(confirmation_cell, "Confirmed")
        # print(confirmation_cell)
        # confirmation_cell.value = 'Confirmed'
    # ORDER_LIST.update_cells(cells_list)

    # i = 0
    # while i < len(ORDER_LIST.get_all_values()):
    #     cell = ORDER_LIST.findall(str(order_data[0]))
    #     if
    #     ORDER_LIST.update_cells(('H' + str(cell.row)), 'Confirmed')
    #     i += 1

    # i = 0
    # while i < len(ORDER_LIST.get_all_values()):
    # for row in ORDER_LIST.get_all_values():
    #     for item in row:
    #         if item == str(order_data[0]):
    #             row[7] = 'Confirmed'
    #     ORDER_LIST.append_row(row)
    # cell = ORDER_LIST.find(str(order_data[0]))
    # ORDER_LIST.update(('H' + str(cell.row)), 'Confirmed')
    # i += 1
    # print(cell)

    # for item in row:

    # # item = item + ["Confirmed"]
    # item.append("Confirmed")
    # print(item)
    # print(individual_user_data)


def display_order_receipt():
    """
    Display receipt with user datails and order list
    """
    print(colored("****Your Reciept****\n", "yellow"))
    print(f"User name: {user_data[0]}")
    print(f"Order Id: {user_data[1]}")
    print(f"Order type: {user_data[2]}")
    print(f"Address: {user_data[3]}")
    order_time = datetime.now()
    delivery_time = order_time + timedelta(minutes=30)
    pickup_time = order_time + timedelta(minutes=15)
    order_time = order_time.strftime("%H:%M:%S  %d-%m-%Y")
    delivery_time = delivery_time.strftime("%H:%M:%S  %d-%m-%Y")
    pickup_time = pickup_time.strftime("%H:%M:%S  %d-%m-%Y")
    print(f"Order time: {order_time}\n")
    # individual_user_receipt = []
    # for row in ORDER_LIST.get_all_values():
    #     for item in row:
    #         if item == str(order_data[0]):
    #             del row[0:4]
    #             individual_user_receipt.append(row)
    #             print(individual_user_receipt)

    # price = ORDER_LIST.col_values(3)
    total_price = 0
    delivery_charge = 5.00
    # print(global_individual_user_data)
    local_user_data = get_individual_user_data()
    for item in local_user_data:
        price = float(item[2].split("€")[1])
        total_price += price
        display_total_price = "€" + str(round(total_price, 2))

    tabulate_preview(local_user_data)
    # print(
    #     tabulate(
    #         local_user_data,
    #         headers=["Item", "Name", "Price"],
    #         tablefmt="simple",
    #         numalign="center"
    #     )
    # )
    # print(display_total_price)
    if user_data[2] == "Home delivery":
        print(f"\nThere is a delivey charge of €{float(delivery_charge):.2f}")
        display_total_price = "€" + str(total_price + delivery_charge)
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
    if user_data[1] == "Home delivery":
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
        end = input("\nEnter Q to quit: ")
        if end.capitalize() == "Q":
            clear_screen()
            print(colored("\nThanks for visiting us\n", "yellow"))
            sleep(2)
            clear_screen()
            break

    # i = 0
    # while i < len(individual_user_data):
    #     for item in individual_user_data:
    #         receipt_data = []
    #         receipt_data = user_data + item
    #         RECEIPT_LIST.append_row(receipt_data)
    #         i += 1
    # j = 0
    # while j < len(ORDER_LIST.get_all_values()):
    #     cell = ORDER_LIST.find(str(order_data[0]))
    #     print(cell)
    #     ORDER_LIST.delete_rows(cell.row)
    #     j += 1

    # ORDER_LIST.clear()
    # user_input = input("To quit, enter Q: ")
    # if user_input.capitalize() == "Q":
    #     ORDER_LIST.clear()
    #     clear_screen()
    #     welcome()


def welcome():
    """
    Function to display home page
    """
    print(colored(WELCOME_MSG, "yellow"))
    while True:
        start_order = input("\nEnter your choice:")
        if start_order.capitalize() == "Y":
            clear_screen()
            get_user_details()
            break
        elif start_order.capitalize() == "N":
            print(colored("\nThanks for visiting us\n", "yellow"))
            sleep(2)
            clear_screen()
            break
        else:
            print(colored("Invalid input. Enter Y to start.\n", "red"))


if __name__ == "__main__":
    welcome()
