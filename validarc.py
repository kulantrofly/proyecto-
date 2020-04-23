'''

E: Extranjero
PE: Panameño Nacido en el extranjero
PI: Panameño Indigena
N: Naturalizado
'''
import re


def instrucciones():
    print("Bienvenido al sistema de Validacior de Cedulas  ")


def panameno():
    while True:
        cedula = input("\nIngrese su cedula presiona l para terminar: ")
        if cedula.lower() == "l":
            break

        else:

            cedula_1 = re.findall(r"\A(N|E)+-\d+-\d", cedula)
            cedula_2 = re.findall(r"\A([1-9]|PE|PI)+-\d+-\d", cedula)

            testLength = cedula.split("-")
            if cedula_1 and len(testLength[0]) == 1:
                print("\n  Esta cedula es valida!!!!.")
            elif cedula_2 and len(testLength[0]) <= 2:
                if testLength[0] in "PEPI" or int(testLength[0]) <= 13:
                    print("\nBien! Esta cedula es valida.")
                else:
                    print("\nCedula Invalida")
            else:
                print("\nCedula Invalida")


if __name__ == "__main__":
    instrucciones()
    panameno()
    print("\ngracias")
