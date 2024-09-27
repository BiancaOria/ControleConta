# from controleConta.buscarConta  import buscarConta
# from controleConta.criarConta   import addConta
# from controleConta.deletarConta import deletarConta
# from controleConta.editarConta  import editarNomeConta
# from controleConta.listarConta  import listar
# from controleConta.sacar        import sacar
# from controleConta.depositar    import depositar
from ex2.controleConta.buscarConta import buscarConta



def inputAddConta():
    nome = input('Digite o nome do cliente:')
    addConta(nome)

def inputDeletarConta():
    numero = int(input('Digite o número da conta:'))
    deletarConta(numero)

def inputEditarConta():
    numero = int(input('Digite o número da conta:'))
    nome = int(input('Digite o nome do cliente:'))
    editarNomeConta(numero,nome)

def inputBuscarConta():
    numero= int(input('Digite o número da conta:'))
    print(buscarConta(numero))

def inputSacar():
    numero= int(input('Digite o número da conta:'))
    valor = int(input('Digite o valor do saque:'))
    sacar(numero,valor)

def inputDepositar():
    numero= int(input('Digite o número da conta:'))
    valor = int(input('Digite o valor do deposito:'))
    depositar(numero,valor)
    

opcoes = {
    '1': inputAddConta,
    '2': inputEditarConta,
    '3': inputDeletarConta,
    '4': inputBuscarConta,
    '5': listar,
    '6': inputSacar,
    '7': inputDepositar,
    '8': exit
}

def menuPrincipal():
    while True:
        print('___Bem Vindo___')
        print('1__Adicionar Conta')
        print('2__Editar Conta')
        print('3__Apagar Conta')
        print('4__Buscar Conta')
        print('5__Listar Contas')
        print('6__Saque')
        print('7__Deposito')
        print('8__Encerrar Menu')

        opcao = input('Digite a opcao:')

        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print('Opção inválida!')

    