# Problem 1
user = input("Whats ur name\n")
ga = ("Happy Durga puja ")
print(ga+user)

# Problem 2
letter = '''Dear <NAME>,
Greetings from Sasta Coding Hub.org.
Im happy to inform that
You are selected!

Thnaks and regards,
RAJU BHAI

Date: <|Date|>'''
name = input("Enter your name\n")
date = input("Enter current date\n")
letter = letter.replace("<NAME>", name)
letter = letter.replace("<|Date|>", date)
print(letter)

# Problem 3
st = "Checkout double  spaces"
doublespace = st.find("  ")
print(doublespace)

#  Problem 4
st = "Checkout double  spaces  ok"
doublespace = st.replace("  ", " ")
print(doublespace)

# Problem 5
letter = "Dear Abbas, Im here to help you! Thanks!"
print(letter)

formatted_letter = "Dear Abbas, \n\tIm here to help you! \nThanks!"
print(formatted_letter)