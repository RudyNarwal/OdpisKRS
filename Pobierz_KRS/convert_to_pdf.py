import json
import sys
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, 'KRS Data', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('DejaVu', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def json_to_pdf(json_file, pdf_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pdf = PDF()
    
    # Add DejaVu font
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf', uni=True)

    pdf.add_page()

    pdf.chapter_title("Rodzaj odpisu")
    pdf.chapter_body(data.get('odpis', {}).get('rodzaj', ''))

    naglowekP = data.get('odpis', {}).get('naglowekP', {})
    pdf.chapter_title("Nagłówek")
    pdf.chapter_body(f"Rejestr: {naglowekP.get('rejestr', '')}\n"
                     f"Numer KRS: {naglowekP.get('numerKRS', '')}\n"
                     f"Data i czas odpisu: {naglowekP.get('dataCzasOdpisu', '')}\n"
                     f"Stan z dnia: {naglowekP.get('stanZDnia', '')}")

    wpisy = naglowekP.get('wpis', [])
    pdf.chapter_title("Wpisy")
    for wpis in wpisy:
        pdf.chapter_body(f"Numer wpisu: {wpis.get('numerWpisu', '')}\n"
                         f"Opis: {wpis.get('opis', '')}\n"
                         f"Data wpisu: {wpis.get('dataWpisu', '')}\n"
                         f"Sygnatura akt sprawy dotyczącej wpisu: {wpis.get('sygnaturaAktSprawyDotyczacejWpisu', '')}\n"
                         f"Oznaczenie sądu dokonującego wpisu: {wpis.get('oznaczenieSaduDokonujacegoWpisu', '')}\n"
                         "--------------------------------------------")

    dzial1 = data.get('odpis', {}).get('dane', {}).get('dzial1', {})
    pdf.chapter_title("Dział 1: Dane Podmiotu")
    pdf.chapter_body(f"Forma prawna: {dzial1.get('danePodmiotu', {}).get('formaPrawna', [{}])[0].get('formaPrawna', '')}\n"
                     f"NIP: {dzial1.get('danePodmiotu', {}).get('identyfikatory', [{}])[0].get('identyfikatory', {}).get('nip', '')}\n"
                     f"REGON: {dzial1.get('danePodmiotu', {}).get('identyfikatory', [{}])[1].get('identyfikatory', {}).get('regon', '')}\n"
                     f"Nazwa: {dzial1.get('danePodmiotu', {}).get('nazwa', [{}])[0].get('nazwa', '')}")

    pdf.chapter_title("Siedziba i Adres")
    siedziba = dzial1.get('siedzibaIAdres', {}).get('siedziba', [{}])[0]
    adres = dzial1.get('siedzibaIAdres', {}).get('adres', [{}])[0]
    pdf.chapter_body(f"Kraj: {siedziba.get('kraj', '')}\n"
                     f"Województwo: {siedziba.get('wojewodztwo', '')}\n"
                     f"Powiat: {siedziba.get('powiat', '')}\n"
                     f"Gmina: {siedziba.get('gmina', '')}\n"
                     f"Miejscowość: {siedziba.get('miejscowosc', '')}\n"
                     f"Ulica: {adres.get('ulica', '')}\n"
                     f"Nr domu: {adres.get('nrDomu', '')}\n"
                     f"Kod pocztowy: {adres.get('kodPocztowy', '')}\n"
                     f"Poczta: {adres.get('poczta', '')}")

    pdf.output(pdf_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: python convert_to_pdf.py <input_json_file> <output_pdf_file>")
    else:
        json_file = sys.argv[1]
        pdf_file = sys.argv[2]
        json_to_pdf(json_file, pdf_file)
