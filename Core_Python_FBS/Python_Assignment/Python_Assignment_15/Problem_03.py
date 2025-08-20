class Shirt:
    def __init__(self,s_id=0,s_name="",s_type="",price=0,s_size=""):
        self.s_id=s_id
        self.s_name=s_name
        self.s_type=s_type
        self.price=price
        self.s_size=s_size

    def __del__(self):
        print("Destructor: ",self.s_name)

    def ShowShirt(self):
        print("Shirt id: ",self.s_id)
        print("Shirt name : ",self.s_name)
        print("Shirt type (formal/printed): ",self.s_type)
        print("Shirt Price : ",self.price)
        print("Shirt size: ",self.s_size)

print("Parameterless constructor ")
obj1=Shirt()
obj1.ShowShirt()

print("Parameterized constructor ")
obj2=Shirt(101,"Cotton","Formal",1000,"XL")
obj2.ShowShirt()