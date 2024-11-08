# Break statement: exits the entire loop
num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

# Continue statement allows you to skip a loop.
devices = ["Laptop", "Phone", "Tablet", "Desktop", "TV"]
for device in devices:
    if device == "Tablet":
        continue
    print(device)