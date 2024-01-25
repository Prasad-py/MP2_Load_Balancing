from flask import Flask, request, jsonify
from multiprocessing import Pool, cpu_count
import time

app = Flask(__name__)

# Existing seed value code here...
seed_value = 0

# New route to handle CPU stress
@app.route('/stress', methods=['POST'])
def stress_cpu():
    # Function to perform CPU intensive computation
    def compute(n):
        total = 0
        for i in range(n):
            total += i**2
        return total

    try:
        # Read the JSON data from the POST request
        data = request.get_json()
        n = data.get('n', 110000000)  # Default value if none provided
        
        # Log the stress test start time
        start_time = time.time()

        # Create a pool of processes
        processes = cpu_count()
        pool = Pool(processes)

        # Run the compute function in parallel
        pool.map(compute, [n] * processes)

        # Log the time taken to perform the stress test
        duration = time.time() - start_time
        return jsonify({"message": "Stress test completed", "time_cost": duration}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
