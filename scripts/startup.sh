cd pokedex
sleep 120
python3 manage.py makemigrations pokedex
python3 manage.py migrate pokedex
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
python3 manage.py search_index --rebuild -f
python3 manage.py runsslserver --certificate /etc/letsencrypt/live/pokedex.automateyournetwork.ca/fullchain1.pem --key /etc/letsencrypt/live/pokedex.automateyournetwork.ca/privkey1.pem 0.0.0.0:8000
