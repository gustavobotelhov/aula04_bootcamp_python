salario: float = 12550
bonus: float = 6.5

def bonus_recebido(salario_usuario,bonus_usuario) -> float:

    bonus_recebido_calculado: float = 1000 + salario * bonus 

    return bonus_recebido_calculado

print(bonus_recebido(salario,bonus))