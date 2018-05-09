import random


def generate_password(numbers):
    """
    Generates a random password of letters, numbers and special characters
    Parameters: accepts an int
    Returns: returns a string
    """

    password = ""
    count = 0

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z"]
    special_char = ["!", "@", "#", "$", "%", "&", "*"]
    order = ["alphabet", "number", "special_char"]

    def random_special_char(char_list):
        return char_list[random.randint(0, 6)]

    def random_number():
        return random.randint(0, 10)

    def random_alphabet(alphabet_list):
        upper_or_lower = random.randint(1, 2)
        if upper_or_lower == 1:
            return alphabet_list[random.randint(0, 25)].upper()
        else:
            return alphabet_list[random.randint(0, 25)].lower()

    def random_order(order_list):
        return order_list[random.randint(0, 2)]

    while count < numbers:
        selection = random_order(order)
        if selection == "alphabet":
            alph_character = random_alphabet(alphabet)
            password = password + alph_character
        if selection == "number":
            num_character = str(random_number())
            password = password + num_character
        if selection == "special_char":
            specialchar_char = random_special_char(special_char)
            password = password + specialchar_char
        count += 1
    return password


new_password = generate_password(random.randint(5, 100))
print(f'==== New Password ====\n\n{new_password}')
