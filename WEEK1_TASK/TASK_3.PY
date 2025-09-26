# Program on if-else and loops

# If-else example: Check pass or fail
marks = 45
if marks >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")

print("\nFor loop example: Print even numbers from 1 to 10")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\nWhile loop example: Countdown from 5 to 1")
count = 5
while count > 0:
    print(count)
    count -= 1