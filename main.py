print("Hello, World!")
print("Good morning!")

#apply the input function
user_input = input("What is your name? ")
#print the stored input
print("Your name is " + user_input + ".")

#create variables
num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True

tally_local_werewolves = 10
werewolf_name = "Billy"
is_warewolf = False

#Print the variables
werewolf_name = "Wendy"
print(werewolf_name)

#Make our own variable
favorite_color = input("What is your favorite color? ")
#Print variable output
print(favorite_color)

#example of conditional logic
user_howl = int(input("How many times do you howl at the moon on a typical night? Please input an integer of 0 or greater. "))
if user_howl > 0:
  print("You may be a werewolf.")

#if-else statements
#temperature outside
temp = int(input("What is the temperature outside? "))
if temp > 80:
  print("Turn on the AC.")
else:
  print("Opens the windows.")

#What is the score?
score = int(input("What is your test score? "))
#Determine the grade.
if score >= 90:
  print("Your grade is an A.")
else:
  if score >= 80:
    print("Your grade is a B.")
  else:
    if score >= 70:
      print("Your grade is a C.")
    else:
      if score >= 60:
        print("Your grade is a D.")
      else:
        print("Your grade is an F.")

#What is the score? ifelse statements
score = int(input("What is your test score? "))
#Determine the grade.
if score >= 90:
  print("Your grade is an A.")
elif score >= 80:
  print("Your grade is a B.")
elif score >= 70:
  print("Your grade is a C.")
elif score >= 60:
  print("Your grade is a D.")
else:
  print("Your grade is an F.")

#using multiple questions to establish if person is a werewolf

werewolf_test_counter = 0

#werewolfs like the full moon.
#Question version: Ask the user "Do you like the full moon? (Type yes or no.)"

werewolf_test_1 = input("Do you like the full moon? (Type yes or no.)")

#werewolfs have super healing.
#Question version: Ask the user "Do you heal super fast? (Type yes or no.)"

werewolf_test_2 = input("Do you heal super fast? (Type yes or no.)")

#werewolfs don't like silver.
#Question version: Ask the user "Are you allergic to silver? (Type yes or no.)")

werewolf_test_3 = input("Are you allergic to silver? (Type yes or no.)")

#Question version:
#Create conditionals that check how many test questions the user answered that indicated they are a werewolf.

if werewolf_test_1 == "yes":
  werewolf_test_counter = werewolf_test_counter + 1
if werewolf_test_2 == "yes":
  werewolf_test_counter = werewolf_test_counter + 1
if werewolf_test_3 == "yes":
  werewolf_test_counter = werewolf_test_counter + 1

#Question version:
#Create an output if the user is clearly not a werewolf.

if werewolf_test_counter == 0:
  print("You are not a werewolf.")

#If they indicated that they might be a werewolf.
#Question version: create an elif condition if the user might be a werewolf.

elif werewolf_test_counter == 1:
  print("You might be a werewolf.")

#Otherwise, the user is definitely a werewolf.
#Question version: end the conditional if the user is definitely a werewolf.

else:
  print("You are a werewolf.")




                        
