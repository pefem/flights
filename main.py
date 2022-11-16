from flask import Flask, request, jsonify
from datetime import datetime
from flights import Flights

flight = Flights()
app = Flask(__name__)

@app.route("/travel/<origin>/<dest>/<date>", methods=["GET"])
def get_flights(origin, dest, date):
    
    if request.method == "GET":
        try:
            date_value = datetime.strptime(date, '%d-%m-%Y').date()
        except ValueError:
            return  "<p> incorrect date format. please enter (dd-mm-yyyy) </p>"
        
        date_value = datetime.strftime(date_value, "%d/%m/%Y")
        flight_details = flight.enter_details(origin, dest, date_value)
        response = flight.get_response(params=flight_details)
        if response.status_code == 200:
            resp_output =  jsonify(response.json())
        else:
            resp_output = "<p>Unexpected response</p>"
        
        return resp_output



if __name__ == "__main__":
    app.run(debug=True)