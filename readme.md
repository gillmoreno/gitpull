
### Microservice in Flask to automate code pulling in server 

This Flask microservice receives a webhook POST request from Github when a new commit is pushed and automatically pulls the new code to the server.

Flask and uwsgi need to be installed on the server (either globally or locally in a virtual environment).

The script gitpull.sh on my server is as follows:


*#!/bin/bash*

*cd path/to/code*

*git pull https://USERNAME:PASSWORD@github.com/USERNAME/REPONAME*

*#Then some code to restart the server... in my case restart docker-compose*

*cd path/to/docker/yml*

*docker-compose down*

*docker-compose up*