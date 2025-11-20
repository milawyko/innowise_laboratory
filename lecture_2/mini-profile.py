def generate_profile(age):
    if age >= 0 and age <= 12:
        life_stage = "Child"
    elif age >= 13 and age <= 19:
        life_stage = "Teenager"
    elif age >= 20:
        life_stage = "Adult"
    return life_stage

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

hobbies = []
while True:
    hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby_input.lower() == 'stop':
        break
    hobbies.append(hobby_input)

life_stage = generate_profile(current_age)
user_profile = {"Name": user_name, "Age": current_age, "Life Stage": life_stage, "Hobbies": hobbies}

print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['Name']}")
print(f"Age: {user_profile['Age']}")
print(f"Life Stage: {user_profile['Life Stage']}")
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")