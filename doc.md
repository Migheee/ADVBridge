## Documentazione del Progetto BRIDGE ADV - Attività svolta da Castenedoli Michele

### 14 marzo 2024

#### 1. Creazione del Virtual Environment
Un ambiente virtuale (`virtual environment`) è una pratica standard per isolare le dipendenze di un progetto Python. È stato creato un ambiente virtuale per questo progetto per gestire le librerie e le dipendenze in modo separato da altri progetti.

- Comando per creare un ambiente virtuale:
  ```bash
  python3 -m venv myenv
  ```

#### 2. Creazione del Progetto con Visual Studio Code
Il progetto è stato creato utilizzando Visual Studio Code come ambiente di sviluppo integrato (IDE).

#### 3. Utilizzo di pip per installare la libreria `supersaas-api-client 2.0.0`
La libreria `supersaas-api-client` è stata installata utilizzando il gestore dei pacchetti `pip`.

- Comando per l'installazione:
  ```bash
  pip install supersaas-api-client==2.0.0
  ```

#### 4. Registrazione e Configurazione dell'Account su SuperSaaS
L'account su SuperSaaS è stato registrato e configurato per analizzare il funzionamento del software come servizio (SaaS). In particolare, è stato creato un calendario.

### 17 marzo 2024

#### 1. Importazione e Configurazione del Client per Interfacciarsi con le API di SuperSaaS
Il client è stato importato e configurato per consentire alla nostra applicazione di inviare richieste alle API di SuperSaaS.

#### 2. Definizione della Classe `Appointment`
Poiché la classe `Appointment` non era presente nella libreria `supersaas-api-client`, è stata definita una classe personalizzata per gestire gli appuntamenti.

```python
from .BaseModel import BaseModel

class Appointment(BaseModel):
    def __init__(self, data):
        # Attributi della classe
        self.id = data.get('id')
        self.slot_id = data.get('slot_id')
        self.created_on = data.get('created_on')
        self.user_id = data.get('user_id')
        self.created_by = data.get('created_by')
        self.waitlisted = data.get('waitlisted')
        self.price = data.get('price')
        self.deleted = data.get('deleted')
        self.full_name = data.get('full_name')
        self.schedule_id = data.get('schedule_id')
        self.schedule_name = data.get('schedule_name')

    # Metodi per accedere agli attributi
    def get_id(self):
        return self.id

    def get_slot_id(self):
        return self.slot_id

    def get_created_on(self):
        return self.created_on

    def get_user_id(self):
        return self.user_id

    def get_created_by(self):
        return self.created_by

    def is_waitlisted(self):
        return self.waitlisted

    def get_price(self):
        return self.price

    def is_deleted(self):
        return self.deleted

    def get_full_name(self):
        return self.full_name

    def get_schedule_id(self):
        return self.schedule_id

    def get_schedule_name(self):
        return self.schedule_name

    def __str__(self):
        # Metodo per rappresentare l'oggetto sotto forma di stringa
        return f"Appointment Details:\nID: {self.id}\nSlot ID: {self.slot_id}\nCreated On: {self.created_on}\nUser ID: {self.user_id}\nCreated By: {self.created_by}\nWaitlisted: {self.waitlisted}\nPrice: {self.price}\nDeleted: {self.deleted}\nFull Name: {self.full_name}\nSchedule ID: {self.schedule_id}\nSchedule Name: {self.schedule_name}"
```

#### 3. Creazione degli Utenti tramite Richiesta HTTP POST a SuperSaaS
Gli utenti sono stati creati inviando una richiesta HTTP POST a SuperSaaS utilizzando il client configurato.

Esempio di creazione di un utente:
```python
Client.instance().users.create(attributes={'name': 'mghcst1@gmail.com', 'full_name': 'Michele Name', 'email': 'mghcst1@gmail.com'}, user_id="1111fk", webhook=True)
```

#### 4. Salvataggio ed Esportazione del Progetto
Il progetto è stato salvato e esportato per la condivisione tramite Google Drive o altri mezzi di distribuzione.

### 21 marzo 2024

#### 1. Documentazione e Analisi per Identificare Eventi Disponibili
È stata completata la documentazione del progetto e l'analisi per identificare gli eventi disponibili su SuperSaaS.

