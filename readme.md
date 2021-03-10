#Django App

Wagtail CMS

## Installation
- Install Docker
- Clone repo
- Create .env file
- `docker-compose build`
- `docker exec -it [container-id] python manage.py migrate`

## Development
- `docker-compose up`
- `docker ps`
- `docker exec -it [container-id] python manage.py yarn start-webpack`

# Infrastructure
Create a DigitalOcean app and a Space for storing the static files.
Create a Postgres DB.
##Run command
`gunicorn --worker-tmp-dir /dev/shm mhoapp.wsgi`

## Deployment to Digital Ocean
- git push master

# Build with
Django: https://docs.djangoproject.com/
Wagtail CMS: https://docs.wagtail.io/
Forum: https://django-machina.readthedocs.io/en/stable/index.html
Live Styleguide: https://github.com/torchbox/django-pattern-library
TailwindCSS: https://tailwindcss.com/
Webpack: https://webpack.js.org/
PostCSS: https://postcss.org/