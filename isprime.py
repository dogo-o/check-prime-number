n = int(input("Número: "))
primo = True
if n < 2:
    primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
if primo:
    print("Primo")
else:
    print("Não é primo")
