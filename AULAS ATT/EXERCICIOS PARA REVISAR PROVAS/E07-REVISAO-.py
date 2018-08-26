'''7.	Desenvolva	um	programa	que	solicite	a	digitação	de	um
número	de	CPF	no	formato	xxx.xxx.xxx-xx	e	indique	se	é	um
número	válido	ou	inválido	através	da	validação	dos	dígitos
verificadores	e dos	caracteres	de	formatação.'''

cpf = str(input("Informe seu CPF: "))
if cpf != "###.###.###.-##":
    print("CPF INVÁLIDO")
elif cpf == "###.###.###-##":
    print("CPF VÁLIDO")