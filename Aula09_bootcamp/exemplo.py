from utils_log import log_decorator

"""def soma(x, y):
    try: 
        soma = x + y
        logger.info(f'Você digitou os valores corretos, a soma é: {soma}')
        return soma
    except:
        logger.critical('Você tem que digitar os valores corretos.')
"""

@log_decorator
def soma(x, y):
    return x + y

soma(2, 3)
soma(2, "3")
soma(2, 1)