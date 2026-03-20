full_name = input("Enter your full name in incorrect case: ")
pascal_casing_full_name = "".join(word.title() for word in full_name.split())
print("full name:", pascal_casing_full_name)
