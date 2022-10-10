from onlineexam import app, db
from flask import render_template, url_for, redirect, flash
from onlineexam.forms import LoginForm, AddHeadsForm, AddExam, AddUser, HeadLogin, UserLogin, Delete, Update
from onlineexam.models import Admin, Heads, Exams, User, Updates


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('base.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    delhead = Delete()
    user = User.query.all()
    head = Heads.query.all()
    if delhead.validate_on_submit():
        head_to_delete = Heads.query.filter_by(headuid=delhead.uid.data).first()
        db.session.delete(head_to_delete)
        db.session.commit()
        flash("Deleted Head Successfully")
        redirect(url_for('admin_page'))

    return render_template('adminhome.html', head=head, user=user, form=delhead)


@app.route('/head')
def head_page():
    user = User.query.all()
    exam = Exams.query.all()
    updat = Updates.query.all()
    return render_template('headhome.html', user=user, exam=exam, updat=updat)


@app.route('/user', methods=['GET', 'POST'])
def user_page():
    return render_template('userhome.html')


@app.route('/userlogin', methods=['GET', 'POST'])
def user_login():
    form = UserLogin()
    if form.validate_on_submit():
        check_login = User(username=form.uname.data,
                           userpassword=form.password.data)
        for values in User.query.all():
            if (check_login.username == values.username) and (check_login.userpassword == values.userpassword):
                flash("Login:Success")
                return redirect(url_for('user_page'))
        flash(f'Error:No Login History Found')
    return render_template('userlogin.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        check_login = Admin(adminname=form.adminname.data,
                            password_hash=form.password.data)
        for values in Admin.query.all():
            if (check_login.adminname == values.adminname) and (check_login.password_hash == values.password_hash):
                return redirect(url_for('admin_page'))
            else:
                flash("No user Found. Please Try Again.")
                redirect(url_for('login_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error:{err_msg}')
    return render_template('login.html', form=form)


@app.route('/headlogin', methods=['GET', 'POST'])
def head_login():
    form = HeadLogin()
    if form.validate_on_submit():
        check_login = Heads(headname=form.headname.data,
                            hpassword=form.hpassword.data)
        for values in Heads.query.all():
            if (check_login.headname == values.headname) and (check_login.hpassword == values.hpassword):
                return redirect(url_for('head_page'))
            else:
                flash("No users Found! Login Again")
                redirect(url_for('lead_login'))
    return render_template('headlogin.html', form=form)


@app.route('/addhead', methods=['GET', 'POST'])
def head_add():
    form = AddHeadsForm()
    if form.validate_on_submit():
        head_to_create = Heads(headuid=form.headuid.data,
                               headname=form.headname.data,
                               deptname=form.deptname.data,
                               hpassword=form.confpass.data)
        db.session.add(head_to_create)
        db.session.commit()
        return redirect(url_for('admin_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error:{err_msg}')
    return render_template('addheads.html', form=form)


@app.route('/adduser', methods=['GET', 'POST'])
def add_user():
    form = AddUser()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              emailid=form.emailid.data,
                              gender=form.gender.data,
                              userpassword=form.userconfirm.data,
                              phone=form.phone.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('user_login'), form=form)

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error:{err_msg}', category='danger')
    return render_template('adduser.html', form=form)


@app.route('/addexam', methods=['GET', 'POST'])
def add_exam():
    form = AddExam()
    if form.validate_on_submit():
        exam_to_add = Exams(examcode=form.examcode.data,
                            examname=form.examname.data,
                            description=form.description.data,
                            examfee=form.examfee.data,
                            examdate=form.examdate.data,
                            findate=form.findate.data,
                            requirements=form.requirements.data)
        db.session.add(exam_to_add)
        db.session.commit()
        flash("Exam Added successfully")
        return redirect(url_for('head_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error:{err_msg}', category='danger')
    return render_template('addexam.html', form=form)


@app.route('/addupdate', methods=['GET', 'POST'])
def add_update():
    form = Update()
    if form.validate_on_submit():
        update_to_add = Updates(desc=form.description.data)
        db.session.add(update_to_add)
        db.session.commit()
        flash("Updates Added Successfully")
        return redirect(url_for("head_page"))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error:{err_msg}')
    return render_template("addupdates.html", form=form)
