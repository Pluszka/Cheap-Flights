class FlightData:
    def __init__(self, price, start, start_airport, destination, destination_airport,
                 start_date, end_date, stop_overs=0, via_city=""):
        self.price = price
        self.start = start
        self.start_airport = start_airport
        self.destination = destination
        self.destination_airport = destination_airport
        self.start_date = start_date
        self.end_date = end_date
        self.stop_overs = stop_overs
        self.via_city = via_city
