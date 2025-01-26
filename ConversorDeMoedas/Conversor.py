import requests

URL_PRIMARY = "https://economia.awesomeapi.com.br/json/last/"

def escrevaOsDados():
    moeda1 = input("Digite a sigla da primeira moeda que será convertida: ").upper()
    valor1 = float(input("Digite a quantidade da primeira moeda: "))
    moeda2 = input("Digite a sigla segunda moeda: ").upper()
    conversor(moeda1, valor1, moeda2)
    
def conversor(moeda1, valor1, moeda2):
    url = URL_PRIMARY+moeda1+"-"+moeda2
    siglas = moeda1 + moeda2
    sla = requests.get(url).json().get(siglas)
    res = float(sla.get('bid')) * valor1
    print(f"\n{valor1} {moeda1} = {res} {moeda2}  |  Data: {sla.get('create_date')}\n")

if __name__ == "__main__":
    print("--------------------\nBEM VINDO AO CONVERSOR DE MOEDA DO YAGO!\n--------------------\n")
    resposta = input("Digite 'S' para realizar alguma conversao, se nao quiser, 'N': ")
    while resposta.lower() != 'n':
        escrevaOsDados()
        resposta = input("Digite 'S' para realizar alguma conversao, se nao quiser, 'N': ")
    print("ATÉ BREVE!!!")