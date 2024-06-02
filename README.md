# Password Leak Checker

This repository contains a Python script that checks if any passwords stored in a specified directory have been leaked using the "Have I Been Pwned" API.

## Features

- Uses the "Have I Been Pwned" API to check if passwords have been compromised.
- Reads passwords from text files within a specified directory.
- Hashes passwords using SHA-1 and only sends partial hashes to the API for privacy.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/PasswordLeakChecker.git
    cd PasswordLeakChecker
    ```

2. Install the required libraries:
    ```sh
    pip install requests
    ```

## Usage

1. Place your password files in the `dragHerePass` directory. Each file should contain a single password.

2. Run the script:
    ```sh
    python check_passwords.py
    ```

## Code Explanation

### Functions

- **request_api_data(query_char)**:
  - Fetches data from the "Have I Been Pwned" API using the first 5 characters of the SHA-1 hash of the password.

- **get_pass_leaks_count(hashes, hash_check)**:
  - Parses the API response to find if the tail part of the hash exists and returns the count of times the password was found.

- **pwned_api_check(password)**:
  - Hashes the password using SHA-1, splits the hash to send a partial hash to the API, and checks if the password has been leaked.

- **check_pass_from_file()**:
  - Iterates over all files in the specified directory, reads the passwords, and checks them using the `pwned_api_check` function.

### Main Script

- The main script reads the passwords from files in the `dragHerePass` directory and checks if they have been leaked using the defined functions.

## Example

For example, if you have a file `password1.txt` with the content `password123` in the `dragHerePass` directory, running the script will check if `password123` has been leaked and print the number of times it was found.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## Author

Adrian Infante 

---

Happy coding!
