from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':"Miguel"}
	posts = [{'author':{'nickname':'John'},'body':'Beautiful day in Portland!'},
			{'author':{'nickname':'Susan'},'body':'The Avengers movie was so cool!'}]
	return render_template("index.html",title = "Home",user=user,posts=posts)

@app.route('/login',methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		#flash 函数是一种快速的方式下呈现给用户的页面上显示一个消息
		flash('Login requested for OpenID="'+form.openid.data+'",remember_me='+str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',title='Sign In',form = form,providers = app.config['OPENID_PROVIDERS'])

@app.route('/channel_v3.json')
def json():
	return render_template('channel_v3.json')
