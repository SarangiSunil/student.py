python
Copy code
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
num = int(input("Enter the number to be inserted: "))
pos = int(input("Enter the position to insert the number: "))

numbers.insert(pos-1, num)

print("The updated list is:", numbers)
