email = input("Enter your email: ")     #sample email: fareedzafar657@gmail.com
if len(email) >= 6:
    if "@" in email and email.count("@") == 1:
        if email[0].isalpha():
                if (email[-3]==".") ^ (email[-4]=="."):     # XOR operator
                    if " " in email:
                        print("Wrong email.")
                    else:
                        pass
                else:
                    print("Wrong email.")
        else:
            print("Wrong email.")
    else:
        print("Wrong email.")
else:
    print("Wrong email.")
