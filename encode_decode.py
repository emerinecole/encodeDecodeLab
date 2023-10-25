
#this encode and main function are written by Cole Emerine



# function to encode the password
def encode(seq):
    new = ""
    for item in seq:
        temp = int(item)+3
        new += str(temp)

    print("Your password has been encoded and stored!")
    return new


def decode(seq):
    pass


#main function to call the loop for encoding and decoding
def main():
    choice = 0
    while choice != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encod_pswd = encode(password)
        elif choice == 2:
            print(f'The encoded password is {encod_pswd}, and the original password is {decode(encod_pswd)}.')
        else:
            break



if __name__ == "__main__":
    main()