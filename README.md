# weatherstack
Checks current weather using open api and python

WeatherStack documentation: https://weatherstack.com/documentation

Currently supported:
- [Current Weather](https://weatherstack.com/documentation#current_weather) 
- reads json from weatherstack and import to a file
- insert to sqlite data table
- querying from sqlite data table
- wrapping the paramaters using config.py
- used requriments file to check all imported libraries
- use main to control the run
- add test to every function with the unittest lib
- added dockerfile to run from outside run this two commands:
- docker build -t weatherstack .
- docker run -it --rm --name weatherstack weatherstack
