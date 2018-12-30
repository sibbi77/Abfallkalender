Abfallkalender
==============

Konvertiert eine csv Datei (Onlinekalender Stadt Hamminkeln) in eine iCalender Datei


Auf https://www.mywastewatcher.de/abfallkalender/ die eigene Straße einstellen und
eine csv-Datei erzeugen lassen (Abfallkalender_Hamminkeln.csv).

Die csv-Datei beginnt wie folgt:

```
Farbe;Abfallart;Abfuhrtag;Wochentag;V;Bemerkung
rot;SC;04.01.2017;Mittwoch;;
grau;RA;05.01.2017;Donnerstag;;
```

Kodierung der Datei muss iso-8859-1 sein.

Falls eine .xlsx-Datei heruntergeladen wurde, kann diese mit LibreOffice in .csv umgewandelt werden.

Aufruf des Programmes:

    python AbfallkalenderHamminkeln.py Abfallkalender_Hamminkeln.csv
oder
    python3 AbfallkalenderHamminkeln.py Abfallkalender_Hamminkeln.csv

es wird die Datei `Abfallkalender_Hamminkeln.csv.ics` erzeugt.
Diese Datei kann auf eine ownCloud hochgeladen werden und dann per Klick in
den Kalender importiert werden.
