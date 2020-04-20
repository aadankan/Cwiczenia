passwordFile = open("SecretPasswordFile.txt")
secretPassword = passwordFile.read()
typedPassword = input("Enter the password: ")
if typedPassword == secretPassword:
    print("Masz dostęp.")
    if typedPassword == "12345":
        print("This is the slogan of reckless people on suitcases.")
else:
    print("No access.")