# Airbnb Clone - Python

## Project Description



This project is a simplified Python implementation of an Airbnb clone. It aims to replicate some of the basic functionalities of the Airbnb platform, allowing users to manage and book accommodations. The project includes a command-line interface (CLI) for users to interact with the system.


## Command Interpreter

The command interpreter is a text-based interface that enables users to interact with the Airbnb clone. It interprets user commands and performs corresponding actions, such as creating listings, booking accommodations, and managing user accounts.


## How to Start

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/airbnb-clone-python.git
   cd airbnb-clone-python
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Command Interpreter:**
   ```
   python airbnb_cli.py
   ```

## How to Use

Once the command interpreter is running, you can interact with the Airbnb clone by entering commands. Here are some of the available commands:


- `create_user`: Create a new user account.
  ```
  > create_user JohnDoe
  ```

- `create_listing`: Create a new accommodation listing.
  ```
  > create_listing "Cozy Apartment" 2 "123 Main St"
  ```

- `book_accommodation`: Book an accommodation for a specific user.
  ```
  > book_accommodation JohnDoe "Cozy Apartment" 2023-12-01 2023-12-10
  ```

- `list_accommodations`: List all available accommodations.
  ```
  > list_accommodations
  ```
