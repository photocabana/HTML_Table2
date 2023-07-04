from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Rindy', 'last_name' : 'Fisk'},
        {'first_name' : 'Quackers', 'last_name' : 'Mccoy'},
        {'first_name' : 'Dreamy', 'last_name' : 'McDream Pants'},
        {'first_name' : 'Minnie', 'last_name' : 'Mouse'},
        {'first_name' : 'Mickey', 'last_name' : 'Mouse'},
        {'first_name' : 'Donald', 'last_name' : 'Duck'}
    ]

    return render_template('index.html', users = users)  

if __name__=="__main__":
    app.run(debug=True)