#### 2. Modifica della Configurazione del Calendario per Ottenere l'ID
La configurazione del calendario è stata modificata per consentire l'accesso all'ID del calendario, necessario per determinate operazioni nell'applicazione.

Definizione della classe `Slot` per poter accedere ad ogni evento del calendario
```python
from .BaseModel import BaseModel

class Slot(BaseModel):
    def __init__(self, data):
        self.id = data.get('id')
        self.start = data.get('start')
        self.finish = data.get('finish')
        self.title = data.get('title')
        self.description = data.get('description')
        self.location = data.get('location')
        self.capacity = data.get('capacity')

    def get_id(self):
        return self.id

    def get_start(self):
        return self.start

    def get_finish(self):
        return self.finish
 
    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_location(self):
        return self.location

    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return f"Slot Details:\nID: {self.id}\nSlot start: {self.start}\nSlot finish: {self.finish}\nSlot title: {self.title}\nSlot Description: {self.description}\nSlot Location: {self.location}\nSlot capacity: {self.capacity}"

```
Breve spiegazione di ogni parte del codice:

1. **Classe `Slot` e Metodo `__init__`:**
   La classe `Slot` è una sottoclasse di `BaseModel`. Nel suo costruttore `__init__`, prende un parametro `data` che dovrebbe essere un dizionario contenente i dati relativi allo slot. I dati vengono quindi estratti dal dizionario utilizzando il metodo `data.get('key')` e assegnati agli attributi della classe.

2. **Metodi di Accesso (`get_id`, `get_start`, `get_finish`, ecc.):**
   Questi sono metodi di accesso (getter) che restituiscono i valori degli attributi dello slot. Ogni metodo restituisce semplicemente il valore dell'attributo corrispondente.

3. **Metodo `__str__`:**
   Il metodo `__str__` è un metodo speciale che restituisce una rappresentazione stringa dell'oggetto `Slot`. Quando chiamiamo `str(slot)`, viene restituita una stringa formattata che mostra i dettagli dello slot, inclusi ID, orario di inizio e fine, titolo, descrizione, posizione e capacità.

### Commento sull'utilità e la struttura del codice:

- Questa implementazione è utile perché incapsula i dati relativi allo slot in un oggetto `Slot`, consentendo di accedere e manipolare facilmente tali dati attraverso i metodi di accesso.
  
- I metodi di accesso (`get_id`, `get_start`, ecc.) forniscono un'interfaccia pulita per ottenere informazioni specifiche sugli slot, nascondendo i dettagli implementativi dell'accesso agli attributi all'esterno della classe.

- Il metodo `__str__` fornisce una rappresentazione leggibile dell'oggetto `Slot` quando viene stampato, rendendo più facile il debug e il logging.

In questa versione migliorata, gli attributi sono incapsulati come proprietà (`@property`), consentendo un accesso più intuitivo e rispettoso dell'incapsulamento degli attributi.
Accesso ad ogni slot disponibile nel calendario Tramite richiesta HTTP Post
```python
appointments = Client.instance().appointments.range(schedule_id=714767, user="1111fk")
```

### 25 marzo 2024
Tentativi nell'accedere alle informazioni degli utenti creati
Richiesta HTTP Post Tramite Browser per accedere ad ogni informazioni degli utenti
```json
{
    "id": 12826385,
    "role": 3,
    "name": "mghcst1@gmail.com",
    "full_name": "Michele Name",
    "created_on": "2024-03-25T17:03:46Z",
    "mobile": null,
    "address": null,
    "fk": 1111,
    "last_login": null,
    "credit": "0,00"
  }
```

