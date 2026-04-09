input("6'2")
print("How old are you", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

college = input("Where did you go to college?")
work = input("\033[FWhere do you currently work?")

print(f"\rSo, you went to {college}, and are now working at {work}.       ")
