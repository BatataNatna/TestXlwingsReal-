import pandas as pd

def lire_donnees_patient(fichier_excel):
    """Lit toutes les feuilles de l'Excel d'un patient et retourne un dict"""
    xls = pd.ExcelFile(fichier_excel)
    data = {}

    for sheet in xls.sheet_names:
        data[sheet] = pd.read_excel(fichier_excel, sheet_name=sheet)

    return data