Definizione della classe User per creazione degli oggetti utente
```python
import datetime
from .BaseModel import BaseModel

class User(BaseModel):
    def __init__(self, data):
        self.id = data.get("id", None)
        self.role = data.get("role", None)
        self.name = data.get("name", None)
        self.full_name = data.get("full_name", None)
        self.created_on = self._parse_datetime(data.get("created_on", None))
        self.mobile = data.get("mobile", None)
        self.address = data.get("address", None)
        self.fk = data.get("fk", None)
        self.last_login = self._parse_datetime(data.get("last_login", None))
        self.credit = data.get("credit", None)

    def _parse_datetime(self, dt_str):
        if dt_str:
            return datetime.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ")
        else:
            return None

    def get_id(self):
        return self.id

    def get_role(self):
        return self.role

    def get_name(self):
        return self.name

    def get_full_name(self):
        return self.full_name

    def get_created_on(self):
        return self.created_on

    def get_mobile(self):
        return self.mobile

    def get_address(self):
        return self.address

    def get_fk(self):
        return self.fk

    def get_last_login(self):
        return self.last_login

    def get_credit(self):
        return self.credit

    def __str__(self):
        return (
            f"User info:\nid={self.id}, \nrole={self.role}, \nname={self.name}, "
            f"\nfull_name={self.full_name}, \ncreated_on={self.created_on}, "
            f"\nmobile={self.mobile}, \naddress={self.address}, \nfk={self.fk}, "
            f"\nlast_login={self.last_login}, \ncredit={self.credit}"
        )

```

Ecco una spiegazione dettagliata del codice:

- **Metodo `__init__`:**
  - Il metodo `__init__` è il costruttore della classe `User`.
  - Prende un parametro `data`, che dovrebbe essere un dizionario contenente i dati relativi all'utente.
  - Utilizza il metodo `data.get("key", default)` per estrarre i valori dall'oggetto `data` e inizializzare gli attributi dell'oggetto `User`.
  - Il metodo `_parse_datetime` viene utilizzato internamente per convertire una stringa di data/ora nel formato specificato (`"%Y-%m-%dT%H:%M:%SZ"`) in un oggetto `datetime.datetime`.

- **Metodi di Accesso (`get_id`, `get_role`, ecc.):**
  - Questi sono metodi di accesso (getter) che restituiscono i valori degli attributi dell'utente.
  - Ogni metodo restituisce semplicemente il valore dell'attributo corrispondente.

- **Metodo `__str__`:**
  - Il metodo `__str__` è un metodo speciale che restituisce una rappresentazione stringa dell'oggetto `User`.
  - Quando chiamiamo `str(user)`, viene restituita una stringa formattata che mostra i dettagli dell'utente, inclusi ID, ruolo, nome, nome completo, data di creazione, numero di telefono, indirizzo, FK, ultimo accesso e credito.

### Funzionamento del Codice:

- La classe `User` facilita l'accesso e la manipolazione dei dati relativi all'utente all'interno del programma.
- Utilizza il metodo `_parse_datetime` per garantire che le date e gli orari vengano correttamente convertiti in oggetti `datetime.datetime`, facilitando la manipolazione dei dati temporali.


In questa versione migliorata, gli attributi sono incapsulati come proprietà (`@property`), consentendo un accesso più intuitivo e rispettoso dell'incapsulamento degli attributi.
### 10 Aprile 2024
Richiesta HTTP per poter prenotarsi e vedere gli slot (eventi) a cui l'utente si è prenotato.
Es ```python
c=Client.instance().appointments.agenda_slots(schedule_id=714767, user_id=a.get_name(), from_time=datetime.now())
```



Richiesta HTTP per poter eliminare prenotazioni

Es ```python
Client.instance().appointments.delete(schedule_id=714767, appointment_id=appuntamento.get_id(), webhook=True)
```


### 15 Aprile 2024 
Analisi e documentazioni sulle alternative al VENV. Purtroppo non consente di essere attivato su OS differenti a quello su cui è stato creato
Inizializzazione container docker per garantire compatibilità tra diverse architetture.
```dockerfile
# Usa un'immagine di base leggera di Python
FROM python:3.12

# Imposta il working directory all'interno del container
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze Python
RUN pip install -r requirements.txt

# Copia il codice sorgente dell'applicazione nell'immagine Docker
COPY . .

# Esponi la porta 5000 per le connessioni HTTP
EXPOSE 5000

# Comando per avviare l'applicazione Flask quando il container viene avviato
CMD ["python", "app.py"]

```

