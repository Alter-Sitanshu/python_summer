from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, Length
from flask import Flask, render_template, request, redirect, url_for
import json
from json.decoder import JSONDecodeError

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder":"Name"})
    loc = URLField('Location URL', validators=[DataRequired()], render_kw={"placeholder":"Location URL"})
    opening = TimeField('Opening Time', validators=[DataRequired()])
    closing = TimeField('Closing Time', validators=[DataRequired()])
    coffee = SelectField('Coffe Rating', validators=[DataRequired()], choices=[1,2,3,4,5])
    wifi = SelectField('Wifi Rating', validators=[DataRequired()], choices=[1,2,3,4,5])
    submit = SubmitField('Submit', validators=[DataRequired()], render_kw={"class":"submit"})

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hallabol'  # Replace with your actual secret key

@app.route("/add", methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if request.method=="POST":
        name = form.name.data
        loc = form.loc.data
        opening = str(form.opening.data)
        closing = str(form.closing.data)
        coffee = str(form.coffee.data)
        wifi = str(form.wifi.data)
        data_update = {name:{"name":name, "loc":loc, "opening":opening, "closing":closing, "coffee":coffee, "wifi":wifi}}
        print(data_update)
        try:
            with open('coffee_website\static\data.json', 'r') as file:
                data = json.load(file)
                data.update(data_update)
        except JSONDecodeError:
            with open('coffee_website\static\data.json', 'w') as file:
                json.dump(data_update, file, indent=4)
        except FileNotFoundError:
            with open('coffee_website\static\data.json', 'w') as file:
                json.dump(data_update, file, indent=4)
        else:
            with open('coffee_website\static\data.json', 'w') as file:
                json.dump(data, file, indent=4)
        
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
    try:
        with open('coffee_website\static\data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return render_template('data.html', data = data)
if __name__ == "__main__":
    app.run(debug=True)