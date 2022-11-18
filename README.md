# Pizza Hub

Developer: Jyoti Yadav

The live link of website- ![Live Link]() (#top)

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
 - Be able to add and remove items from an order or cancel the order prior to submission.
 - The ability to preview their order.

### Site Owner Goals

 - To rovide customers an easy-to-use app to order pizza from The pizza Hub.
 - To provide home delivery or pickup option to the customers.
 - To provide the customer the ability to preview their orders.
 - To provide the customer to choose either final confirmation or cancel their order.
 - To provide the customer to exit to home page any time.
 - Ensure all user inputs are validated and errors handled as to not provide issues with orders and a negative user experience.

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

#### First-time  User

1. As a user, I want to be:
    - provided with clear instructions throughout the app.
    - able to choose my order between pick up or home delivery.
    - able to view the menu.
    - able to add items to my order.
    - able to remove items from my order.
    - able to preview an order.
    - able to cancel an unplaced order.
    - able to place an order.
    - shown a receipt.
    - able to exit the app.

#### Site Owner

2. As the site owner, I would want:
    - User to be greeted with a welcome message to give a friendly feel to the app.
    - User information to be saved to a Google Sheets file.
    - Orders to be saved to a Google Sheets file.
    - User to get feedback based on their input.

### User Manual
<details><summary>Instructions</summary>


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

 - tabulate - JUSTIFICATION: I used this library to output lists and dictionaries in a table format enhancing user experience and overall readability.
 - termcolor - JUSTIFICATION: I used this library to give colour to user feedback and instructions
 - pyfiglet - JUSTIFICATION: I used this library to generate the text art messages
 - gspread - JUSTIFICATION: I used this library to add, remove and manipulate data within my Google Sheets worksheets and to interact with Google APIs
 - google.oauth.service_account - JUSTIFICATION: I used this library to set up the authentication needed to access the Google API and connect the Service Account using the Credentials function. From this a cred.json file was generated with all details needed for the API to access the Google account. This information is then stored in the config var section when deploying to Heroku.

## Existing features

### Welcome message

The welcome message is featured on the main page and will greet users with a friendly message.

[Welcome message image]()

### Welcome message invalid input feedback

The welcome message invalid input feedback is featured on the welcome page and will alert users of an invalid option entry.

[Welcome message invalid input image]()

### User details



[User details image]()

### Delivery Type Options

 There are two delivery type options, one being home delivery and another of pickup. Pickup will auto populate the address as The Pizza Hub. For home delivery, customers will be asked to enter their address.

 [delivery type image]()

 ### Menu
 
The Menu feature will display a tabulated format of all items available for order. The menu has 5 options: Add item, remove item, preview order, cancel order and complete order.

[Menu img]()

### Add item to order

The Add item to order feature on the Menu page allows users to add an item to their order by typing the relevant number as displayed on the menu.

[Add item to order image]()

### Invalid item from order

The Invalid item feature on the Menu page warns users that their previously entered input is not valid.

[invalid menu number]()

### Preview order

The preview order feature on the Menu page allows users to preview the items currently added to their order.

[Preview order image]()

### Cancel order

The cancel order feature on the Menu page allows users to cancel their order and return to the Welcome page.

[Cancel order image]()

### Complete order

The complete order is a feature that will allow users to complete and process the order or cancel and return to the menu and all of its options.

[Complete order image]()

### Display order receipt

The display order receipt featured will be displayed upon order completion. It includes all information which had been gathered throughout the process such as user name, name, address, delivery type and items order.

[Display order receipt image]()

### Quit

The quit is a feature used throughout the app to allow the user to validate they do intend to quit and if not return to the current position in the app.

[Quit image]()

## Future implementations

In the future as my skills grow I would like to implement the following features:
    - 

## Python Validation

PEP-8 Validation was used to validate the Python code used in the app.

<details><summary>Python file - run.py</summary>
<img src="">
</details>

## Testing

### Manual testing

### Automated testing

## Bugs

## Deployment

### Heroku

### Forking the GitHub Repository

### Clone a GitHub Repository

## Credits

## Acknowledgements

I would like to also thank the following:

[Back to Top](#top)