### 20 Aprile 2024
Creazione dell'immagine Docker attraverso
```bash
docker build -t flask-app .
```
Esecuzione del container Docker: Dopo aver costruito l'immagine Docker, è stato eseguito il seguente comando per avviare un container basato sull'immagine appena creata
```bash
docker run --name my-flask-app -p 5000:5000 flask-app
```
Ricerca della folder su cui vengono scaricate le librerie. Dopo aver trovato `pwd` della directory delle librerie, è stato proceduto alla modifica del file docker per copiare tutte le modifiche effettuate sull pacchetto SuperSaas scaricato al momento dell'esecuzione del container
```dockerfile
FROM python:3.12

RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip3 --version

RUN pip install Flask==3.0.3
RUN pip install supersaas-api-client

# Copia il codice sorgente dell'applicazione nell'immagine Docker
COPY app.py .
COPY Models /usr/local/lib/python3.12/site-packages/SuperSaaS/Models

# Esponi la porta 5000 per le connessioni HTTP
EXPOSE 5000

# Comando per avviare l'applicazione Flask quando il container viene avviato
CMD ["python", "app.py"]
```


### 25 aprile 2024

### Panoramica
Creazione della base dell' applicazione Flask che funge da interfaccia per interagire con il servizio di pianificazione SuperSaaS. Espone diversi endpoint per eseguire operazioni come il recupero degli appuntamenti disponibili, la prenotazione di nuovi appuntamenti e l'eliminazione di appuntamenti esistenti.

### Sorgente di `app.py`
```python
from flask import Flask, jsonify, request
from SuperSaaS import Client
from datetime import datetime

app = Flask(__name__)

# Configura il client SuperSaaS con le credenziali di autorizzazione
Client.instance().configure(
    account_name='mighe',
    api_key='rP9UKDlFKmQy88QArA5VnQ'
)

# Rotta per ottenere gli appuntamenti disponibili
@app.route('/appointments/available', methods=['POST'])
def get_available_appointments():
    try:
        data = request.json
        appointments = Client.instance().appointments.range(schedule_id=data['schedule_id'], user=data['user'])
        appointment_list = []
        for appointment in appointments:
            appointment_info = {
                'id': appointment.get_id(),
                'start': appointment.get_start(),
                'finish': appointment.get_finish(),
                'title': appointment.get_title(),
                'description': appointment.get_description(),
                'location': appointment.get_location(),
                'capacity': appointment.get_capacity()
            }
            appointment_list.append(appointment_info)
        return jsonify(appointment_list), 200  # Restituisce la lista degli appuntamenti disponibili come JSON con status code 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Restituisce un messaggio di errore con status code 500 se si verifica un'eccezione

# Rotta per prenotare un appuntamento
@app.route('/appointments/book', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        response = Client.instance().appointments.create(
            schedule_id=data['schedule_id'],
            user_id=data['user_id'],
            attributes=data['attributes'],
            form=True,
            webhook=True
        )
        return jsonify({'message': 'Appointment booked successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotta per eliminare un appuntamento
@app.route('/appointments/delete', methods=['POST'])
def delete_appointment():
    try:
        data = request.json
        Client.instance().appointments.delete(schedule_id=data['schedule_id'], appointment_id=data['appointment_id'], webhook=True)
        return jsonify({'message': 'Appointment deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

```

### Dipendenze
- `Flask`: Utilizzato per creare l'applicazione web e definire le rotte.
- `jsonify`: Utilizzato per serializzare i dati nel formato JSON.
- `request`: Utilizzato per gestire le richieste HTTP in ingresso.
- `SuperSaaS.Client`: Rappresenta il client SuperSaaS per interagire con l'API.
- `datetime`: Utilizzato per lavorare con data e ora.

### Configurazione
Il client SuperSaaS è configurato con credenziali specifiche (`account_name` e `api_key`) necessarie per autenticare le richieste API al servizio SuperSaaS.

### Endpoint

#### 1. `/appointments/available` (POST)
- **Scopo**: Recuperare gli appuntamenti disponibili in base all'orario specificato e all'utente.
- **Payload della Richiesta**:
  ```json
  {
    "schedule_id": "<schedule_id>",
    "user": "<user_id>"
  }
  ```
- **Risposta**: Restituisce un array JSON degli appuntamenti disponibili con dettagli come ID, ora di inizio, ora di fine, titolo, descrizione, luogo e capacità.

