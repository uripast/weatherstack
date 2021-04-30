# weatherstack
Checks current weather using open api and python

WeatherStack documentation: https://weatherstack.com/documentation

Currently supported:
- [Current Weather](https://weatherstack.com/documentation#current_weather) 
- reads json from weatherstack
- inserting to sqlite data table
- querying from sqlite data table
- wrapping the paramaters using config.py
- used requriments file to check all imported libraries
- added dockerfile to run from outside run this two commands:
- docker build -t weatherstack .
- docker run -it --rm --name weatherstack weatherstack
