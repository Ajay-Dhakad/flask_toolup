from flask import Flask,request,render_template,redirect,flash,session
from flask_sqlalchemy import SQLAlchemy
import random
import bcrypt
import requests



app=Flask(__name__)

app.secret_key='ghjklkjhgcvbn678"?|>KB'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

db=SQLAlchemy(app)

class Messages(db.Model):
    id=key=db.Column('id',db.Integer,primary_key=True)
    key=db.Column('key',db.String(50),nullable=False,unique=True)
    name=db.Column('name',db.String(50),nullable=False)
    message=db.Column('message',db.String(500),nullable=False)


with app.app_context():
    db.create_all()






#homepage
@app.route('/')

def home():
    return render_template("home.html")





#generate passwords

@app.route('/generate_password',methods=['GET','POST'])
def gen_password():


    a="abcdefghijklmnopqrstuvwxyz"
    b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c="1234567890"
    d="!@#$%^&*_+%"
    pswd=a+b+c+d

    if request.method == 'POST':
        len = request.form.get('length')

        if len:
            password = "".join(random.sample(pswd, int(len)))
            return render_template('password.html', password=password)

        # If the user didn't provide input for length, flash an error message.
       # flash('Please enter a valid password length.', 'error')
        

    return render_template('password.html')
        



@app.route('/endencrypt')
def endecrypt():
    return render_template('endecrypt.html')


@app.route('/encryptor',methods=['GET','POST'])

def encrypt_msg():

    if request.method=='POST':
       
       name=request.form.get('name')
       message=request.form.get('message')

       key=bcrypt.hashpw(name.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
       key=key[::-1]
       key=key[0:7]


       entry=Messages(name=name,message=message,key=key)
       
       db.session.add(entry)
       db.session.commit()

       return render_template('encryptor.html',key=key)






    return render_template('encryptor.html')


@app.route('/decryptor',methods=['GET','POST'])

def decrypt_msg():

    

    if request.method =='POST':

        key=request.form.get('key')

        message=Messages.query.filter_by(key=key).first()

        if message:
            
            return render_template('decryptor.html',message=message)
        
            
            

        flash('No messages found with this key 😐','error')
    


    return render_template("decryptor.html")


@app.route('/iptracker',methods=['GET','POST'])
def iptracker():
    if request.method=="POST":
        ip=request.form.get('ip')
        track=requests.get(f'http://ip-api.com/json/{ip}').json()

        if track['status']=='success':
            country=track['country']
            region=track['regionName']
            city=track['city']
            zip=track['zip']
            isp=track['isp']
            data=True

            return render_template('iptracker.html',country=country,region=region,city=city,zip=zip,isp=isp,data=data)
        else:
            flash('Enter a Valid IP...')

    return render_template('iptracker.html')
    



if __name__=='__main__':
    app.run(host=('0.0.0.0'),port=('5000'))