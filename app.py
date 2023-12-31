from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, Form, FormField, FieldList
from wtforms.validators import InputRequired, Length, AnyOf, Email
from collections import namedtuple


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecret!'


class YearForm(Form):
    year = IntegerField('Year')
    total = IntegerField('Total')

class TelephoneForm(Form):
    country_code = StringField('Country code:')
    area_code = IntegerField('Area code')
    number = StringField('number')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[
        InputRequired(),
        Length(min=5, max=10, message='Wrong lenght of login'),
    ])
    password = PasswordField('password', validators=[
        InputRequired(),
        Length(min=3, max=10, message='kwiksimus'),
        AnyOf(['kwoka', 'psiocha'])
    ])

    age = IntegerField('Age', default=14)
    yes_no = BooleanField(default=True)

    email = StringField('email', validators=[
        Email()
    ])

class NameForm(LoginForm):
    first_name = StringField('1st Name')
    second_name = StringField('2nd Name')
    home_phone = FormField(TelephoneForm)
    mobile_phone = FormField(TelephoneForm)
    years = FieldList(FormField(YearForm), min_entries=3)

class User():
    def __init__(self, username, age, email) -> None:
        self.username = username
        self.age = age
        self.email = email




    @app.route('/', methods = ['POST', 'GET'])
    def index():

       

        group = namedtuple('Group', ['year', 'total'])
        g1 = group(2020, 100)
        g2 = group(2021, 200)
        g3 = group(2022, 300)

        data = {'years' : [g1, g2, g3]}

        User_sylwek = User(username='Stalonek', age=32, email='cykor13@gmail.com')
        form = NameForm(obj=User_sylwek, data=data)

        if form.validate_on_submit():
            # return f'Home Phone area code: {form.home_phone.area_code.data} and Mobile area code is: {form.mobile_phone.area_code.data}'
            # return f'<h1> Username: {form.username.data} password: {form.password.data} Age: {form.age.data} Yes or No: {form.yes_no.data} email: {form.email.data}</h1>'
            output = '<h1>'

            for field in form.years:
                output += f'Year: {field.year.data} Total: {field.total.data} <br />' 
                
            output +=  '</h1>'
            return output

        return render_template('index.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)