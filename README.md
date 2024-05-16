# Simple Python Banking Script
The Python Banking System is a simple script that simulates basic banking operations such as withdrawals. It allows users to withdraw money from their accounts, taking into account their balance and overdraft limit if necessary.

## Features:
Account Management: The script provides functionality to manage individual bank accounts, including name, account number, balance, and overdraft limit.

Withdrawal Functionality: Users can withdraw money from their accounts, with the script automatically deducting the amount from their balance or utilizing their overdraft limit if necessary.

## How to Use:
Define Bank Accounts: Define bank accounts with their respective details such as name, account number, balance, and overdraft limit.

Withdraw Money: Use the withdraw() function to withdraw money from a specific account. Provide the account and the amount to withdraw as arguments.

Follow Prompts: The script will prompt you to confirm the withdrawal and provide options to proceed or quit the withdrawal process.

Withdrawal Complete: Once the withdrawal is complete, the script will display the remaining balance in the account.

Example:
```
accountBegum = {
    'name': 'Begum Oral',
    'accountNo': '111222333',
    'balance': 3000,
    'overdraft': 2000
}

withdraw(accountBegum, 5000)
```
