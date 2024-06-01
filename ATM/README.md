# ATM Simulator

This project is an ATM Simulator application built using the `customtkinter` library for the GUI and a database module (`mysql.connector`) for managing account information. The application allows users to create, remove, and manage bank accounts, including checking balances, making deposits, and withdrawing funds.

## Features

- Create new bank accounts with an initial balance
- Remove existing bank accounts
- Check the balance of an account
- Deposit money into an account
- Withdraw money from an account

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LiveKiller/technohacks/ATM.git
   cd ATM
   ```

2. **Install dependencies:**

   This project requires Python and the following Python libraries:
   
   - customtkinter
   - pillow
   - mysql.connector

   You can install them using pip:

   ```bash
   pip install customtkinter pillow
   ```

3. **Ensure the database module (`db`) is set up:**

   The database module (`db`) should contain functions for adding accounts, removing accounts, getting balances, and updating balances. Ensure you have this module in the project directory.

## Usage

1. **Run the application:**

   ```bash
   python ATM.py
   ```

2. **Interacting with the ATM Simulator:**

   - **Create Account:** Enter the account ID and name, then click "Create Account". You'll be prompted to enter an initial balance.
   - **Remove Account:** Enter the account ID and name, then click "Remove Account".
   - **Check Balance:** Enter the account ID and name, then click "Check Balance".
   - **Deposit:** Enter the account ID and name, then click "Deposit". You'll be prompted to enter the deposit amount.
   - **Withdraw:** Enter the account ID and name, then click "Withdraw". You'll be prompted to enter the withdrawal amount.

## File Structure

- `atm_simulator.py`: The main application file containing the GUI and logic.
- `db.py`: The database module for handling account data.
- `img.png`: The background image for the application.

## Database Module (`db.py`)

Ensure your `db.py` file contains the following functions:

- `create_table()`: Creates the necessary table if it doesn't exist.
- `add_account(id, name, initial_balance)`: Adds a new account and returns the account ID.
- `remove_account(id, name)`: Removes an account and returns a boolean indicating success.
- `get_balance(id, name)`: Returns the balance for the specified account.
- `update_balance(id, name, amount)`: Updates the balance for the specified account and returns a boolean indicating success.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://python-pillow.org/)

Feel free to customize this `README.md` file to better fit your specific needs and project details.
