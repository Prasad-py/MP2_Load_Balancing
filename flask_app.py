from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the seed value
seed_value = 0

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    global seed_value
    if request.method == 'POST':
        # Update the seed value with the number provided in the JSON body
        data = request.get_json()
        seed_value = data.get('num', seed_value)  # Defaults to current seed value if 'num' not in JSON
        return jsonify(success=True), 200
    elif request.method == 'GET':
        # Return the seed value
        return str(seed_value), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

