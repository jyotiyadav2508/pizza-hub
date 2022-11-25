# The Pizza Hub

Developer: Jyoti Yadav

[View live website](https://the-pizza-hub.herokuapp.com/)

The Pizza Hub website has been developed to provide users the chance to order Pizza for home delivery or pick-up via a command line based interface.

![mockup image]()


## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
    5. [User Manual](#user-manual)    
3. [Technical Design](#technical-design)
    1. [Structure](#structure)
    2. [Flowchart](#flowchart)
    3. [Data Models](#data-modals)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Framework and Tools](#framework-and-tools)
    3. [Libraries](#libraries)
5. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Implementations](#future-implementations)
6.  [Python Valiadation](#python-valiadation) 
7. [Testing](#testing)
    1. [Validator Testing](#validator-testing)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

 - Be able to easily interact with the app to order pizza for pick up or home delivery.
 - Navigate the app seamlessly.
 - Receive clear instructions on their current input options.
 - Be able to add and remove items from an order prior to order confirmation.
 - The ability to preview their order.
 - Be able to quit the app from any page.

### Site Owner Goals

 - To provide customers an easy-to-use app to order pizza from The pizza Hub.
 - To provide home delivery or pickup option to the customers.
 - To provide the customer the ability to preview their orders.
 - To provide the customer to choose order confirmation or quit.
 - To provide the customer to exit any time.
 - Ensure all user inputs are validated and errors are handled to provide a good user experience.

## User Experience

### Target Audience

 - People looking to have pizza ordered for home delivery.
 - People looking to pick up pizza from the store.

### User Requirements and Expectations

 - The ability to seamlessly navigate through the app.
 - To have a well organized menu.
 - To have a easy ordering process.
 - To have validation that inputs have been successfully entered.

### User Stories

#### Site User

1. As a user, I want to be:
    - provided with clear instructions throughout the app.
    - able to choose my order between pick up or home delivery.
    - able to view the menu.
    - able to add items to my order.
    - able to remove items from my order.
    - able to preview an order.
    - able to cancel an unplaced order.
    - able to place an order.
    - able to see an order receipt.
    - able to exit the app.

#### Site Owner

2. As a site owner, I would want:
    - users to be greeted with a welcome message to give a friendly feel to the app.
    - to save the user information and order data to a Google Sheets file.
    - users to get feedback based on their input.

### User Manual
<details><summary>Instructions</summary>

#### Overview

The Pizza Hub app is for users who wish to place orders for home delivery / pickup.

----

#### Home Page

The home page opens with the store name "The Pizza Hub". A welcome page greets the users and asked if they would like to make an order. Users will be provdided with 2 options: Yes and No. Selecting yes will take the user to the main screen while selecting no will exit the app.

----

#### Main Page

The purpose of the main page is to get the user details. Users are asked to provide their name and choice of delivery type. If a home delivery option is selected then home address is also asked.

----

#### Menu page

On the Menu page users are provided with a table format of the menu with the range of items available for order. Users will be provdided with three options.

  - Item number -  To add the item to the order, users will be provided with feedback showing their selected item has been added to the order list and also a warning message if an invalid input has been entered.
  - Q - To cancel order, view thank you message and exit the app.
  - P - To preview the current order.

  ----

#### Preview page

The preview page shows the user's selected order list in a table format. The table shows the item details like item name and price. Also it provides user four options.

  - Item number - To remove any item from the list by entering item number. Invalid input will be warned with a message.
  - A - To add more item, user go back to menu page.
  - C - To confirm the order after preview.
  - Q - To cancel order, view thank you message and exit the app.
  
  ----

#### Receipt page

The receipt page is shown when the user confirms the order. Receipt page displays user's order with their name, unique order ID, order type, address, order time, delivery / pickup time and total price of the order. Quit option is shown along with a thank you message.

----
</details>

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Structure

This app was designed using Code Institutes Python Essentials Template. The template creates a command line interface within a blank page with a run button located above the command line interface. As this project is only intended for use on large screen devices there was no need to incorporate responsiveness to the page. On arrival to the page, the user will be presented with a welcome message and instructions on user input choices.

### Flowchart

The following flowchart was created to help identify functions that would be required in the Python files.
<details><summary>Overview</summary>
<img src="">
</details>

### Data Models

This project uses Object Orientated Programming to interact and manipulate the following:

  - Lists - This project uses list to aid the storage of data from the Google Sheets file to variables and vice versa.

  - Google Sheets API - Google Sheets was used in this project to store all required data outside the container.


## Technologies Used

### Languages

- Python 3 - Used to create the command line based app.

### Framework and Tools

 - Git - Used for version control.
 - GitHub - Used to deploy the projects code.
 - Gitpod - Used to develop and test code.
 - [lucidchart](https://www.lucidchart.com/) Used to create the project flow.
 - LibreOffice Draw - Used to create the flowchart.
 - Google Sheets - Used to store data outside of the program with the User data, food menu and sales records stored on separate worksheets.
 - Google Cloud Platform - Used to manage access permissions to google services such as google autho and google sheets.
 - Heroku Platform - Used to deploy the live project.
 - PEP8 - Used to validate code against Python conventions.

## Libraries

### Python Libraries

 - os - Used to determine operating system and clear CLI.
 - time - Used to create a delay effect.
 - datetime - Used to get current time stamp and assign times to orders.

### Third Party Libraries

 - tabulate - I used this library to output lists in a table format enhancing user experience and overall readability.
 - termcolor - I used this library to give colour to user feedback and instructions.
 - pyfiglet - I used this library to generate the text art messages.
 - gspread - I used this library to add, remove and manipulate data within my Google Sheets worksheets and to interact with Google APIs
 - google.oauth.service_account - I used this library to set up the authentication needed to access the Google API and connect the Service Account using the Credentials function. From this a cred.json file was generated with all details needed for the API to access the Google account. This information is then stored in the config var section when deploying to Heroku.

## Features

### Existing features

### Welcome message

The welcome message is featured on the home page and will greet users with a friendly message.

<details>
<summary>Welcomw message image</summary>
<img src = "">
</details>

### Welcome message invalid input feedback

The welcome message invalid input feedback is featured on the welcome page and will alert users of an invalid option entry.

<details>
<summary>Welcome message invalid input image</summary>
<img src = "">
</details>

### User Name

This page asks users to provide their name.

<details>
<summary>User details image</summary>
<img src = "">
</details>

### Delivery Type Options

There are two delivery type options, one for home delivery and another for pickup. Pickup will auto populate the address as 'The Pizza Hub'. For home delivery, customers will be asked to enter their address.

<details>
<summary>delivery type image</summary>
<img src = "">
</details>

 ### Menu
 
The Menu feature will display a tabulated format of all items available for order. The menu has three options: Add item, preview order, quit.

<details>
<summary>Menu img</summary>
<img src = "">
</details>

### Add item to order

The Add item to order feature on the Menu page allows users to add an item to their order by typing the relevant item number as displayed on the menu.

<details>
<summary>Add item to order image</summary>
<img src = "">
</details>

### Invalid item from order

The Invalid item feature on the Menu page warns users that their previously entered input is not valid.

<details>
<summary>Invalid food item number image</summary>
<img src = "">
</details>

### Empty order list warning

The empty order list warning feature on the Menu page will warn users that their order list is empty, therefore no preview is possible.

<details>
<summary>Empty list warning image</summary>
<img src = "">
</details>

### Preview order

The preview order feature on the Menu page allows users to preview the items currently added to their order.

<details>
<summary>Preview order image</summary>
<img src = "">
</details>

### Remove itam

The remove item feature on the preview page allows users to remove any selected item from user's order list.

<details>
<summary>Remove item image</summary>
<img src = "">
</details>

### Confirm order

The confirm order is a feature that will allow users to confirm the order and allows us to generate the receipt.

<details>
<summary>Confirmation order image</summary>
<img src = "">
</details>


### Display order receipt

This feature is displayed upon order completion. It includes all information which had been gathered throughout the process such as user name, delivery type, address and item ordered.

<details>
<summary>Display order receipt image</summary>
<img src = "">
</details>

### Delivery charge

This feature adds a delivery cost if the order is for delivery and adds nothing if it is for pickup.

<details>
<summary>Display delivery charge image</summary>
<img src = "">
</details>

### Display order / delivery time

This feature displays the order time and delivery / pickup time on the order receipt.

<details>
<summary>Display order / delivery time image</summary>
<img src = "">
</details>

### Quit

This feature is used throughout the app to allow the user to quit the app with a thank you message.

<details>
<summary>Quit image</summary>
<img src = "">
</details>

## Future implementations

In the future as my skills grow I would like to implement class method. 
Payment type 

## Python Validation

PEP-8 Validation was used to validate the Python code used in the app.

<details><summary>Python file - run.py</summary>
<img src="">
</details>

## Testing

### Site User Stories

1. As a user, I want to be provided with clear instructions throughout the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| All listed features in the Features section provide the user with feedback based on user input | As prompted, enter user input | User to be provided with positive and negative feedback based on user input | Works as expected |

2. As a user, I should get an option to choose my order between pickup or home delivery.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Order type options | Enter desired order type by entering D for home delivery or p for pickup | If order type Home Delivery is selected, the address is asked for | Works as expected |

3. As a user, I want to view a clear and well-structed menu.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Table formatted menu | Enter data when asked for name, address and delivery type | Menu and options to be displayed to the user  |Works as expected |

4. As a user, I want to add an item to the order list. Additionally have the option to remove items from order list.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Add item to order list | Enter item number | User input item to be validated and added to the order list with confirmation message |Works as expected |
| Remove item from order list | Enter item number | User input item to be validated and removed from the order list with confirmation message |Works as expected |

5. As a user, I want to be able to preview my order.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Preview the order list in table format  | Enter 'P' on menu page | User to be provided with a table of currently selected items for order with the following options:  remove item, add item, confirm order and quit |Works as expected |

6. As a user, I want to be able to cancel an unplaced order.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Quit | Enter 'Q' |   |Works as expected  |

7. As a user, I want to be able to see my order receipt.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Order receipt | Enter user name, order type, add item to order list and then from preview page enter 'C' | A formatted page along with user details and order summary will be displayed |Works as expected  |

8. As a user, I want to be able quit the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Quit | Enter 'Q' either from home page or menu page or preview page or receipt page | A thanku message comes and user exits the app | Works as expected |


### Site Owner Stories

1. As a site owner, I want users to be greeted with a welcome message to give the app a friendly experience.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Welcome message  | Run the app   | Title of website and welcome message to be displayed  |Works as expected  |

2. As a site owner, I want to save the user information and order data to a Google Sheets file.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Retrieve and Append data | To add item on menu page | Retrieve data from Google Sheets worksheet 'menu' and add all information entered during this process will be appended to a Google Sheets worksheet 'order_list' | Works as expected |



3. As a site owner, I want users to receive feedback based on their input.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Welcome message invalid input | Enter an invalid option at the Welcome screen  | User to be provided with feedback stating that Invalid input |Works as expected  |
| Order type options | User input | Shows positive or negative feedback based on user input | Works as expected |
| Menu | User input | Shows confirmation message for valid item and Invalid message for invalid input | Works as expected |
| Preview order | Add item in order list and then click 'P' to go to preview | Preview page is shown when user inputs are valid otherwise show feedback based on user input | Works as expected |
| Receipt | Confirm user order | Upon order completion a formatted page of order summary will be displayed to the user | Works as expected  |
| Quit | Enter 'Q' | User exits the app with a thank you message | Works as expected |


## Bugs

## Deployment

### Heroku

This project was deployed to Heroku with following steps:

1. Use the "pip freeze -> requiremnts.txt" command in the terminal to save any libraries that need to be installed in the file.
2. Navigate to https://www.heroku.com/ and login or create an account. 
3. Click the "new" button in the upper right corner and select "create new app".
<details>
<summary>Screenshot</summary>
<img src="screenshots/deployment/create_new_app.jpg">
</details>

4. Choose an app name, region and click "Create app".
<details>
<summary>Screenshot</summary>
<img src="screenshots/deployment/app_name.jpg">
</details>

5. Under Config Vars store any sensitive data which saved in .json file. Name CREDS in Key field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
<details>
<summary>Screenshot</summary>
<img src="screenshots/deployment/config_var.jpg">
</details>

6. Go to the "settings" tab, add first the Python build pack and then the node.js build pack.
<details>
<summary>Screenshot</summary>
<img src="screenshots/deployment/add_buildpack.jpg">
</details>

7. Go to the "deploy" tab and pick GitHub as a deployment method.
<details>
<summary>Screenshot</summary>
<img src="screenshots/deployment/deployment_method.jpg">
</details>

8. Click the connect button in order to connect it to github.

9. In the "Choose a branch to deploy" section 'main' was auto selected so clicked on deploy branch.
<details>
<summary>Screenshot</summary>
<img src="screenshots/deployment/manual_deploy.jpg">
</details>
 
10. Wait for the app to build and then click on the "View" link which leads to the deployed link.

----

### Clone a GitHub Repository

I made a local clone of a repository via the following steps:

  - Navigate to www.github.com and log in.
  - Once logged in navigate to the desired [GitHub Repository](https://github.com/jyotiyadav2508/pizza-hub.git)
  - Locate the code button at the top, above the repository file structure.
  - Select the preferred clone method from HTTPS. SSH or GitHub CLI then click the copy button to copy the URL to my clipboard.
  - Open Git terminal
  - Type `git clone` and paste the previously copied URL. I copied HTTPS method.
  - `$ clone https://github.com/jyotiyadav2508/pizza-hub.git`
  - Now press enter and the local clone will be created at the local location.

## Credits

## Acknowledgements

I would like to also thank the following:
  - My Husband for his support and help doing this project.
  - My Code Institute mentor Mr Sandeep Aggarwal for his guidance through this project.
  - My fellow Code Institute students from whom I got the project idea.
  - Code Institute tutor support who helped me with different issues while doing the project.
  

[Back to Top](#the-pizza-hub)