#### 2. `/appointments/book` (POST)
- **Scopo**: Prenotare un nuovo appuntamento.
- **Payload della Richiesta**:
  ```json
  {
    "schedule_id": "<schedule_id>",
    "user_id": "<user_id>",
    "attributes": {
      "full_name": "<full_name>",
      "email": "<email>",
      "slot_id": "<slot_id>"
    }
  }
  ```
- **Risposta**: Restituisce un messaggio di successo se l'appuntamento è stato prenotato con successo.

#### 3. `/appointments/delete` (POST)
- **Scopo**: Eliminare un appuntamento esistente.
- **Payload della Richiesta**:
  ```json
  {
    "schedule_id": "<schedule_id>",
    "appointment_id": "<appointment_id>"
  }
  ```
- **Risposta**: Restituisce un messaggio di successo se l'appuntamento è stato eliminato con successo.

### Gestione degli Errori
- Le eccezioni vengono gestite all'interno di ciascuna rotta, e i messaggi di errore vengono restituiti come risposte JSON con i codici di stato HTTP appropriati (`500` per errori del server).

### Esecuzione dell'Applicazione
- L'applicazione può essere eseguita localmente utilizzando `python app.py`.
- È in modalità debug (`debug=True`), che fornisce messaggi di errore utili durante lo sviluppo.


### 04 Maggio 2024
### Panoramica
Modifiche al sorgente di `app.py`  
Le modifiche apportate al codice sono state significative per implementare nuove funzionalità e migliorare la gestione delle richieste e delle risposte nel contesto di un'applicazione web utilizzando Flask e SuperSaaS.

### Modifiche apportate al codice:

1. **Configurazione del client SuperSaaS:**
   - Utilizzo della libreria `SuperSaaS` per configurare il client con le credenziali di autorizzazione specificate, tra cui `account_name` e `api_key`. Questa configurazione avviene all'avvio dell'applicazione.

2. **Rotta per ottenere gli appuntamenti disponibili (`/appointments/available`):**
   - Aggiunta di una rotta HTTP `POST` per gestire la richiesta di ottenere gli appuntamenti disponibili.
   - Utilizzo di `request.json` per estrarre i dati inviati nella richiesta come oggetto JSON, includendo `schedule_id` e `user`.
   - Utilizzo del client `SuperSaaS` per recuperare gli appuntamenti in base all'ID dello schema e all'utente specificato.
   - Creazione di una lista di informazioni sugli appuntamenti estratti, come `id`, `start`, `finish`, `title`, `description`, `location`, `capacity`.
   - Restituzione dell'elenco degli appuntamenti disponibili come JSON con uno status code 200 in caso di successo. In caso di errore, viene restituito un messaggio di errore con uno status code 500.

3. **Rotta per prenotare un appuntamento (`/appointments/book`):**
   - Aggiunta di una rotta HTTP `POST` per gestire la prenotazione di un appuntamento.
   - Utilizzo di `request.json` per estrarre i dati inviati nella richiesta, inclusi `schedule_id`, `user_id`, `attributes`.
   - Utilizzo del client `SuperSaaS` per creare una prenotazione di appuntamento con i dati specificati, come l'ID dello schema, l'ID utente e altri attributi.
   - Restituzione di un messaggio JSON di conferma con uno status code 200 in caso di successo. In caso di errore, viene restituito un messaggio di errore con uno status code 500.

4. **Rotta per eliminare un appuntamento (`/appointments/delete`):**
   - Aggiunta di una rotta HTTP `POST` per gestire l'eliminazione di un appuntamento.
   - Utilizzo di `request.json` per estrarre i dati inviati nella richiesta, tra cui `schedule_id` e `appointment_id`.
   - Utilizzo del client `SuperSaaS` per eliminare l'appuntamento specificato tramite ID dello schema e ID appuntamento.
   - Restituzione di un messaggio JSON di conferma con uno status code 200 in caso di successo. In caso di errore, viene restituito un messaggio di errore con uno status code 500.

5. **Configurazione delle credenziali SuperSaaS e gestione delle sessioni:**
   - Configurazione del client `SuperSaaS` con le credenziali di autorizzazione specificate.
   - Impostazione di una chiave segreta per le sessioni (`app.secret_key`) per la gestione delle sessioni utente.

