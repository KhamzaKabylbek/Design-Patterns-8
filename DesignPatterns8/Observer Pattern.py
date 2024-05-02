class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.investors = []

    def register_investor(self, investor):
        self.investors.append(investor)

    def unregister_investor(self, investor):
        self.investors.remove(investor)

    def update_price(self, price):
        self.price = price
        self.notify_investors()

    def notify_investors(self):
        for investor in self.investors:
            investor.update(self.symbol, self.price)


class Investor:
    def __init__(self, name):
        self.name = name
        self.stocks = []

    def update(self, symbol, price):
        print(f"{self.name} received an update: {symbol} price is now {price}")

    def invest_in_stock(self, stock):
        self.stocks.append(stock)
        stock.register_investor(self)

    def divest_from_stock(self, stock):
        self.stocks.remove(stock)
        stock.unregister_investor(self)

if __name__ == "__main__":
    apple_stock = Stock("NIKE", 160.0)
    google_stock = Stock("ADIDAS", 3000.0)

    investor1 = Investor("Sultan")
    investor2 = Investor("Khamza")

    investor1.invest_in_stock(apple_stock)
    investor2.invest_in_stock(google_stock)

    apple_stock.update_price(165.0)
    google_stock.update_price(3100.0)

    investor1.divest_from_stock(apple_stock)

    apple_stock.update_price(170.0)
    google_stock.update_price(3200.0)
