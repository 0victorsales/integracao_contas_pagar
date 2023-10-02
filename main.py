
import json
from requests import request
from datetime import datetime, timedelta
import numpy as np
import random

#SECTION - API's

#NOTE - Matriz
app_key_matriz = "app_key_matriz"
app_secret_matriz = "app_secret_matriz"
endpoint_matriz_cont_pgr = "https://app.omie.com.br/api/v1/financas/contapagar/"

#NOTE - Filial 1
app_key_filial_1 = "app_key_filial_1"
app_secret_filial_1 = "app_secret_filial_1"

#NOTE - Filial 2
app_key_filial_2 = "app_key_filial_2"
app_secret_filial_2 = "app_secret_filial_2"

#NOTE - Endpoint
endpoint_incluir_contas_pagar = 'https://app.omie.com.br/api/v1/financas/contapagar/'
endpoint_contas_pagar = 'https://app.omie.com.br/api/v1/financas/contapagar/'
endpoint_listar_clientes = 'https://app.omie.com.br/api/v1/geral/clientes/'
endpoint_contas_corrente = 'https://app.omie.com.br/api/v1/geral/contacorrente/'




def listar_contas_pagar_filial_1(pagina: int):


    payload = json.dumps({
    'call': 'ListarContasPagar',
    'app_key': app_key_filial_1,
    'app_secret': app_secret_filial_1,
    'param': [
        {   
            "pagina": pagina,
            "registros_por_pagina": 500,
            "apenas_importado_api": "N",
              

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_contas_pagar, headers=headers, data=payload)
    
    
    if response.status_code == 200:
        return response.json()
    else:
        pass


def listar_contas_pagar_filial_2(pagina: int):


    payload = json.dumps({
    'call': 'ListarContasPagar',
    'app_key': app_key_filial_2,
    'app_secret': app_secret_filial_2,
    'param': [
        {   
            "pagina": pagina,
            "registros_por_pagina": 500,
            "apenas_importado_api": "N",
              

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_contas_pagar, headers=headers, data=payload)
    
    
    if response.status_code == 200:
        return response.json()
    else:
        pass



def incluir_conta_pagar(dic_contas_pagar):


    payload = json.dumps({
    'call': 'IncluirContaPagar',
    'app_key': app_key_matriz,
    'app_secret': app_secret_matriz,
    'param': [
        {   
            "codigo_lancamento_integracao": dic_contas_pagar["cod_integracao"],
            "codigo_cliente_fornecedor": dic_contas_pagar["cod_cliente"],
            "data_vencimento": dic_contas_pagar["data_vencimento"],
            "valor_documento": dic_contas_pagar["valor_documento"],
            "codigo_categoria": dic_contas_pagar["codigo_categoria"],
            "data_previsao": dic_contas_pagar["data_previsao"],
            "id_conta_corrente": dic_contas_pagar["cod_conta_corrente"],              

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_incluir_contas_pagar, headers=headers, data=payload)
    
    
    if response.status_code == 200:
        print('Conta a pagar criada com sucesso')
        return response.json()
    else:
        print('Não foi possivel cadastrar conta a pagar')
        pass


def listar_cliente_matriz(pagina):

    payload = json.dumps({
    'call': 'ListarClientes',
    'app_key': app_key_matriz,
    'app_secret': app_secret_matriz,
    'param': [
        {   
            "pagina": pagina,
            "registros_por_pagina": 500,   
            "apenas_importado_api": "N"          

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_listar_clientes, headers=headers, data=payload)
    
    
    if response.status_code == 200:
        return response.json()
    else:
        pass


def listar_cliente_filial_1(pagina):

    payload = json.dumps({
    'call': 'ListarClientes',
    'app_key': app_key_filial_1,
    'app_secret': app_secret_filial_1,
    'param': [
        {   
            "pagina": pagina,
            "registros_por_pagina": 500,   
            "apenas_importado_api": "N"          

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_listar_clientes, headers=headers, data=payload)
    
    
    if response.status_code == 200:
        return response.json()
    else:
        pass


def listar_cliente_filial_2(pagina):

    payload = json.dumps({
    'call': 'ListarClientes',
    'app_key': app_key_filial_2,
    'app_secret': app_secret_filial_2,
    'param': [
        {   
            "pagina": pagina,
            "registros_por_pagina": 500,   
            "apenas_importado_api": "N"          

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_listar_clientes, headers=headers, data=payload)
    
    
    if response.status_code == 200:
        return response.json()
    else:
        pass



def contas_correntes_matriz():

    payload = json.dumps({
    'call': 'ListarContasCorrentes',
    'app_key': app_key_matriz,
    'app_secret': app_secret_matriz,
    'param': [
        {   
            "pagina": 1,
            "registros_por_pagina": 500,   
            "apenas_importado_api": "N"          

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
   
    response = request(method='POST', url=endpoint_contas_corrente, headers=headers, data=payload)    
   
    if response.status_code == 200:
        return response.json()
    else:
        pass


def contas_correntes_filial_1():

    payload = json.dumps({
    'call': 'ListarContasCorrentes',
    'app_key': app_key_filial_1,
    'app_secret': app_secret_filial_1,
    'param': [
        {   
            "pagina": 1,
            "registros_por_pagina": 500,   
            "apenas_importado_api": "N"          

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
   
    response = request(method='POST', url=endpoint_contas_corrente, headers=headers, data=payload)    

    if response.status_code == 200:
        return response.json()
    else:
        pass

def contas_correntes_filial_2():

    payload = json.dumps({
    'call': 'ListarContasCorrentes',
    'app_key': app_key_filial_2,
    'app_secret': app_secret_filial_2,
    'param': [
        {   
            "pagina": 1,
            "registros_por_pagina": 500,   
            "apenas_importado_api": "N"          

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
   
    response = request(method='POST', url=endpoint_contas_corrente, headers=headers, data=payload)    
    
    if response.status_code == 200:
        return response.json()
    else:
        pass




def consultar_contas_pagar_filial_1(codigo: int):


    payload = json.dumps({
    'call': 'ConsultarContaPagar',
    'app_key': app_key_filial_1,
    'app_secret': app_secret_filial_1,
    'param': [
        {   
            "codigo_lancamento_omie": codigo,
            "codigo_lancamento_integracao": "",
                         

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_contas_pagar, headers=headers, data=payload)
   
    
    if response.status_code == 200:
        return response.json()
    else:
        pass
        



def consultar_contas_pagar_filial_2(codigo: int):


    payload = json.dumps({
    'call': 'ConsultarContaPagar',
    'app_key': app_key_filial_2,
    'app_secret': app_secret_filial_2,
    'param': [
        {   
            "codigo_lancamento_omie": codigo,
            "codigo_lancamento_integracao": "",
                         

        }
    ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

   
    response = request(method='POST', url=endpoint_contas_pagar, headers=headers, data=payload)
   
    
    if response.status_code == 200:
        return response.json()
    else:
        pass


#SECTION - Funções

def dic_clientes_matriz():

    pagina =1
    total_de_paginas = 1

    while pagina<= total_de_paginas:
        dados = listar_cliente_matriz(pagina=pagina)
        dados_clientes_matriz = dados["clientes_cadastro"]

        dicionario_clientes_matriz = {}
        for clientes_matriz in dados_clientes_matriz:
            

            cnpj = clientes_matriz["cnpj_cpf"]
            codigo_cliete_matriz = clientes_matriz["codigo_cliente_omie"]            
            dicionario_clientes_matriz[cnpj] = codigo_cliete_matriz
            

        total_de_paginas = int(dados["total_de_paginas"])
        pagina += 1

        return dicionario_clientes_matriz
    



def dic_clientes_filial_1():

    pagina =1
    total_de_paginas = 1

    while pagina<= total_de_paginas:
        dados = listar_cliente_filial_1(pagina=pagina)
        dados_clientes_filial_1 = dados["clientes_cadastro"]

        
        dicionario_clientes_filial_1 = {}
        for clientes_filial_1 in dados_clientes_filial_1:
            

            cnpj = clientes_filial_1["cnpj_cpf"]
            codigo_cliete_filial_1 = clientes_filial_1["codigo_cliente_omie"]            
            dicionario_clientes_filial_1[codigo_cliete_filial_1] = cnpj            
            

        total_de_paginas = int(dados["total_de_paginas"])
        pagina += 1

        return dicionario_clientes_filial_1



def dic_clientes_filial_2():

    pagina =1
    total_de_paginas = 1

    while pagina<= total_de_paginas:
        dados = listar_cliente_filial_2(pagina=pagina)
        dados_clientes_filial_2 = dados["clientes_cadastro"]

        dicionario_clientes_filial_2 = {}
        for clientes_filial_2 in dados_clientes_filial_2:
            

            cnpj = clientes_filial_2["cnpj_cpf"]
            codigo_cliete_filial_2 = clientes_filial_2["codigo_cliente_omie"]            
            dicionario_clientes_filial_2[codigo_cliete_filial_2] = cnpj            

        total_de_paginas = int(dados["total_de_paginas"])
        pagina += 1

        return dicionario_clientes_filial_2
    
def dic_contas_correntes_matriz():
    
    dados = contas_correntes_matriz()
    dados_contas_correntes_matriz = dados["ListarContasCorrentes"]

    dicionario_contas_matriz = {}
    for contas_matriz in dados_contas_correntes_matriz:
        descricao = contas_matriz["descricao"]
        codigo = contas_matriz["nCodCC"]
        dicionario_contas_matriz[descricao] = codigo
    
    return dicionario_contas_matriz


def dic_contas_correntes_filial_1():
    
    dados = contas_correntes_filial_1()
    dados_contas_correntes_filial_1 = dados["ListarContasCorrentes"]

    dicionario_contas_filial_1 = {}
    for contas_filial_1 in dados_contas_correntes_filial_1:
        descricao = contas_filial_1["descricao"]
        codigo = contas_filial_1["nCodCC"]
        dicionario_contas_filial_1[codigo] = descricao
    
    return dicionario_contas_filial_1


def dic_contas_correntes_filial_2():
    
    dados = contas_correntes_filial_2()
    dados_contas_correntes_filial_2 = dados["ListarContasCorrentes"]

    dicionario_contas_filial_2 = {}
    for contas_filial_2 in dados_contas_correntes_filial_2:
        descricao = contas_filial_2["descricao"]
        codigo = contas_filial_2["nCodCC"]
        dicionario_contas_filial_2[descricao] = codigo
    
    return dicionario_contas_filial_2



#SECTION - Chamada de funcoes
dicionario_contas_matriz = dic_contas_correntes_matriz()
dicionario_contas_filial_1 = dic_contas_correntes_filial_1()
dicionario_contas_filial_2 = dic_contas_correntes_filial_2()

lista_clientes_matriz = dic_clientes_matriz()
lista_clientes_fiial_1 = dic_clientes_filial_1()
lista_clientes_fiial_2 = dic_clientes_filial_2()


#SECTION - Main code

#NOTE - Contas a pagar Filial 1
codigo_lancamento_omie = 123456 

dados_contas_pagar = consultar_contas_pagar_filial_1(codigo_lancamento_omie)
if dados_contas_pagar != None:

    lista_contas_pagar = []

    #NOTE - Verifica se o contas a pagar está direcionada a matriz
    distribuicao = dados_contas_pagar["distribuicao"]
    if not distribuicao:
        print('Conta a pagar sem departamento')
    else:
        departamento = distribuicao[0]
        matriz = departamento["cDesDep"]
        if matriz == 'Matriz':
            dic_contas_pagar_filial_1 = {}
            random_codigo_integracao = random.randint(10**13, 10**14 - 1)  
            """
            Nessa Parte do código os dados do contas e receber são adicionados ao dicionário dic_contas_pagar_filial_1
            ......

            """
            
            #NOTE - Obtendo codigo do cliente Matriz
            cod_cliente_filial_1 = dic_contas_pagar_filial_1["codigo_cliente_fornecedor"]
            cnpj_cliente_filial_1 = lista_clientes_fiial_1.get(cod_cliente_filial_1, None)
            cod_cliente_integracao = lista_clientes_matriz.get(cnpj_cliente_filial_1, None)
            
            if cod_cliente_integracao == None:
                print(f'Cliente com cnpj: {cnpj_cliente_filial_1} não cadastrado na Matriz')
                
            else:
                #NOTE - Obtendo codigo conta corrente Matriz
                id_conta_corrente_filial = dic_contas_pagar_filial_1["id_conta_corrente"]
                descricao_conta_corrente_filial = dicionario_contas_filial_1.get(id_conta_corrente_filial, None)
                cod_conta_corrente_filial = dicionario_contas_matriz.get(descricao_conta_corrente_filial, None)                

                dic_contas_pagar_filial_1["cod_cliente"] = cod_cliente_integracao
                dic_contas_pagar_filial_1["cod_conta_corrente"] = cod_conta_corrente_filial
                dic_contas_pagar_filial_1               
                lista_contas_pagar.append(dic_contas_pagar_filial_1)  
        
    for cont_pagar in lista_contas_pagar:
        incluir_conta_pagar(cont_pagar)
else:
    print('Contas a pagar não e faz parte da Filial 1 - Camaçari')
    pass


#NOTE - Contas a pagaer Filial 2

dados_contas_pagar = consultar_contas_pagar_filial_2(codigo_lancamento_omie)

if dados_contas_pagar != None:
    lista_contas_pagar_fiilial_2 = []

    #NOTE - Verifica se o contas a pagar está direcionada a matriz
    distribuicao = dados_contas_pagar["distribuicao"]
    if not distribuicao:
        print('Conta a pagar sem departamento')
    else:
        departamento = distribuicao[0]
        matriz = departamento["cDesDep"]
        if matriz == 'Matriz':
            dic_contas_pagar_filial_2 = {}
            random_codigo_integracao = random.randint(10**13, 10**14 - 1)  
            """
            Nessa Parte do código os dados do contas e receber são adicionados ao dicionário dic_contas_pagar_filial_1
            ......

            """

            #NOTE - Obtendo codigo do cliente Matriz
            cod_cliente_filial_2 = dic_contas_pagar_filial_2["codigo_cliente_fornecedor"]
            cnpj_cliente_filial_2 = lista_clientes_fiial_2.get(cod_cliente_filial_2, None)
            cod_cliente_integracao = lista_clientes_matriz.get(cnpj_cliente_filial_2, None)

            if cod_cliente_integracao == None:
                print(f'Cliente com cnpj: {cnpj_cliente_filial_2} não cadastrado na Matriz')
            
            else:
                #NOTE - Obtendo codigo conta corrente Matriz
                id_conta_corrente_filial_2 = dic_contas_pagar_filial_2["id_conta_corrente"]
                descricao_conta_corrente_filial_2 = dicionario_contas_filial_2.get(id_conta_corrente_filial_2, None)
                cod_conta_corrente_filial = dicionario_contas_matriz.get(descricao_conta_corrente_filial_2, None)                

                dic_contas_pagar_filial_2["cod_cliente"] = cod_cliente_integracao
                dic_contas_pagar_filial_2["cod_conta_corrente"] = cod_conta_corrente_filial              
                lista_contas_pagar_fiilial_2.append(dic_contas_pagar_filial_2)     

    
    for cont_pagar_filial_2 in lista_contas_pagar_fiilial_2:
        incluir_conta_pagar(cont_pagar_filial_2)
else:
    print('Contas a pagar não e faz parte da Filial 2 - Conquista')
    pass