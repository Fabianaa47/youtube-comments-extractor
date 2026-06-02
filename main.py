"""
Script pentru extragerea comentariilor populare de la un videoclip de pe YouTube.

Echipa: 12-E5
Studenti: BĂLAN FABIANA-ROBERTA, BĂLAN MIRUNA-COSMINA
Tema proiect: D2-T1 | Parcurgerea unor documente pentru a extrage informația cerută.

Surse folosite:
- BeautifulSoup / web scraping: https://realpython.com/beautiful-soup-web-scraper-python/
- youtube-comment-downloader: https://pypi.org/project/youtube-comment-downloader/
- YAML / PyYAML: https://pyyaml.org/wiki/PyYAMLDocumentation
"""

from itertools import islice
import yaml
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR


# Link către videoclipul ales
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Câte comentarii vrem să salvăm
numar_comentarii = 5

# Numele fișierului în care salvăm datele
fisier_YAML = "comentarii.yaml"


def extrage_comentarii(video_url, numar_comentarii):
    """
    Funcția extrage comentariile populare de la un videoclip YouTube.
    Returnează o listă de dicționare.
    """

# Ne permite să accesăm comentariile.
    downloader = YoutubeCommentDownloader()

    # Obținem comentariile sortate după popularitate
    comentarii_youtube = downloader.get_comments_from_url(
        video_url,
        sort_by=SORT_BY_POPULAR
    )
    lista_comentarii = []

    # Luăm doar primele 5 comentarii
    for comentariu in islice(comentarii_youtube, numar_comentarii):
        recenzie = {
            "autor": comentariu.get("author", "Autor necunoscut"),
            "data": comentariu.get("time", "Data necunoscuta"),
            "continut": comentariu.get("text", "")
        }

        # Adăugăm recenzia (dicționarul) în lista de comentarii.
        lista_comentarii.append(recenzie)
    return lista_comentarii


def salveaza_in_yaml(comentarii, nume_fisier):
    """
    Funcția salvează lista de comentarii într-un fișier YAML.
    """

    with open(nume_fisier, "w", encoding="utf-8") as fisier:

        # Transformăm lista de comentarii în format YAML.
        yaml.safe_dump(
            comentarii,
            fisier,
            allow_unicode=True,
            sort_keys=False
        )

def main():
    """
    Funcția principală a programului.
    """

# Apelăm funcția și salvăm.
    comentarii = extrage_comentarii(video_url, numar_comentarii)
    salveaza_in_yaml(comentarii, fisier_YAML)
    print("Comentariile au fost salvate in fisierul:", fisier_YAML)

if __name__ == "__main__":
    main()