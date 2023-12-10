Num = int(input("Enter a integer number: ").strip())

if Num <= 1:
    print(f"{Num} is cannot be factored.")
else:
    number = 2
    while number < Num:
        if Num % number == 0:
            smallest_factor = number
            break
        number += 1
    else:
        smallest_factor = Num
        print(f"The smallest factor of {Num} is {smallest_factor}")