from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import Length, NumberRange, Email, AnyOf, EqualTo, DataRequired


class LoginForm(FlaskForm):
    adminname = StringField(label='Admin Name', validators=[Length(min=1, max=30, message='Please Provide a name.')])
    password = PasswordField(label='Password', validators=[Length(min=1, max=20, message="Provide a Password.")])
    login = SubmitField(label='Login')


class UserLogin(FlaskForm):
    uname = StringField(label='User Name', validators=[Length(min=1, max=30, message='Please Provide a name.')])
    password = PasswordField(label='Password', validators=[Length(min=1, max=20, message="Provide a Password.")])
    login = SubmitField(label='Login')


class HeadLogin(FlaskForm):
    headname = StringField(label='Head Name', validators=[Length(min=1, max=30, message='Please Provide a name.')])
    hpassword = PasswordField(label='Password')
    hlogin = SubmitField(label='Login')


class AddHeadsForm(FlaskForm):
    headuid = StringField(label='Head User ID',
                          validators=[Length(min=5, max=15, message='Please Provide a ID between 6-15 Characters.')])
    deptname = StringField(label='Department Name',
                           validators=[Length(min=1, max=30, message='Please Provide dept name.')])
    headname = StringField(label="Head Name",
                           validators=[Length(min=5, max=20, message='Please Provide a name between 6-20 Characters.')])
    hpassword = PasswordField(label='Password',
                              validators=[DataRequired(message='Please enter password') ])
    confpass = PasswordField('Confirm Password',
                             validators=[DataRequired(message='Enter Password'),
                                         EqualTo(hpassword, message="Password doesn't match")])

    addhead = SubmitField(label='Add Head')


class AddExam(FlaskForm):
    examcode = StringField('Exam Code', validators=[Length(min=4, max=20, message='Too Short for Exam Code.')])
    examname = StringField('Exam Name', validators=[Length(min=3, max=15, message=u'Too Short For Exam Name.')])
    description = StringField("Description", validators=[Length(min=5, max=100, message=u'Too short For Description.')])
    examfee = IntegerField('Exam Fees', validators=[NumberRange(min=0, max=50000, message=u'Invalid Input Given.')])
    examdate = DateTimeField('Exam Date: Format = dd/mm/yy', format='%d/%m/%y')
    findate = DateTimeField('Final Date To Apply: Format= dd/mm/yy', format='%d/%m/%y')
    requirements = StringField('Qualifications to Apply',
                               validators=[Length(min=5, max=100, message=u'Too short for Qualifications')])
    addexam = SubmitField(label='Add Exam')


class AddUser(FlaskForm):
    username = StringField('User Name', validators=[Length(min=1, max=30, message='Please Provide a name.')])
    emailid = StringField("Email-Id", validators=[Email("Enter email-id")])
    gender = StringField('Gender',
                         validators=[AnyOf(values=('male', 'female'),
                                           message="Invalid data. Enter in Specified format")])
    userpass = PasswordField('Password')
    userconfirm = PasswordField('Confirm Password', validators=[EqualTo(userpass, message="Passwords don't match")])
    phone = StringField('Phone no', validators=[DataRequired(message="Enter A phone Number")])
    register = SubmitField(label="Register")


class Delete(FlaskForm):
    uid = StringField()
    delete = SubmitField(label='Delete')
    update = SubmitField(label="Update")

class Update(FlaskForm):
    description = StringField("Description",
                              validators=[Length(min=5, max=200, message="Enter a detailed description")])
    addupdate = SubmitField(label="Add Update")


