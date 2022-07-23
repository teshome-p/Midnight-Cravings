from flask import Flask, render_template, url_for, flash, redirect,request
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = '48103c3f1e535f696813b3bcb1321b7b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

cart_items = []
prices = {"Burger and Fries":15,"Philly Cheesesteak":17,"Hot Wings":15,
        "Gluten Free Vegan Pizza":25, "Beyond Burger on a Gluten Free Bun":15,
        "Chipotle Lentil Tacos":12,"Beyond Beef Tacos":14,"Vegan Nice Cream":9,
        "Vegan Brownies":4,"Vegan Flourless Chocolate Cake":20,"Milkshakes":8,
        "Frozen Yogurt":7,"Ice Cream":5,"Cupcakes":3,"Chocolate Lava Cakes":5,
        "Pepperoni Pizza":20,"Barbecue Chicken Pizza":20,"Meat Lovers Pizza":25,
        "Ground Beef Pizza":20,"Hawaiian Pizza":20,"Veggie Mushroom and Olives Pizza":20,
        "Margherita Pizza":20}

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

@app.route("/cart", methods= ['GET', 'POST'])
def cart():
    if request.method == "POST":
        if request.form.get("purchase button") == "Purchase items":
            price = cart_items[-1]
            cart_items.clear()
            return "<b> Order confirmed\n " + price + " </b>"
    return render_template('cart.html', subtitle='Cart Page', text=", ".join(cart_items))

@app.route("/menu", methods = ['GET','POST'])
def menu():
    if request.method == "POST":
        for name in request.form.keys():
            if name != "view cart":
                cart_items.append(name)
        if request.form.get("view cart") == "View cart":
            total_price = 0
            for name in cart_items:
                total_price += prices[name]
            cart_items.append("Total Price: " + str(total_price))
            return redirect(url_for("cart"))
    return render_template("../templates/menu.html")

@app.route("/home", methods = ['GET','POST'])
def home():
    if request.method == "POST":
        if request.form.get("menu button") == "Go to menu":
            return redirect(url_for('menu'))
    return render_template("home.html")

@app.route("/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
