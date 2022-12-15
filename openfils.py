text = "i can do this!\n"
with open("test.txt", "a") as file:
    print(file.write(text))

with open("test.txt", "w") as file:
    file.write(text)

print(file.closed)
