## Prerequisites

1. Install Docker-compose.
2. Install Python3
3. Install pgadmin4 (optional)

installations at my machine
1. OS: Ubuntu 20.04.4 LTS
2. Docker version 20.10.7, build 20.10.7-0ubuntu5~20.04.2
3. Docker-Compose version v2.4.1

## Local Development with Docker

optional
```bash
python3 -m venv env && source env/bin/activate 
```

run first time with --build.

```bash
sudo docker-compose up --build
```

run for start project
```bash
sudo docker-compose up
```

run for down containers

```bash
sudo docker-compose down
```

### Run dev server

This will run server on [http://localhost:8001](http://localhost:8001)


### Create superuser

Enter in container 
```bash
sudo docker exec -it code-graphers-assessment-web-1 /bin/bash

```

you can create initial super-user with next commad in the container:

```bash
./manage.py createsuperuser
```

## API Docs
login by visiting this [link](http://localhost:8001). 

API documentation is automatically generated using Swagger. You can view documention by visiting this [http://localhost:8001/docs](http://localhost:8001/docs).


## run unit tests
Enter in container 
```bash
sudo docker exec -it code-graphers-assessment-web-1 /bin/bash

```

in the container run pytest

```bash
pytest
```
