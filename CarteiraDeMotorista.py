print("-----------------------------------------------------------------------------")
print("--------------------------->A U T O   E S C O L A<---------------------------")
print("-----------------------------------------------------------------------------")
nome= str(input("Por favor, digite seu nome :""\n"))
nome=nome.upper()
tipo= (input("DIGITE A OPÇÃO DESEJADA DA SUA CNH : ( A : (CARRO), B : (MOTO) , AB : (CARRO E MOTO) , D : (CAMINHAO) ). PARA CANCELAR DIGITE (SAIR) .""\n"))
tipo = tipo.upper()
while tipo != "sair":
    ano_nasc = int(input("Digite o seu ano de nascimento :""\n"))
    ano_atual = int(input("Digite o ano atual :""\n"))
    idade = (ano_atual - ano_nasc)
    if tipo == "A" :
        resultado = "CARRO"
    elif tipo == "B" :
        resultado = "MOTO"
    elif tipo == "AB" :
        resultado = "CARRO E MOTO"
    elif tipo == "D" :
        resultado = "CAMINHÃO"
    if idade < 18 :
        print(nome,",MUITA CALMA NESSA HORA, VOCE TEM APENAS",idade,"ANOS, E AINDA NAO PODE TIRAR HABILITAÇÃO""\n")
    else:
        print(nome,",VOCE TEM",idade,"ANOS E JA PODE TIRAR HABILITAÇÃO DO TIPO ->",tipo, "<- QUE É DE", resultado ,"." "\n")

    print("-----------------------------------------------------------------------------")
    print("--------------------------->A U T O   E S C O L A<---------------------------")
    print("-----------------------------------------------------------------------------")
    tipo = (input("DIGITE A OPÇÃO DESEJADA DA SUA CNH : ( A : (CARRO), B : (MOTO) , AB : (CARRO E MOTO) , D : (CAMINHAO) ). PARA CANCELAR DIGITE (SAIR) .""\n"))