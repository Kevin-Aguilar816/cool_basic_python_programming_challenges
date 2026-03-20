full_name = input("Enter your full name with incorrect case: ")
snake_case_full_name = "_".join(word.lower() for word in full_name.split())
print("full name in snake case:", snake_case_full_name)
