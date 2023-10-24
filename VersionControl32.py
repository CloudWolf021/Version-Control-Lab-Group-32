'''
A rudimentary password encoder and decoder.
Name: Adrian Palamarev
'''


def encode_password(input_password):  # Encode the password by adding three to each digit.
    encoded_password = ""
    for ch in input_password:
        encoded_password += chr(ord(ch) + 3)
    return encoded_password


if __name__ == "__main__":      # Main Logic
    encoded_password = None
    while True:
        print("Menu\n-------------\n"  # Print the menu
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input("Please Enter an option: "))

        if option == 1:  # Encode a password
            encoded_password = encode_password(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif option == 2:  # Decode a password
            print(f"The encoded password is {encoded_password},"
                  f"and the original password is {decode_password(encoded_password)}.\n")
        else:  # Exit the program
            break

