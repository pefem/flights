from flask import Flask, request
from datetime import datetime
from flights import Flights
import json

flights = Flights()
app = Flask(__name__)


@app.route("/")
def index():
    return "<p> welcome to the flights api </p>"

# returns the list of airports and corresponding code
@app.route("/airports", methods=["GET"])
def get_airports():

    if request.method == "GET":
        response = flights.get_airport_response()

        if response.ok:
            data = response.json()
            airport_list = []
            countries = data['data'][0]['countries']

            for country in countries:
                airports = country['airports']
                for airport in airports:
                    airport_data = airport['airport']
                    airport_details = {
                        "airport_name": airport_data["meaning"],
                        "airport_code": airport_data["code"]
                    }
                    airport_list.append(airport_details)
            output = airport_list
        else:
            # airport details not showing due to status code 403
            return  "<p> unable to get airport details </p>"

        return output

# Return an airport based on the airport code provided
@app.route("/airports/<airport_id>", methods=["GET"])
def get_airport(airport_id):
    
    if request.method == "GET":
        airports = get_airports()
        return [airport for airport in airports if airport["airport_code"] == airport_id]

# returns available flights based on origin, destination and date provided
@app.route("/airports/<origin>/<dest>/<date>", methods=["GET"])
def get_flights(origin, dest, date):
    
    if request.method == "GET":
        try:
            date_value = datetime.strptime(date, '%d-%m-%Y').date()
        except ValueError:
            return "<p> incorrect date format. please enter (dd-mm-yyyy) </p>"
        
        date_value = datetime.strftime(date_value, "%d/%m/%Y")
        flight_details = flights.enter_details(origin, dest, date_value)
        response = flights.get_flight_response(params=flight_details)
        flight_options = []

        if response.status_code == 200:
            try:
                resp_output =  response.json()
                available_flights = resp_output["data"]["journey"]["outbound"]["flights"]

                for flight in available_flights:
                    fare_info = flight["priceInfo"]["fares"][0]

                    flight_info = {
                        "departure_airport": flight["trips"][0]["departure"]["airportCode"],
                        "arrival_airport": flight["trips"][0]["arrival"]["airportCode"],
                        "departure_date_and_time": flight["trips"][0]["departure"]["date"],
                        "arrival_date_and_time": flight["trips"][0]["arrival"]["date"],
                        "flight_number": fare_info["basisCodes"][0]["flightNumber"],
                        "Adult_fare_cost": fare_info["fullPrice"]
                    }
                    flight_options.append(flight_info)
                output = flight_options
            except KeyError:
                output = resp_output["data"]["journey"]["outbound"]["message"]["code"]
        else:
            output = "<p> Unexpected response </p>"
        
        return output

# retrieves the cheapest flight
@app.route("/airports/<origin>/<dest>/<date>/cheap", methods=["GET"])
def get_cheapest(origin, dest, date):

    if request.method == "GET":
        origin_ = origin
        dest_ = dest
        date_ = date
        
        flights = get_flights(origin=origin_, dest=dest_, date=date_)
        flights.sort(key=lambda flight: flight["Adult_fare_cost"])
        return flights[0]





if __name__ == "__main__":
    app.run(debug=True)