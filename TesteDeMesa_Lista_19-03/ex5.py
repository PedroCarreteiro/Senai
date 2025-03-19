idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))

if idade1 > idade2 and idade1 > idade3:
    print("A idade da primeira pessoa é a maior")
elif idade2 > idade1 and idade2 > idade3:
    print("A idade da segunda pessoa é a maior")
elif idade3 > idade1 and idade3 > idade2:
    print("A idade da terceira pessoa é a maior")

if idade1 < idade2 and idade1 < idade3:
    print("A idade da primeira pessoa é a menor")
elif idade2 < idade1 and idade2 < idade3:
    print("A idade da segunda pessoa é a menor")
elif idade3 < idade1 and idade3 < idade2:
    print("A idade da terceira pessoa é a menor")