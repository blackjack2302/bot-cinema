import requests
from bs4 import BeautifulSoup

def buscar_sessoes():
    url = "https://www.ingresso.com/sao-paulo/home"  # Exemplo
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, "html.parser")

    filmes = {}
    for filme in soup.select(".movie-card"):
        nome = filme.select_one(".movie-title").text.strip()
        horarios = [h.text for h in filme.select(".showtimes")]
        filmes[nome] = horarios

    return filmes
