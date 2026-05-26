print("Welcome to the CPU Game!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit()

print("Nice! Let's play :)")

score = 0



answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:    print("Incorrect! The correct answer is 'central processing unit'.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:    print("Incorrect! The correct answer is 'graphics processing unit'.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:    print("Incorrect! The correct answer is 'random access memory'.")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:    print("Incorrect! The correct answer is 'power supply unit'.")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "% of the questions correct!")

