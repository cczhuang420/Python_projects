import requests
import hashlib
import sys


def get_passwords():
    file_name = input('what is your passwords file path?: ')
    with open(file_name) as file:
        lines = file.readlines()
    return lines


def split_password(password):
    head = password[:5]
    tail = password[5:]
    return head, tail


def hash_password(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()


def request_api_data(char):
    url = 'https://api.pwnedpasswords.com/range/' + char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'error fetching {response.status_code}')
    return response


def check_pwned_api(password, tail, lines):
    is_pwned = False
    for line in lines:
        response_tail, count = line.split(":")
        if tail == response_tail:
            print(
                f'The password - "{password}" was found {count} times, you better to change your password')
            is_pwned = True
    if not is_pwned:
        print(f'The password - "{password}" was not found! Carry on. ')


def check_passwords(passwords):
    for password in passwords:
        password = password.rstrip('\n')  # for those reading from file
        hashed_password = hash_password(password)
        head, tail = split_password(hashed_password)
        response = request_api_data(head)
        lines = response.text.splitlines()
        check_pwned_api(password, tail, lines)


if __name__ == '__main__':
    # read input password from file
    passwords = get_passwords()
    # read input passwords from command line
    # passwords = sys.argv[1:]
    sys.exit(check_passwords(passwords))
