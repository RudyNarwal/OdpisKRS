****Odpis KRS****
--

Program do pobierania odpisów pełnych z KRS

****Opis****
--

Ten prosty program służy do komunikowania się z API Portalu Rejestru Sądowych, wysyłania zapytania na podstawie podanego KRS, wskazania, czy chodzi o przedsiębiorstwo czy stowarzyszenie oraz pobiera aktualny odpis z serwera. Po pobraniu pliku, który domyślnie jest dostarczany jest w formacie .json. Skrypt w Python dokonuje jego konwersji na .pdf, który jest bardziej czytelny dla przeciętnego użytkownika. Program nie posiada żadnych formatek, które dodają autentyczności dokumentu. Służy tylko do sprawdzenia wpisów w rejestrze w bardziej czytelny sposób niż robi to .json. 

Uruchamianie
--
**Zależności**

* Windows,
* Python (jakakolwiek wersja),
* Biblioteka fpdf,
* Dejavu Fonts.

**Włączanie programu**
--
Dwuklik na pliku wsadowym Windows Pobierz_KRS.bat. Postępuj zgodnie z instrukcjami a program się wszystkim zajmie.

**Autor**
--
Mateusz Trejman

**Historia wersji**
--
* 0.1
  * Wydanie wstępne
 
**Licencja**
--
Projekt stworzony na podstawie licencji GNU v3.0

**Uznanie**
--
* [Bitstream Vera Fonts](https://dejavu-fonts.github.io/License.html),
* [FPDF](http://www.fpdf.org/)
