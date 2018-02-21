from flask import Flask, request, render_template, url_for


app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    url_for('static', filename="tree.json")
 