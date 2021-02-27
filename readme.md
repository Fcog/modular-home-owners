#Django App

Wagtail CMS

##Installation
- Install Docker
- Clone repo
- Create .env file
- `docker-compose build`
- `docker exec -it [container-id] python manage.py migrate`

##Development
- `docker-compose up`
- `docker ps`
- `docker exec -it [container-id] python manage.py tailwind start`

#Deployment
- git push master

#Infrastructure
Create a DigitalOcean app and Space. Uses a Postgres DB.
##Run command
`gunicorn --worker-tmp-dir /dev/shm mhoapp.wsgi`