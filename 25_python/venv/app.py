from flask import Flask, render_template, request
import sys
import os
import json
sys.path.append('../25_python/')  # Ensure this path contains listcommand.py
import listcommand

app = Flask(__name__)

DATA_FILE = os.path.join(os.getcwd(), 'customer_data.json')

def save_customer_data(data):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            all_data = json.load(f)
    else:
        all_data = []
    all_data.append(data)
    with open(DATA_FILE, 'w') as f:
        json.dump(all_data, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        customer_input = request.form.get('customer_input', '')
        # Example: use listcommand.main() for prediction/response
        try:
            prediction = listcommand.main() if hasattr(listcommand, 'main') else 'No output from listcommand.py'
        except Exception as e:
            prediction = f'Error calling listcommand.main(): {e}'
        result = prediction
        save_customer_data({'input': customer_input, 'prediction': prediction})
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
