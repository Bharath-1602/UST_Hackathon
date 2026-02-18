from flask import Flask , request 

app = Flask(__name__)
@app.route('/trigger')

def trigger(method=['GET']):
    if request.method == "GEt":
        return "Triggered the port"

if __name__ == "__main__":
    app.run(debug=True)

