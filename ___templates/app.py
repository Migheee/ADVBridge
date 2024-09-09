from flask import Flask, jsonify, request, render_template, session, redirect
import mysql.connector
from flask_caching import Cache

from flask import render_template
from datetime import datetime
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


# Middleware per disabilitare la cache
@app.after_request
def add_header(response):
    """
    Aggiunge gli header per disabilitare la cache nelle risposte HTTP.
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response



# Rotta per la pagina di login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        session['user_email'] = user_email
        return redirect('/profile')
    return render_template('login.html')



# Rotta per ottenere gli appuntamenti disponibili
@app.route('/appointments/available', methods=['GET'])
def get_available_appointments():
    try:
        appointments = Client.instance().appointments.range(schedule_id=714767, user=session.get('user_email'))
        appointment_list = []

        for appointment in appointments:
            start_datetime = datetime.strptime(appointment.get_start(), '%Y-%m-%dT%H:%M')
            finish_datetime = datetime.strptime(appointment.get_finish(), '%Y-%m-%dT%H:%M')

            appointment_info = {
                'id': appointment.get_id(),
                'title': appointment.get_title(),
                'description': appointment.get_description(),
                'location': appointment.get_location(),
                'start': start_datetime.strftime('%d-%m-%Y %H:%M'),
                'finish': finish_datetime.strftime('%d-%m-%Y %H:%M'),
                'capacity': appointment.get_capacity()
            }
            appointment_list.append(appointment_info)

        return render_template('appointments.html', appointments=appointment_list)

    except Exception as e:
        print(e)
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

@app.route('/appointments/my_bookings', methods=['GET'])
def get_my_bookings():
    try:
        user_email = session.get('user_email')
        if not user_email:
            return jsonify({'error': 'User not authenticated.'}), 401
        
        # Richiedi le prenotazioni dell'utente
        bookings = Client.instance().appointments.agenda_slots(schedule_id=714767, user_id=user_email)
        
        # Prepara i dati per la visualizzazione in HTML
        appointment_list = []
        for booking in bookings:
            created_on_iso = booking.get_created_on()  # Assuming get_created_on() returns ISO 8601 datetime string
            
            # Utilizza datetime.strptime() per convertire la stringa datetime nel formato corretto
            created_datetime = datetime.strptime(created_on_iso, '%Y-%m-%dT%H:%M:%SZ')
            
            # Formatta la data nel formato desiderato ('%d-%m-%Y %H:%M')
            formatted_created_on = created_datetime.strftime('%d-%m-%Y %H:%M')
            
            appointment = {
                'schedule_name': booking.get_schedule_name(),
                'created_on': formatted_created_on,
                'id': booking.get_id(),
            }
            appointment_list.append(appointment)
        
        print(appointment_list)
        return render_template('my_appointments.html', appointments=appointment_list), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rotta per visualizzare le informazioni del profilo dell'utente
@app.route('/profile', methods=['GET'])
def view_profile():
    try:
        user_email = session.get('user_email')
        if not user_email:
            return jsonify({'error': 'User email not found in session'}), 400
        
        # Ottieni l'user_id dall'email utilizzando la funzione get_user_id_from_db
        user_id = get_user_id_from_db(user_email)
        
        # Ottieni le informazioni sull'utente dal client SuperSaaS
        user_info = Client.instance().users.get(user_id=user_id)
        
        # Estrai le informazioni utili dall'oggetto user_info
        full_name = user_info.get_full_name()
        email = user_info.get_name()
        telefono = get_phone_from_db(email)
        
        # Assicurati che i dati siano correttamente estratti
        if not full_name or not email or not telefono:
            return jsonify({'error': 'User data not found'}), 404
        
        # Passa le informazioni dell'utente al template
        return render_template('profile.html', full_name=full_name, email=email, telefono=telefono)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/appointments/delete', methods=['POST'])
def delete_appointment_api():
    try:
        # Assicurati che l'utente sia autenticato
        user_email = session.get('user_email')
        if not user_email:
            return jsonify({'error': 'User not authenticated.'}), 401
        
        # Ottieni l'ID dell'appuntamento da eliminare dalla richiesta JSON
        data = request.json
        appointment_id = data['appointment_id']  # Assumendo che 'appointment_id' sia incluso nei dati della richiesta
        print(f"Appointment ID to delete: {appointment_id}")
        
        # Effettua la cancellazione dell'appuntamento utilizzando il metodo 'DELETE' del client SuperSaaS
        Client.instance().appointments.delete(schedule_id=714767, appointment_id=appointment_id, webhook=True)
        
        return jsonify({'message': 'Appointment deleted successfully'}), 200
    
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/account/create', methods=['POST'])
def create_account():
    try:
        data = request.json  # Assumendo che i dati siano inviati come JSON

        # Estrai i dati necessari dalla richiesta
        name = data['name']
        full_name = data['full_name']
        email = data['email']
        # Altri dati che potresti avere bisogno di estrarre

        # Crea l'utente utilizzando il client SuperSaaS
        response = Client.instance().users.create(
            attributes={
                'name': email,
                'full_name': full_name,
                'email': email,
                
            },
            user_id="1112fk"
            webhook=True
        )

        return jsonify({'message': 'Account created successfully'}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
