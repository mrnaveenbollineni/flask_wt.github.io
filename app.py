from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    product_name = request.form['product_name']
    
    # Convert to JSON format
    data = {
        'name': name,
        'product_name': product_name
    }
    
    return jsonify(data)  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
