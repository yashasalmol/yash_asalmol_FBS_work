class Television:
    def __init__(self,module_number=0,screen_size=0,price=0):
        self.module_number = module_number
        self.screen_size = screen_size
        self.price = price

    def accept_input(self):
        try:
            self.module_number = int(input("Enter module number: "))
            self.screen_size = int(input("Enter screen size: "))
            self.price = int(input("Enter price: "))

            if len(str(self.module_number)) > 4:
                raise ValueError("Model number cannot be more than 4 digits")
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen Size must be 12 and 70 inches")
            if self.price < 0 or self.price > 5000:
                raise ValueError("Price must be between 0 to 5000")

        except:
            print("Invalid input resetting all values to 0")
            self.module_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("module number: ",self.module_number)
        print("screen size: ",self.screen_size)
        print("Price: Rs",self.price)
    
tv = Television()
tv.accept_input()
tv.display()