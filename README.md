# docker_equipment_site_django_2022

Make a web page with postgres database to track equipment and jobs

To build the docker-compose file use the below code

``` bash
docker-compose up -d --build
```

A container called (web) will be created along with postgres database  and the web page will be running

To do migrations and makemigrations use the command below

``` bash
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py makemigrations
```

To start and stop the container use the below command

``` bash
docker-compose up -d 

docker-compose down
```
