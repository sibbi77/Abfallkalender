# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 12:27:48 2014

@author: Sebastian Held <sebastian.held@gmx.de>
"""

"""
Dieses Programm erzeugt eine iCalendar Datei, die die Müll-Abholtage enthält.

Auf http://www.abfallkalender.wastewatcher.de die eigene Straße einstellen und
eine Exceldatei erzeugen lassen. Diese Exceldatei mit Hilfe von Excel in eine
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
"""


import sys

# tested with icalendar-3.8.4 from http://icalendar.readthedocs.org
from icalendar import Calendar, Event

from datetime import datetime, timedelta
import csv

def main():
    
    # create calendar
    cal = Calendar()
    cal.add('version','2.0')
    cal.add('prodid','-//Ingenieurbüro Held//AbfallkalenderHamminkeln_Python_import//DE')

    f = open(sys.argv[1], 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            #print(row)
            try:
                datum = datetime.strptime(row[1],'%d.%m.%y')
                #print(datum)
                event = Event()
                event.add('dtstamp',datetime.now())
                event.add('dtstart',datum.date())
                # ownCloud is broken, it needs a dtend property
                event.add('dtend',(datum + timedelta(days=1)).date())
                event.add('summary','Müll ' + row[3])
                cal.add_component(event)
            except:
                pass
    finally:
        f.close()
        
    # write to disk
    f = open(sys.argv[1]+'.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
    
    sys.exit(0)


if __name__ == '__main__':
    main()
