# BackEnd EV1
cd agenda_contactos
python -m venv venv
mandar el activate a la terminal
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


si no funciona al iniciar escribir: cd .. y hacer migraciones