'''
Funções - def em Python

usar ' def funcao()' é muito util para repetir
'''

def saudacao(msg ='ola',nome='usuario'):
    nome = nome.replace('a','@')
    print(msg,nome)

saudacao('oi')
saudacao()
saudacao()
saudacao()
saudacao(nome='samuel')
saudacao()