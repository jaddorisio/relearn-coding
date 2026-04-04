
# Stores types of people, places types of people in a string that is stored in variable x
types_of_people = 10
x = f"There are {types_of_people} types of people."


# Stores two words as variables, then later users these in a string that is stored to variable y
binary = "binary"
do_not = "don't"
y = f"Those who know{binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = True 
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print (w+e)