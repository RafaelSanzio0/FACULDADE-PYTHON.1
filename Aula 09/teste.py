idade = int(input("Digite uma idade entre 0 e 150: "))

while idade < 0 or idade > 150:
    idade = int(input("Idade invalida! digite novamente: "))


salario = float(input("Digite um salario maior que zero: "))

while salario < 0:
    salario = float(input("Salario invalido! Digite o salario novamente: "))

sexo = input("Digite um Sexo Válido: ")
while sexo.upper() != "FERMININO" and sexo.upper() != "MASCULINO":
    sexo = input("Digite o sexo novamente: ")

estado_civil = input(("Digite o seu estado civil no momento: "))
while estado_civil.upper() != "SOLTEIRO" and estado_civil.upper() != "CASADO" and estado_civil.upper() != "VIUVO" and estado_civil != "DIVORCIADO":
    estado_civil = input("Formato invalido!!!Digite seu estado civil novamente: ")





