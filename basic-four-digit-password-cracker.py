"""this is the basic script, feel free to optimize / make changes to it"""

def generate_possible_combinations(length, character):
    if length == 1:
        return list(character)

    sub_combinations = generate_possible_combinations(length-1, character)
    all_combinations = []

    for letter in character:
        for sub_combo in sub_combinations:
            all_combinations.append(letter + sub_combo)
    return all_combinations

res = generate_possible_combinations(4, "1234567890")
# print(res)

def crack_password(user_password, combinations):
    if user_password in combinations:
        print(f"Password matched: ...=> {user_password}")
    else:
        print("Error")
crack_password(user_password=input("Enter your 4 digit pin: "), combinations=res)
