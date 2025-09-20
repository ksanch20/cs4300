#Function to calculate discount applied to price 
def calculate_discount(price, discount):
    #Calculate the discount 
    try:
        discounted_price = price * ((100 - discount)*0.01)
        #Return price rounded to two decimal places 
        return round(discounted_price,2)
    except TypeError:
        raise ValueError("Price and discount must be numeric values")


