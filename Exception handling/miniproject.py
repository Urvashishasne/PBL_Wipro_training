file_name = input("Enter the file name:")
if not file_name.endswith(".txt"):
    file_name += ".txt"

total_items = 0
free_items = 0
total_price = 0
discount = 0

try:
    file = open(file_name, "r")
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split()
        if parts[-1].lower() == "free":
            free_items += 1
        elif parts[0].lower() == "discount":
            try:
                discount = int(parts[-1])
            except:
                print("Invalid discount amount.")
        else:
            try:
                price = int(parts[-1])
                total_price += price
                total_items += 1
            except:
                print("Invalid price in line:", line)
    file.close()
    final_price = total_price - discount
    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", total_price)
    print("Discount given:", discount)
    print("Final amount paid:", final_price)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)
