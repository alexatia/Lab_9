def decode(password):
    decoded_password = ''
    for char in password:
        decoded_password += str(((int(char)+10)-3) % 10)

    return decoded_password
