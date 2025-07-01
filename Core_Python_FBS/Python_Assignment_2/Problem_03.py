# Convert distant given in feet and inches into meter and centimeter. 

feet = float(input("Enter feet :"))
inches = float(input("Enter inches :"))

meters = (feet * 0.3048) + (inches * 0.0254)
centimeter = meters *100

print(f"Distance into meters : {meters} and Distance into centimeter : {centimeter}")
