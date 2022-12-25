import pandas as pd


def _tabela_em_branco(n):
    tabela = pd.DataFrame([], index = range(n+1), columns=['prestação','juros','amortização','saldo devedor'])
    return(tabela)

def _prestação_price(principal, juros, n):
    f = (1+juros)**n
    fator_anuidade = (f * juros)/(f-1)
    prest = principal * fator_anuidade
    return(prest)


def SAC(principal, juros, n):
    
    tabela = _tabela_em_branco(n)
    amort = principal/n

    for i in tabela.index:
        if i > 0:
            tabela.loc[i,'saldo devedor'] = tabela.loc[i-1,'saldo devedor'] - amort
            tabela.loc[i,'amortização'] = amort
            tabela.loc[i,'juros'] = tabela.loc[i-1,'saldo devedor'] * juros
            tabela.loc[i,'prestação'] = tabela.loc[i,'amortização'] + tabela.loc[i,'juros']
        else:
            tabela.loc[i,'saldo devedor'] = principal
            
    return(tabela)


def PRICE(principal, juros, n):
    
    tabela = _tabela_em_branco(n)
    prest = _prestação_price(principal, juros, n)
    
    for i in tabela.index:
        if i > 0:
            tabela.loc[i,'prestação'] = prest
            tabela.loc[i,'juros'] = tabela.loc[i-1,'saldo devedor'] * juros
            tabela.loc[i,'amortização'] = tabela.loc[i,'prestação'] - tabela.loc[i,'juros']
            tabela.loc[i,'saldo devedor'] = tabela.loc[i-1,'saldo devedor'] - tabela.loc[i,'amortização']
        else:
            tabela.loc[i,'saldo devedor'] = principal
            
    return(tabela)


