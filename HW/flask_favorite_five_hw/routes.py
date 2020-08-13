from july_blog import app
from flask import render_template

# Home Route
@app.route('/')
def  home():
    customer_name = "Mike"
    order_number = 1
    item_dict = {1: "Ice Cream", 2: "Bread", 3:"Lemons", 4: "Cereal"}
    return render_template("home.html", customer_name=customer_name, order_number = order_number, item_dict = item_dict)

#Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")