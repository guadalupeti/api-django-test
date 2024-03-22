import re
import validate_docbr

def cpf_valido(numero_do_cpf):
    cpf = validate_docbr.CPF()
    resposta = cpf.validate(numero_do_cpf)
    return resposta

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta

