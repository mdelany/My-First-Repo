print("What is your favorite sport?")
sport = input()

if sport == "Hockey":
    print ("That's my favorite sport too!")
elif sport == "Tennis":
    print (sport + " is so much fun")
else:
    print (sport + " sounds like fun.")

print ("What is your favorite subject?")
subject = input()
if subject == "Science" or subject == "English":
    print (subject + " is my favorite too.")
else:
    print ("I hate " + subject)

print("Which do you like better? Dogs or cats?")
dogvcat = input()
if dogvcat == "Dogs":
    print ("What's your favorite breed?")
    breed = input()
    if breed == "Pomeranian" or breed == "Husky" or breed == "Teacup poodle":
        print (breed + "s are the cutest!")
    else:
        print ("My favorite breed is pomeranians")
else:
    print ("I think dogs are better.")

print ("what's your favorite food?")
food = input()
if food == "Apple pie" or "Pizza" or "Croissant" or "Bread pudding" or "Chinese food":
    print (food + " is my favorite too!")
else:
    print (food + " sounds delicious.")
