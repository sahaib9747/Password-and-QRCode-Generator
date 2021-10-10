import random
import qrcode
import string 


def generate_password(pass_length):
    """ This function takes a length of password and process to consists a password using various characters """

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    mixed = lower + upper + digits + symbols  # combinations of all digits, characters, symbols. 

    password = ''.join(random.sample(mixed, pass_length)) # will return a password of given length 
    
    return password


def generate_qrcode(password):
    """ This function takes a password and generate a qr code afterwards it get saved in desired location """
    
    filename = input("Enter your filename: ")  # file will be created automatically 
    img = qrcode.make(password)
    img.save(filename + '.png')


def main():
    pass_length = int(input("Set Password Length: "))
    password = generate_password(pass_length)
    print(f'Your password is: {password}')
    
    generate_qrcode(password)
    print('Your password has been saved as QR Code!')


if __name__ == '__main__':
    main() # run the app