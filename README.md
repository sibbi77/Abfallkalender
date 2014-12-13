Abfallkalender
==============

Konvertiert eine csv Datei (Onlinekalender Stadt Hamminkeln) in eine iCalender Datei


Auf http://www.abfallkalender.wastewatcher.de die eigene Straße einstellen und
eine Exceldatei erzeugen lassen. Diese Exceldatei mit Hilfe von Excel/Calc in eine
csv Datei exportieren (UTF-8 Textkodierung).

Die csv-Datei beginnt wie folgt:
Abfuhrtermine,,,,
Bz,Abfuhrtermin,Tag,Fraktion,Bemerkung
5,05.01.15,Mo,gelb,
5,07.01.15,Mi,Schadstoff,

Aufruf des Programmes:
python AbfallkalenderHamminkeln.py gridAbfuhrtermine.csv
es wird die Datei gridAbfuhrtermine.csv.ics erzeugt.
Diese Datei kann auf eine ownCloud hochgeladen werden und dann per Klick in
den Kalender importiert werden.