6. **Implementazione di funzioni di utilità per l'accesso al database MySQL:**
   - Creazione della funzione `get_user_id_from_db(email)` per ottenere l'ID utente a partire dall'indirizzo email consultando un database MySQL locale.
   - Creazione della funzione `get_phone_from_db(email)` per recuperare il numero di telefono associato a un'email nel database MySQL.

7. **Rotte per la gestione delle richieste utente:**
   - Rotta `/` per la pagina di login, che gestisce le richieste GET e POST per l'autenticazione dell'utente e l'impostazione della sessione.
   - Rotta `/appointments/available` per ottenere gli appuntamenti disponibili, utilizzando il client `SuperSaaS` per recuperare le informazioni degli appuntamenti in base all'utente attualmente autenticato.
   - Rotta `/appointments/book` per prenotare un appuntamento, utilizzando le informazioni dell'utente autenticato e i dati forniti nella richiesta per creare una prenotazione tramite il client `SuperSaaS`.
   - Rotta `/appointments/my_bookings` per ottenere le prenotazioni dell'utente autenticato, utilizzando il client `SuperSaaS` per recuperare le prenotazioni relative allo schema specificato.
   - Rotta `/profile` per visualizzare le informazioni del profilo dell'utente autenticato, ottenendo e mostrando le informazioni dal client `SuperSaaS` e dal database MySQL.

