#Faculdade SENAC PE
#Autor: Vitor Matheus
#DataInicial- 06/01/2021
#Iniciação Científica Iot01
#Exemplo de API para guardar dados de temperatura em arquivo .csv, os dados estão sendo coletados através de um hardware(arduino).

from datetime import datetime #Biblioteca para armazenar data e hora
from pytz import timezone  #Biblioteca para definição de fuso horário
from flask import Flask

app=Flask(__name__)
caminho ='/home/VitorMatheus1/dados/registros.csv' #Definindo arquivo onde serão armazenados os dados.

@app.route('/arm/<string:codigo>/<string:chave>/<string:temperatura>')
def recebeValor(codigo, chave, temperatura):         #parâmetros definidos
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone("America/Sao_Paulo") #Escolhendo o fuso horário a ser usado
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M") #Formatando a data e hora para o padrão do Brasil

    arquivo=open(caminho,'a')
    arquivo.write(codigo + ',' + chave + ',' + data_e_hora_sao_paulo_em_texto + ',' + str(temperatura) + "\n" )
    arquivo.close()
    return temperatura






@app.route('/<string:temperatura>')
def recebeValor2(temperatura):
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone("America/Sao_Paulo") #Escolhendo o fuso horário a ser usado
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M") #Formatando a data e hora para o padrão do Brasil

    arquivo=open(caminho,'a')
    arquivo.write( "Id01"+ ',' + data_e_hora_sao_paulo_em_texto + ',' + str(temperatura) + "\n" )
    arquivo.close()
    return temperatura