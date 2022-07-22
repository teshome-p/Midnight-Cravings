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
            cart_items.clear()
            return "<b> Order confirmed </b>"
    return render_template('cart.html', subtitle='Cart Page', text=" ".join(cart_items))

@app.route("/menu", methods = ['GET','POST'])
def menu():
    if request.method == "POST":
        if request.form.get("pizza") == "Add pizza to cart":
            cart_items.append("pizza")
        if request.form.get("item 2") == "Add item 2 to cart":
            cart_items.append("item 2")
        if request.form.get("item 3") == "Add item 3 to cart":
            cart_items.append("item 3")
        if request.form.get("item 4") == "Add item 4 to cart":
            cart_items.append("item 4")
        if request.form.get("view cart") == "View cart":
            return redirect(url_for("cart"))
    return render_template('menu.html', subtitle='Menu',img_1 = "pizza.jpg")

@app.route("/home", methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form.get("menu button") == "Go To Menu":
            return redirect(url_for('menu'))
    return render_template('home.html', subtitle='Home')

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
