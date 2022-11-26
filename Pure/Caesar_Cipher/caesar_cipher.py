import string

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


# FUNCTIONS
def encrypt(message, shift_num):
    """Encrypts the message based on given shift number"""
    encrypted_msg = ""
    for i in range(len(message)):
        if string.ascii_lowercase.find(message[i]) + shift_num > 25:
            encrypted_msg += string.ascii_lowercase[string.ascii_lowercase.find(message[i]) + shift_num - 26]
        else:
            encrypted_msg += string.ascii_lowercase[string.ascii_lowercase.find(message[i]) + shift_num]
    return encrypted_msg


def decrypt(message, shift_num):
    """Decrypts the message based on given shift number"""
    decrypted_msg = ""
    for i in range(len(message)):
        if string.ascii_lowercase.find(message[i]) - shift_num < 0:
            decrypted_msg += string.ascii_lowercase[26 - (shift_num - string.ascii_lowercase.find(message[i]))]
        else:
            decrypted_msg += string.ascii_lowercase[string.ascii_lowercase.find(message[i]) - shift_num]
    return decrypted_msg


# INITIALIZED VARIABLES
cc_continue = ""

print(logo)
while cc_continue != "n":
    enc_or_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_msg = input("Type your message (only letters, no spaces):\n").lower()
    msg_shift = int(input("Type the shift number:\n"))
    if enc_or_dec == "encode":
        enc_msg = encrypt(message=user_msg, shift_num=msg_shift)
        print(f"Here's the encoded result:\t{enc_msg}\n")
    elif enc_or_dec == "decode":
        enc_msg = decrypt(message=user_msg, shift_num=msg_shift)
        print(f"Here's the encoded result:\t{enc_msg}\n")
    else:
        print("You've entered invalid parameters.")

    cc_continue = input("Do you want to go again? (Y/n):\t")

"""
    Caesar Cipher:
    Encrypt - If a/A and shift number = 4:
        A-B-C-D-E
          1-2-3-4
    Decrypt - If m/M and shift number = 8:
        M-L-K-J-I-H-G-F-E
          1-2-3-4-5-6-7-8
"""
