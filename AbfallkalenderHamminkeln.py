# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 12:27:48 2014

@author: Sebastian Held <sebastian.held@gmx.de>
"""

"""
Dieses Programm erzeugt eine iCalendar Datei, die die Müll-Abholtage enthält.

Auf https://www.mywastewatcher.de/abfallkalender/ die eigene Straße einstellen und
eine csv-Datei erzeugen lassen (Abfallkalender_Hamminkeln.csv).

Die csv-Datei beginnt wie folgt:

```
Farbe;Abfallart;Abfuhrtag;Wochentag;V;Bemerkung
rot;SC;04.01.2017;Mittwoch;;
grau;RA;05.01.2017;Donnerstag;;
```

Aufruf des Programmes:
python AbfallkalenderHamminkeln.py gridAbfuhrtermine.csv
es wird die Datei gridAbfuhrtermine.csv.ics erzeugt.
Diese Datei kann auf eine ownCloud hochgeladen werden und dann per Klick in
den Kalender importiert werden.
"""


import sys
import uuid

# tested with icalendar-3.8.4 from http://icalendar.readthedocs.org
from icalendar import Calendar, Event

from datetime import datetime, timedelta
import csv

def main():
    
    # create calendar
    cal = Calendar()
    cal.add('version','2.0')
    cal.add('prodid','-//Ingenieurbüro Held//AbfallkalenderHamminkeln_Python_import//DE')

    f = open(sys.argv[1], mode='rt', encoding='iso-8859-1')
    try:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            #print(row)
            try:
                try:
                    datum = datetime.strptime(row[2],'%d.%m.%y')
                except:
                    datum = datetime.strptime(row[2],'%d.%m.%Y')
                #print(datum)
                event = Event()
                event.add('dtstamp',datetime.now())
                event.add('dtstart',datum.date())
                # ownCloud is broken, it needs a dtend property
                event.add('dtend',(datum + timedelta(days=1)).date())
                event.add('summary','Müll ' + row[0])
                # rfc5545 corrects the specification to require uid
                event.add('uid',uuid.uuid4().hex);
                event.add('description',row[5].strip())
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
