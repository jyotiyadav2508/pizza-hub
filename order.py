
# from time import sleep
# import gspread
# from tabulate import tabulate


# class UserOrder:
#     """
#     Class that creates user order instance
#     """
#     def __init__(self, user_name, item_num, item_name, price, order_type, address):
#         # instance attribute
#         self.user_name = user_name
#         self.item_num = item_num
#         self.item_name = item_name
#         self.price = price
#         self.order_type = order_type
#         self.address = address
    
#     def append_order_data(self):
#         """
#         Function to update user data in order worksheet
#         """
#         order_data = [self.user_name, self.item_num, self.item_name, self.price, self.order_type, self.address]
#         update_worksheet = SHEET.worksheet('order')
#         update_worksheet.append_row(order_data)
#         formatted_order_data = (tabulate(update_worksheet))
#         print(formatted_order_data)