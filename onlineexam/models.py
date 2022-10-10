from onlineexam import db


class Admin(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    adminname = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)


class Heads(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    headuid = db.Column(db.String(length=50), nullable=False, unique=True)
    headname = db.Column(db.String(length=30), nullable=False, unique=False)
    deptname = db.Column(db.String(length=30), nullable=False, unique=False)
    hpassword = db.Column(db.String(length=60), nullable=False)


class Exams(db.Model):
    examcode = db.Column(db.String(), primary_key=True)
    examname = db.Column(db.String(length=30), nullable=False, unique=False)
    description = db.Column(db.String(length=100), nullable=False, unique=False)
    examfee = db.Column(db.Integer(), nullable=False, unique=False)
    examdate = db.Column(db.String(length=10), nullable=False, unique=False)
    findate = db.Column(db.String(length=10), nullable=False, unique=False)
    requirements = db.Column(db.String(length=50), nullable=False, unique=False)


class User(db.Model):
    userid = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=40), nullable=False, unique=False)
    emailid = db.Column(db.String(length=50), nullable=False, unique=True)
    gender = db.Column(db.String(length=10), nullable=False, unique=False)
    userpassword = db.Column(db.String(length=30), nullable=False, unique=False)
    phone = db.Column(db.String(length=10), nullable=False, unique=True)


class Updates(db.Model):
    upid = db.Column(db.Integer(), primary_key=True)
    desc = db.Column(db.String(length=200), nullable=False, unique=False)
    # def __repr__(self):
    # return 0
