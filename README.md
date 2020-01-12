# MyTickets
 Hausübung 2 in SWENGS (IMA17 Semester 5)

Die Idee hinter MyTickets ist ein Ticketsystem, wie es eine IT-Firma nutzen könnte.
Derzeit wird jeglicher Content des Tickets über ein Textfeld abgebildet.

Backend:
Umgesetzt sind 4 Models

- Country (letztendlich nur im Hintergrund als Attribut von Company)
- Company
- Person
- Ticket

Unter myTickets/fixtures gibt es Beispieldaten.
Folgende Befehle sind daher nötig:

- python manage.py createsuperuser
- python manage.py loaddata myTickets/fixtures/initial_data.json


Frontend:
- Login/Logout/Guards
- Tickets (list, create, update, delete)
- Personen (list, create, update, delete)

Custom Validatoren:
- Ticket.Content darf keine linefeeds enthalten
- Person.First_name und Person.Last_name darf keine Zahlen enthalten

Externe Komponente:
- Inputswitch in Person.Internal  (Boolean: Ist Person aus eigener Company oder nicht?)
https://primefaces.org/primeng/#/inputswitch


Ich hoffe, ich habe durch Git keine wichtigen Dateien verloren.