from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, AnyOf, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecret!'

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

class User():
    def __init__(self, username, age, email) -> None:
        self.username = username
        self.age = age
        self.email = email



    @app.route('/', methods = ['POST', 'GET'])
    def index():

        User_sylwek = User(username='Stalonek', age=32, email='cykor13@gmail.com')
        form = NameForm(obj=User_sylwek)

        if form.validate_on_submit():
            return f'<h1> Username: {form.username.data} password: {form.password.data} Age: {form.age.data} Yes or No: {form.yes_no.data} email: {form.email.data}</h1>'
        
        return render_template('index.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)