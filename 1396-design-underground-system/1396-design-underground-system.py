class UndergroundSystem:

    def __init__(self):
        self.travel_times = defaultdict(list) # {"AB": [10,14,11]}
        self.checkins = {} # contains the check-in station {"id": station_name}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, end_station_name: str, end_time: int) -> None:
        start_station_name, start_time = self.checkins.pop(id)
        route_name = start_station_name + "-" + end_station_name
        self.travel_times[route_name].append(end_time - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route_name = startStation+"-"+endStation
        times = self.travel_times[route_name]
        return sum(times) / len(times)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)