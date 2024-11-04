def check_username_validity(username):

    if not (5 <= len(username) <= 15):
        return "Invalid username: Length must be between 5 and 15 characters."
    if not (username[0].isalpha()):
        return "Invalid username: Username must start with character."
    if not (username.isalnum()):
        return "Invalid username: Username must contain only alphanumeric characters."

    return "Valid Username"


print(check_username_validity(username="amarnath"))
