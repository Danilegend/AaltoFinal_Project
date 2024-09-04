import time

value = 2

print(f"Printing multiplication table for {value}:\n")

for i in range(1, 11):
    print(f'{value} x {i} = {value * i}')
    time.sleep(1)
