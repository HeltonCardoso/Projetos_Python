#MAIOR_IDADE = 18

#idade = int(input("Informe a sua idade "))

#if idade >= MAIOR_IDADE:
 #   print("Maior de Idade:")

#if idade < MAIOR_IDADE:
 #   print("Menor de idade não pode emitir CNH:")
#opcao = int(input("Informe uma opçãp :[1] Sacar \n[2] Extrato: "))

#if opcao == 1:
 #   valor = float(input("Informe a quantia para o saque "))
#elif opcao ==2:
 #   print("Exibindo o extrato...")
   #sys.exit("Opcão Invalida")
conta_normal = True
conta_universitaria = False
saldo = 2500
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
         print("Não foi possivel realizar o saque:")
elif conta_universitaria:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
else:
     print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente:")




