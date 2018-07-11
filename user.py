

class userData():

    def __init__(self,name,bal,stock,cash,wcash):
        self.name = name
        self.bal = bal
        self.stock = stock
        self.cash = cash
        self.wcash = wcash

    def getName(self):
        return self.name

    def getCash(self):
        return self.cash
    def getBalance(self):
        return self.bal
    def getStocks(self):
        return self.stock
    def getWCash(self):
        return self.wcash



class Stock():
    
    def __init__(self,name,ticker,price,stockopen,stockclose):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.open = stockopen
        self.close = stockclose

    def getName(self):
        return self.name
    def getTicker(self):
        return self.ticker
    def getPrice(self):
        return self.price
    def getOpen(self):
        return self.open
    def getClose(self):
        return self.close
    def setPrice(self,newPrice):
        self.price = newPrice
    def setOpen(self,newOpen):
        self.open = newOpen
    def setClose(self,newClose):
        self.close = newClose
    
class StockData():
    def __init__(self,lst):
        self.stocks= lst

    def __iter__(self):
        return self.stocks
    
