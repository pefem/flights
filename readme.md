# Flights api
This is a simple api which allows the user to request available flights(one way) based on a request being made.

## how to make a request
To make a request simply add the following to the request url: origin, destination and date. see example below
* http://127.0.0.1:5000/travel/{origin}/{destination}/{dd-mm-yyyy}
* for the purposes of this Demo please use "LON" as origin airport and "BHD" as destination airport and a date of your choice in the right format. 

## how to run app
You can run this app either by cloning from the git repo provided below or by pulling it from dockerhub(see link below)
* git repo - https://github.com/pefem/flights
* dockerhub - efemp/flight_api