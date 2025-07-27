product_id = 456789  #int

product_name = "Nike Air Max Running Shoes"  #string

price = 7999.00  #float
 
categories = ["Footwear", "Running Shoes", "Men"]  #list

stock_details = (200, 150) #available, sold (tuple)

discount_percentage = 25.0  #float percentage
 
product_features = {"Air Cushion", "Breathable Fabric", "Rubber Sole"}  #set
 
supplier_details = {
     "name": "Nike India Pvt Limited", "contact": "1800-102-6453",  
     "location": "Hyderabad" }  #dict
 
# Display product details using different formatting methods
 
print("Product ID, Name, Price:", product_id, product_name, price, sep=',')

 
print("Product Discount: %.2f%%" % discount_percentage)

 
print(f"Product Name: {product_name}")

print(f"Price: {price}")

print(f"Discount: {discount_percentage}%")

print(f"Stock Available: {stock_details[0]} units")

 
print("Supplier Details: Name - {0}, contact - {1}, Location - {2}".format(
    supplier_details["name"],
     supplier_details["contact"],
     supplier_details["location"]
    ))

