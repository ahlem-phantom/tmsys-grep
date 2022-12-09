#!/bin/bash
docker-compose exec web python main.py db init
docker-compose exec web python main.py db migrate
docker-compose exec web python main.py db upgrade