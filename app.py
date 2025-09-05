from flask import Flask , render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/hearing')
def hearing():
    return render_template('hearing.html')

if __name__ == '__main__':
    app.run(debug=True)
    