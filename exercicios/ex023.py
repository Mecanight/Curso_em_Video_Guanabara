num = int(input("Digite um número entre 0 e 9999\n"))
print(num)
print(type(num))

print("A unidade de milhar é: ", (num//1000))
print(f"A centena é: ", ((num%1000)//100))
print("A dezena é :", (((num%1000)%100)//10))
print("A unidade é: ", ((((num%1000)%100)%10)))
