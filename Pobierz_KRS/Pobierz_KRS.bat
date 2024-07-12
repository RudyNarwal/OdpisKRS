@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

:: Zapytaj użytkownika o numer KRS
set /p KRS=Podaj numer KRS: 

:: Zapytaj użytkownika o typ rejestru
echo Wybierz typ rejestru:
echo 1. Przedsiębiorstwa
echo 2. Stowarzyszenia
set /p REJESTR=Wybierz opcję (1 lub 2): 

:: Ustaw typ rejestru na podstawie wyboru użytkownika
if %REJESTR%==1 (
    set TYP_REJESTRU=P
) else (
    if %REJESTR%==2 (
        set TYP_REJESTRU=S
    ) else (
        echo Niepoprawny wybór. Skrypt zakończy działanie.
        goto :eof
    )
)

:: Skonstruuj URL do API
set URL=https://api-krs.ms.gov.pl/api/krs/OdpisPelny/%KRS%?rejestr=%TYP_REJESTRU%&format=json

:: Wykonaj żądanie do API i zapisz wynik do pliku
echo Wykonuję żądanie do API...
curl -s -o OdpisPełny%KRS%.json "%URL%"

:: Sprawdź, czy plik OdpisPełny%KRS%.json został utworzony
if exist OdpisPełny%KRS%.json (
    echo Wynik został zapisany do pliku OdpisPełny%KRS%.json
    python convert_to_pdf.py wynik.json OdpisPełny%KRS%.pdf
    if exist OdpisPełny%KRS%.pdf (
        echo Plik PDF został utworzony jako OdpisPełny%KRS%.pdf
        del OdpisPełny%KRS%.json
        del *.pkl
    ) else (
        echo Wystąpił błąd podczas konwersji do PDF.
    )
) else (
    echo Wystąpił błąd podczas pobierania danych z API.
)

:end
pause