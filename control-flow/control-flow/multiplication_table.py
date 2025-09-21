number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication table for {number}:")
print("-" * 30)


for i in range(1, 11):
    
    product = number * i
    

    print(f"{number} * {i} = {product}")