from abc import ABC, abstractmethod


class firm(ABC):
    def __init__(self, model, price, accessory):
        self.model = model
        self.price = price
        self.accessory = accessory

    @abstractmethod
    def info(self):
        pass


class AMD(firm):
    __nameFirm = "AMD"
    def info(self):
        print(f"This is an AMD {self.model} {self.accessory}, it costs {self.price}. This firm has a red logo.")


class Intel(firm):
    __nameFirm = "Intel"
    def info(self):
        print(f"This is an Intel {self.model} {self.accessory}, it costs {self.price}. This firm has a blue logo.")


firm1 = AMD("Ryzen 9 5900X OEM", 30000, "video card")
firm2 = Intel("Core i7-10700", 20000, "CPU")
for i in (firm1, firm2):
    i.info()
