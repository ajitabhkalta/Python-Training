import logging

logging.basicConfig(level=logging.CRITICAL)

class Dosa():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logging.debug("Dosa object created: {} (INR-{})".format(self.name, self.price))
        #print("Dosa object created: {} (INR-{})".format(self.name, self.price))
        #By using print stmt we can't turn off printing 

    def make(self, quantity):
        logging.info(f"Made {quantity} {self.name} Dosa(s)")
        #print(f"Made {quantity} {self.name} Dosa(s)")
        #By using print stmt we can't turn off printing 

    def pack(self, quantity):
        logging.warning(f"Packed {quantity} {self.name} Dosa(s)\nBill:{quantity*self.price}")
        #print(f"Packed {quantity} {self.name} Dosa(s)\nBill:{quantity*self.price}")
        #By using print stmt we can't turn off printing 
        
Dosa1 = Dosa("Masala", 15)
Dosa1.make(3)
Dosa1.pack(3)

Dosa2 = Dosa("Onion", 12)
Dosa2.make(2)
Dosa2.pack(2)