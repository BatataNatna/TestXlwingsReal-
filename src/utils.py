from datetime import datetime

def date_aujourdhui():
    return datetime.today().strftime("%Y-%m-%d")

def nettoyer_nom(nom):
    return nom.replace(" ", "_")
