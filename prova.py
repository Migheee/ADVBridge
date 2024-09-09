from SuperSaaS import Client
from datetime import datetime

# Initialize the singleton with authorization credentials
Client.instance().configure(
    account_name='mighe',
    api_key='rP9UKDlFKmQy88QArA5VnQ'
)    

# Do API calls
Client.instance().schedules.list()

#Client.instance().users.create(attributes={'name': 'mghcst1@gmail.com', 'full_name': 'Michele Name', 'email': 'mghcst1@gmail.com'}, user_id="1111fk", webhook=True)
appointments = Client.instance().appointments.range(schedule_id=714767, user="1111fk")  #per vedere appuntamenti disponibili
print(appointments)
print("SLOT DISPONIBILI")
#slot = appointments[0]
for slots in appointments:       #per vedere le info degli appuntamenti: Nota, è stato necessario definire la classe in model
    print(slots.get_id())  
    print(slots.get_start())
    print(slots.get_finish())
    print(slots.get_title())
    print(slots.get_description())
    print(slots.get_location())
    print(slots.get_capacity())






a=Client.instance().users.get(user_id="1111fk")#informazioni utente
print(a.__str__())


Client.instance().appointments.create(schedule_id=714767, user_id="1111fk", attributes={'full_name': 'Example Name', 'email': 'mghcst1@gmail.com', 'slot_id': 61074641, 'phone': 1111, "field_1_r": "aa"}, form=True, webhook=True) #per prenotarsi



print("\nINFO APPUNTAMENTO")
c=Client.instance().appointments.agenda_slots(schedule_id=714767, user_id=a.get_name(), from_time=datetime.now())#per vedere le prenotazioni, è necessario definire la classe in model
appuntamento = c[0]
for b in c:
  
    print(b.__str__())


#Client.instance().appointments.delete(schedule_id=714767, appointment_id=appuntamento.get_id(), webhook=True)



