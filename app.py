from flask import Flask , render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
import os
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 


class Recepies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingridents = db.relationship('Ingridents', backref='ingrident') 
    steps = db.relationship('Steps', backref='step') 

class Ingridents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingrident_name = db.Column(db.String(50), nullable=False)
    ingrident_qty = db.Column(db.String(50), nullable=False)
    recepie_id = db.Column(db.Integer, db.ForeignKey('recepies.id'), nullable=False)


class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    step_data = db.Column(db.String(50), nullable=False)
    step_order = db.Column(db.Integer, nullable=False)
    recepie_id = db.Column(db.Integer, db.ForeignKey('recepies.id'), nullable=False)





@app.route('/')
def show_all():
   return render_template('index.html',mytitle="Recipe Diary",recepies = Recepies.query.all(), ingridents = Ingridents.query.all(), steps = Steps.query.all() )




@app.route('/newrecipe')
def newrecipe():
   return render_template('newrecipe.html',mytitle="NEW Recipe")




@app.route('/newingrident',methods = ['GET', 'POST'])
def newingrident():
    
    if request.method == 'GET':
        
        return render_template('newingrident.html', rid2 = request.args.get('rid'))
    
    return redirect(url_for('show_all'))




@app.route('/newcookingstep',methods = ['GET', 'POST'])
def newcookingstep():
    
    if request.method == 'GET':
        
        return render_template('newcookingstep.html', rid2 = request.args.get('rid'))
    
    return redirect(url_for('show_all'))





@app.route('/addnewrecipe', methods = ['GET', 'POST'])
def addnewrecipe():
    if request.method == 'POST':
        recepie2 = Recepies(name=request.form['name']) 
        db.session.add(recepie2)
        db.session.commit()
        return redirect(url_for('show_all'))
    return render_template('index.html',mytitle="Recipe Diary",recepies = Recepies.query.all(), ingridents = Ingridents.query.all(), steps = Steps.query.all() )
    


@app.route('/addnewingrident', methods = ['GET', 'POST'])
def addnewingrident():
    if request.method == 'POST':
        
        
        receipe_ingrident2 = Ingridents(ingrident_name = request.form['name'],ingrident_qty = request.form['qty'], recepie_id = request.form['rid'] )

        db.session.add(receipe_ingrident2)
        db.session.commit()

        return redirect(url_for('show_all'))
    return render_template('index.html',mytitle="Recipe Diary",recepies = Recepies.query.all(), ingridents = Ingridents.query.all(), steps = Steps.query.all() )
    




@app.route('/addnewcookingstep', methods = ['GET', 'POST'])
def addnewcookingstep():
    if request.method == 'POST':
        
        
        receipe_step2 = Steps(step_data = request.form['name'],step_order = request.form['order'], recepie_id = request.form['rid'] )

        db.session.add(receipe_step2)
        db.session.commit()

    return redirect(url_for('show_all'))
    #return render_template('index.html',mytitle="Recipe Diary",recepies = Recepies.query.all(), ingridents = Ingridents.query.all(), steps = Steps.query.all() )
    







@app.route('/deleteingrident', methods = ['GET', 'POST'])
def deleteingrident():
    if request.method == 'POST':
        
        
        #receipe_ingrident2 = Ingridents.query.filter(id==request.form['iid'])
        #receipe_ingrident2 = db.session.query(Ingridents).filter(id==17)
        Ingridents.query.filter_by(id=request.form['iid']).delete()
        #db.session.delete(receipe_ingrident2)
        db.session.commit()

        
    return redirect(url_for('show_all')) 


@app.route('/deletestep', methods = ['GET', 'POST'])
def deletestep():
    if request.method == 'POST':
        
        Steps.query.filter_by(id=request.form['iid']).delete()

        db.session.commit()

        
    return redirect(url_for('show_all')) 


@app.route('/deletreceipe', methods = ['GET', 'POST'])
def deletreceipe():
    if request.method == 'POST':
        
        Ingridents.query.filter_by(recepie_id=request.form['rid']).delete()
        db.session.commit() 
        Steps.query.filter_by(recepie_id=request.form['rid']).delete()
        db.session.commit() 
        Recepies.query.filter_by(id=request.form['rid']).delete()

        db.session.commit() 

    return redirect(url_for('show_all')) 



#export DATABASE_URI=sqlite:///data.db
if __name__=='__main__':
    db.create_all() 
    app.run(debug=True, host='0.0.0.0')

