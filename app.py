from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

RAZORPAY_KEY_ID=""
RAZORPAY_KEY_SECRET=""

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)

class Product(db.Model):  
    id=db.Column(db.Integer,primary_key=True)
    p_name=db.Column(db.String(20),nullable=False)
    p_price=db.Column(db.Integer,nullable=False)
    p_quantity=db.Column(db.Integer,nullable=False)

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(30),nullable=False)
    message=db.Column(db.String(100),nullable=False)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order")
def order():
    return render_template("orders.html")

@app.route("/product")
def purchase():
    return render_template("product.html")

@app.route("/contact")
def contactus():
    return render_template("contact.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/checkout", methods=['POST'])
def payout():
    return render_template("checkout.html")


if __name__=="__main__":
    app.run(debug=True) 
