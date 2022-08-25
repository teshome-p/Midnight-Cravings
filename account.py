from flask import Flask, render_template, url_for, flash, redirect,request, Markup
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = '48103c3f1e535f696813b3bcb1321b7b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

cart_items = [] # Used to store the items a user adds to their cart

prices = {"Burger and Fries":15,"Philly Cheesesteak":17,"Hot Wings":15,
        "Gluten Free Vegan Pizza":25, "Beyond Burger on a Gluten Free Bun":15,
        "Chipotle Lentil Tacos":12,"Beyond Beef Tacos":14,"Vegan Nice Cream":9,
        "Vegan Brownies":4,"Vegan Flourless Chocolate Cake":20,"Milkshakes":8,
        "Frozen Yogurt":7,"Ice Cream":5,"Cupcakes":3,"Chocolate Lava Cakes":5,
        "Pepperoni Pizza":20,"Barbecue Chicken Pizza":20,"Meat Lovers Pizza":25,
        "Ground Beef Pizza":20,"Hawaiian Pizza":20,"Veggie Mushroom and Olives":20,
        "Margherita Pizza":20}

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Handles the cart page, and checks if the user wants to purchase their selected items
@app.route("/cart", methods= ['GET', 'POST'])
def cart():
    if request.method == "POST":
        if request.form.get("purchase button") == "Purchase items":
            try:
                price = cart_items[-1]
            except:
                price = "Total Price: 0$"
            cart_items.clear()
            return "<b> Order confirmed <br> " + price + " </b>"
    return render_template('cart.html', subtitle='Cart Page', text=", ".join(cart_items))

# Handles the menu page, and checks if the user selects an item from the menu, and checks if they want to view the cart
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
            cart_items.append("Total Price: " + str(total_price) + "$")
            return redirect(url_for("cart"))
    return render_template("menu.html")

# Handles the home page, and checks if the user selects the button to go to the menu
@app.route("/home", methods = ['GET','POST'])
def home():
    if request.method == "POST":
        if request.form.get("menu button") == "Go to menu":
            return redirect(url_for('menu'))
    return render_template("home.html")

# Handles the page for creating an account
@app.route("/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
      if request.method == 'POST' and form.validate():
        username = request.form.get('username')
        email = request.form.get('email')
        user = User.query.filter_by(username=username).first()
        another_user = User.query.filter_by(email=email).first()
        print(user, another_user)
        if user: # if a user is found, we want to redirect back to signup page so user can try again
            message = Markup("<h4>Username already taken. Click <a href='/login'>here</a> to login <br> Click <a href='/'>here</a> to sign-up with a different username</h4>")
            flash(message)
            return render_template('blank.html')
        elif another_user: # if a user is found, we want to redirect back to signup page so user can try again
            message = Markup("<h4>Email already used. Click <a href='/login'>here</a> to login <br> Click <a href='/'>here</a> to sign-up with a different email</h4>")
            flash(message)
            return render_template('blank.html')
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        #flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Sign-Up', form=form)

# Handles the page for logging in when you already have an account
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_name = request.form.get('username')
        user = User.query.filter_by(username=user_name).first()
        #if not user or not user.password:
        if request.form['username'] != user.username or request.form['password'] != user.password:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
