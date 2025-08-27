from excel_reader import lire_excel
from word_generator import generer_word
from pdf_generator import generer_pdf

if __name__ == "__main__":
    fichier_excel = "donnees.xlsx"
    fichier_word = "rapport.docx"
    fichier_pdf = "rapport.pdf"

    # 1. Lire Excel
    donnees = lire_excel(fichier_excel)

    # 2. Générer Word
    generer_word(donnees, fichier_word)
    print(f"✅ Word généré : {fichier_word}")

    # 3. Générer PDF
    generer_pdf(donnees, fichier_pdf)
    print(f"✅ PDF généré : {fichier_pdf}")
