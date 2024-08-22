# Dicionário para armazenar as informações do usuário
dados_usuario = {
    "nome": None,
    "salario": None,
    "bonus": None,
}

# Função para validar o nome
# Essa função é chamada no loop logo abaixo e retorna true ou false de acordo com as verificações.
# por ser uma função apenas para check é por esse motivo que ela retorna true ou false e é do tipo bool.
def validar_nome(nome: str) -> bool:
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    return True

# Loop para solicitar e validar o nome
# Nesse loop a função validar_nome é chamada passando o nome digitado pelo usuario como parametro,
# a função retorna se tudo ok TRUE ou false, se true vai adicionar o nome no dicionário e printar nome valido
while dados_usuario["nome"] is None:
    try:
        nome = input("Digite seu nome: ")
        if validar_nome(nome):
            dados_usuario["nome"] = nome
            print("Nome válido:", nome)
    except ValueError as e:
        print(e)

# Função para solicitar e validar valores numéricos
def solicitar_valor(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                raise ValueError("Por favor, digite um valor positivo.")
            return valor
        except ValueError as e:
            print("Entrada inválida.", e)

# Solicita o salário e o bônus usando a função de validação
dados_usuario["salario"] = solicitar_valor("Digite o valor do seu salário: ")
dados_usuario["bonus"] = solicitar_valor("Digite o valor do bônus recebido: ")

# Função para calcular o bônus recebido
def bonus_recebido(salario_usuario, bonus_usuario) -> float:
    return 1000 + salario_usuario * bonus_usuario

# Imprime as informações para o usuário
print(f"{dados_usuario['nome']}, seu salário é R${dados_usuario['salario']:.2f} e seu bônus final é R${bonus_recebido(dados_usuario['salario'], dados_usuario['bonus']):.2f}.")
