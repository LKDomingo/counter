from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'anybody want a peanut?'
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else: 
        session['count'] = 0
    return render_template("index.html")

@app.route('/destroy_session')
def sessionDestroy():
    session.clear()

    return redirect('/')

@app.route('/plus2')
def plus2():
    print('entered post method')
    session['count'] += 1

    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)