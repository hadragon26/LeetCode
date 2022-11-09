class StockSpanner:

    def __init__(self):
        self.lst = []
        self.track =[]
        self.length = 0

    def next(self, price: int) -> int:
        temp = 0
        if not self.lst:
            self.track.append(1)
            temp = 1
        else:
            if price<self.lst[-1]:
                self.track.append(1)
                temp = 1
            else:
                temp = 1 + self.track[-1]
                index = self.length - self.track[-1] - 1
                while index>= 0:
                    if self.lst[index] <= price:
                        temp+=1
                        index-=1
                    else:
                        break
                self.track.append(temp)
        #print(self.lst)      
        self.lst.append(price) 
        self.length +=1
        return temp
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)