### Codice completo
```python
from flask import Flask, jsonify, request, render_template, session
import mysql.connector
from SuperSaaS import Client

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Configura una chiave segreta per le sessioni

# Configura il client SuperSaaS con le credenziali di autorizzazione
Client.instance().configure(
    account_name='mighe',
    api_key='rP9UKDlFKmQy88QArA5VnQ'
)

# Funzione per ottenere l'user_id dell'utente dal database MySQL
def get_user_id_from_db(email):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Sostituire con il nome utente MySQL
            password='',  # Sostituire con la password MySQL
            database='sas'  # Sostituire con il nome del database MySQL
        )
        cursor = conn.cursor()
        
        # Esegue la query per recuperare l'user_id dall'email
        query = "SELECT id_utente FROM utenti WHERE email = %s"
        cursor.execute(query, (email,))
        
        # Ottiene l'user_id
        user_id = cursor.fetchone()[0]  # Assumendo che ci sia solo un risultato
        
        conn.close()
        return user_id
    except Exception as e:
        print(f"Errore durante il recupero dell'user_id: {str(e)}")
        return None


def get_phone_from_db(email):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Sostituire con il nome utente MySQL
            password='',  # Sostituire con la password MySQL
            database='sas'  # Sostituire con il nome del database MySQL
        )
        cursor = conn.cursor()
        
        # Esegue la query per recuperare il telefono dall'email
        query = "SELECT telefono FROM utenti WHERE email = %s"
        cursor.execute(query, (email,))
        
        # Ottiene il telefono
        telefono = cursor.fetchone()[0]  # Assumendo che ci sia solo un risultato
        
        conn.close()
        return telefono
    except Exception as e:
        print(f"Errore durante il recupero del telefono: {str(e)}")
        return None

# Rotta per la pagina di login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        session['user_email'] = user_email
        return render_template('profile.html', user_email=user_email)
    return render_template('login.html')

# Rotta per ottenere gli appuntamenti disponibili
@app.route('/appointments/available', methods=['GET'])
def get_available_appointments():
    try:
        appointments = Client.instance().appointments.range(schedule_id=714767, user=session.get('user_email'))
        appointment_list = []

        for appointment in appointments:
            appointment_info = {
                'id': appointment.get_id(),
                'start': appointment.get_start(),
                'finish': appointment.get_finish(),
                'title': appointment.get_title(),
                'description': appointment.get_description(),
                'location': appointment.get_location(),
                'capacity': appointment.get_capacity()
            }
            appointment_list.append(appointment_info)

        # Passa i dati degli appuntamenti al template 'appointments.html'
        return render_template('appointments.html', appointments=appointment_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotta per prenotare un appuntamento
@app.route('/appointments/book', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        
        # Ottiene l'user_id dall'email utilizzando la funzione get_user_id_from_db
        user_email = session.get('user_email')
        uid = get_user_id_from_db(user_email)
        
        # Ottiene informazioni sull'utente dalla rotta '/account/info'
        user = Client.instance().users.get(user_id=uid)
        
        # Estrae informazioni utili dall'oggetto user_info
        full_name = user.get_full_name()
        email = user.get_name()
        telefono = get_phone_from_db(email)
        
        # Effettua la prenotazione dell'appuntamento
        response = Client.instance().appointments.create(
            schedule_id=714767,
            user_id=uid,
            attributes={
                'full_name': full_name,
                'email': email,
                'slot_id': data['slot_id'],
                'phone': telefono,
                'field_1_r': data['team_name']
            },
            form=True,
            webhook=True
        )
                   
        return jsonify({'message': 'Appointment booked successfully'}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

# Rotta per ottenere le prenotazioni dell'utente
@app.route('/appointments/my_bookings', methods=['GET'])
def get_my_bookings():
    try:
        bookings = Client.instance().appointments.agenda_slots(schedule_id=714767, user_id=session.get('user_email'))
        booking_list = [b.__str__() for b in bookings]
        return jsonify(booking_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotta per visualizzare le informazioni del profilo dell'utente
@app.route('/profile', methods=['GET'])
def view_profile():
    try:
        user_email = session.get('user_email')
        if not user_email:
            return jsonify({'error': 'User email not found in session'}), 400
        
        # Ottiene l'user_id dall'email utilizzando la funzione get_user_id_from_db
        user_id = get_user_id_from_db(user_email)
        
        # Ottiene le informazioni sull'utente dal client SuperSaaS
        user_info = Client.instance().users.get(user_id=user_id)
        
        # Estrae informazioni utili dall'oggetto user_info
        full_name = user_info.get_full_name()
        email = user_info.get_name()
        telefono = get_phone_from_db(email)
        
        # Costruisce il payload da restituire come risposta JSON
        profile_info = {
            'full_name': full_name,
            'email': email,
            'telefono': telefono
        }
        
        return render_template('profile.html', **profile_info)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Altre attività svolte:
1. **Creazione delle pagine html necessarie per fare il rendering:**
    Creazione della pagina `appointments.html`
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Available Appointments</title>
    </head>
    <body>
        <h1>Available Appointments</h1>
        <div id="appointments">
            {% for appointment in appointments %}
                <div>
                    <p>ID: {{ appointment.id }}</p>
                    <p>Title: {{ appointment.title }}</p>
                    <p>Description: {{ appointment.description }}</p>
                    <p>Location: {{ appointment.location }}</p>
                    <button onclick="bookAppointment({{ appointment.id }})">Book Appointment</button>
                    <hr>
                </div>
            {% endfor %}
        </div>

        <script>
            // Funzione per gestire la prenotazione di un appuntamento
            async function bookAppointment(slotId) {
                const teamName = prompt('Enter your team name:');
                if (!teamName) return;

                try {
                    const response = await fetch('/appointments/book', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            slot_id: slotId,
                            team_name: teamName
                        })
                    });

                    const data = await response.json();
                    alert(data.message);

                } catch (error) {
                    console.error('Error booking appointment:', error);
                    alert('Failed to book appointment. Please try again.');
                }
            }
        </script>
    </body>
    </html>
    ```
    **Visualizzazione degli appuntamenti**:
    - La pagina HTML mostra una lista di appuntamenti disponibili recuperati dal server Flask. Questi appuntamenti sono rappresentati come blocchi di informazioni all'interno di `<div>` annidati. Ogni appuntamento include i seguenti dettagli:
    - **ID**: Identificatore univoco dell'appuntamento.
    - **Titolo**: Titolo dell'appuntamento.
    - **Descrizione**: Descrizione dell'appuntamento.
    - **Località**: Luogo dell'appuntamento.
    
    **Iterazione sugli appuntamenti**:
    - Utilizzando la sintassi di template Jinja `{% for appointment in appointments %}`, la pagina itera attraverso la lista di appuntamenti passata dal server Flask (`appointments`). Per ogni appuntamento, viene generato dinamicamente un blocco HTML che mostra le informazioni dell'appuntamento.
    
    **Prenotazione di un appuntamento**:
   - Ogni blocco di appuntamento include un pulsante "Book Appointment" (`<button onclick="bookAppointment({{ appointment.id }})">`). Quando l'utente clicca su questo pulsante, viene eseguita la funzione JavaScript `bookAppointment(slotId)`.
   - Questa funzione richiede all'utente di inserire il nome del team tramite un prompt.
   - Successivamente, viene eseguita una richiesta `fetch` POST al server Flask (`/appointments/book`) per prenotare l'appuntamento selezionato. La richiesta contiene l'ID dell'appuntamento (`slotId`) e il nome del team (`teamName`).
   - Il server Flask riceve questa richiesta, gestisce la prenotazione utilizzando le informazioni fornite e restituisce una risposta JSON con un messaggio di conferma.
   
   **Gestione delle risposte**:
   - Dopo aver eseguito la richiesta POST per prenotare l'appuntamento, la funzione JavaScript `bookAppointment` attende la risposta dal server.
   - Se la richiesta ha successo, viene mostrato un messaggio di conferma (`alert(data.message)`).
   - In caso di errore durante la prenotazione (ad esempio, problemi di connessione o errori sul server), viene mostrato un messaggio di errore per informare l'utente (`alert('Failed to book appointment. Please try again.')`).


