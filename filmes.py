import requests

def pegarfilme(nome):
    textfilm = nome
    apikey = "79c1806"
    url = f"https://www.omdbapi.com/?t={textfilm}&plot=full&apikey={apikey}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filmedic = {
            "titulo" : data["Title"],
            "data_lancamento" : data["Released"],
            "genero" : data["Genre"],
            "sinopse" : data["Plot"],
            "notaRottenTomatoes" : data["Ratings"][1]["Value"],
            "notaMetacritc" : data["Ratings"][2]["Value"],
            "poster" : data["Poster"]
            }
        return filmedic