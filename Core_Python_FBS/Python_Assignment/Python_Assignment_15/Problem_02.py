class Product:
    def __init__(self,p_id=0,p_name="",price=0,quantity=0):
        self.p_id=p_id
        self.p_name=p_name
        self.price=price
        self.quantity=quantity
    def __del__(self):
        print("Destructor called for : ",self.p_name)
    def ShowProduct(self):
        print("product_id: ",self.p_id)
        print("product_name: ",self.p_name)
        print("price: ",self.price)
        print("quantity: ",self.quantity)

print("Parameterized constructor ")
obj1=Product(101,"Book",100,2)
obj1.ShowProduct()

print("Parameterless constructor ")
obj2=Product()
obj2.ShowProduct()