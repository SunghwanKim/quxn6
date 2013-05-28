from flask import Flask,url_for, session, escape, request, redirect ,render_template
app = Flask(__name__)

@app.route('/')
def index():
	if ('username' in session):
		return 'logged in as %s <p><a href="/logout">logout</a>'% escape(session['username'])
	return 'You are not logged in <p><a href="/login">go to login page</a>'


@app.route('/student/<username>/')
def student(username) :
	return 'Hello %s' % username

@app.route('/student/<username>/<int:user_id>')
def student_with_id(username, user_id):
	return 'Hello %s, %d' % (username, user_id)


@app.route('/method' , methods=['GET','POST'])
def test_HTTP_method():
	if request.method == 'POST':
		return request.method
	else:
		return request.method + '<p>' + request.args.get('name') + '<p>' + request.args.get('password')

@app.route('/login', methods=['POST','GET'])
def login():
	if (request.method == 'POST'):
		name = request.form['name']
		passwd = request.form['password']
		if (name) :
			session['username'] = name
		na = session['username']
		return render_template("main.html",name=na)

	else :
		return render_template("login.html")


if(__name__ == "__main__"):
	app.debug = True
	app.secret_key = '\x088\xab\x1a3\xc0\xd2\xc8\xc5\x9cr\xd5/\x85wk\xa2H\xb2\xc4\xcfO\x95y'
	app.run()
	