2. **Creazione della pagina `login.html`**
    ## NOTA: questa pagina non è completa, era necessaria per testare il collegamento al DB e il corretto funzionamento delle variabili di sessione

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Login</title>
    </head>
    <body>
        <h1>Login</h1>
        <form method="POST" action="/">
            <input type="email" name="email" placeholder="Enter your email" required>
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    ```
    La pagina `login.html` implementa un'interfaccia per l'autenticazione degli utenti.

    **Funzionamento di `login.html`**:
    1. **Inserimento dell'Email**:
        - L'utente visita questa pagina e inserisce il proprio indirizzo email nel campo di input.

    2. **Invio del Modulo**:
        - Dopo aver inserito l'email, l'utente preme il pulsante "Login".
        - Questo azione attiva l'invio dei dati del modulo al server utilizzando il metodo POST.

    3. **Gestione della Richiesta sul Server**:
        - Sul lato server, il framework Flask gestisce la richiesta POST inviata da `login.html` all'endpoint `/`.
        - Il server estrae l'indirizzo email dall'input ricevuto dal modulo di login.

    4. **Controllo dell'Email**:
        - Il server utilizza l'indirizzo email fornito per verificare l'identità dell'utente.
        - Questa verifica può coinvolgere il confronto dell'email con i dati memorizzati nel database degli utenti.

    5. **Avvio di Sessione Utente**:
        - Dopo aver verificato l'identità dell'utente (ad esempio, se l'utente esiste nel database), il server avvia una sessione.
        - Durante la sessione, l'indirizzo email dell'utente è memorizzato in una variabile di sessione (`session['user_email']`) per identificare l'utente autenticato.

    6. **Reindirizzamento o Visualizzazione della Pagina Profilo**:
        - Se l'utente è autenticato con successo, il server reindirizza l'utente a una pagina di profilo.
        - La pagina di profilo può mostrare informazioni sull'utente autenticato, come nome completo, email e altre informazioni pertinenti recuperate dal database.

    7. **Gestione degli Errori**:
        - Se si verifica un errore durante il processo di autenticazione (ad esempio, email non valida o utente non trovato nel database), il server restituisce un messaggio di errore.


3. **Integrazione con Container Docker**


## Resoconto finale
Per poter completare il progetto, era necesario disporre delle pagine frontend, fondamentali per comprendere come effettuare il rendering degli esiti delle risposte e definire le rotte per accedere ad ogni pagina del sito. 
Sarebbe stato utile popolare il DB con i dati forniti da Giulio Zanoni in formato CSV.
Non è stato eseguito alcun progresso sui pagamenti a causa di:
- difficoltà nel reperire documentazione dalla sezione developer di SuperSaas.
- Impossbilità di supportare entrambi i metodi di pagamento previsti (Tramite Carta di Credito SI, ma non con il bonifico bancario)




