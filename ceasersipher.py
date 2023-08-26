from art import logo

print("Welcome to the Caesar Cipher")
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def greating():
    action = input("Do you want to encode(E) or decode(D) message? ")
    inp_message = input("Please enter your message without spaces: ")
    cipher_step = input("Please enter your cipher's shift: ")
    if action.lower() == 'e':
        encode(inp_message, cipher_step)
    elif action.lower() == 'd':
        decode(inp_message, cipher_step)
    else:
        print("You should enter 'E' for encode or 'D' to decode")
    
    cont_message = input("Do you want to continue? Y for yes or anything else for no: ")
    if cont_message.lower() == 'y':
        greating()
    else:
        pass

def encode(message, step):
    new_message = []
    for char in message.lower():
        index = alphabet.index(char)
        new_index = index + int(step)
        if new_index > 24:
            new_index = new_index - 25
        elif new_index < 0:
            new_index = new_index + 25
        else:
            pass
        new_letter = alphabet[new_index]
        new_message.append(new_letter)
    print("".join(new_message))



def decode(message, step):
    new_message = []
    for char in message.lower():
        index = alphabet.index(char)
        new_index = index - int(step)
        if new_index > 24:
            new_index = new_index - 25
        elif new_index < 0:
            new_index = new_index + 25
        else:
            pass
        new_letter = alphabet[new_index]
        new_message.append(new_letter)
    print("".join(new_message))

greating()