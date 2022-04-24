class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.time ={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        route = self.check[id][0]+" "+stationName
        time = t - self.check[id][1]
        
        if route not in self.time:
            self.time[route] = [time]
        else:
            self.time[route].append(time)
            
        del self.check[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        route = startStation + " "+endStation
        
        return sum(self.time[route])/len(self.time[route])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)