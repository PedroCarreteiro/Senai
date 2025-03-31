import re

senha = input("Digite sua senha: ")

if len(senha) >= 8:
    if re.search(r"[!@#$%^&*(),.?"":{}|<>]", senha):
        if re.search(r"[a-z]", senha):
            if re.search(r"[A-Z]", senha):
                if re.search(r"[0-9]", senha):
                    print("Senha Válida!")
                else:
                    print("Senha Inválida! A senha deve conter pelo menos um número.")
            else:
                print("Senha Inválida! A senha deve conter pelo menos uma letra maiúscula.")
        else:
            print("Senha Inválida! A senha deve conter pelo menos uma letra minúscula.")
    else:
        print("Senha Inválida! A senha deve conter pelo menos um caractere especial.")
else:
    print("Senha Inválida! A senha deve ter pelo menos 8 caracteres.")
