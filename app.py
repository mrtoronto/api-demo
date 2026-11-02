from flask import Flask, jsonify, render_template, request

# Initialize the Flask application
app = Flask(__name__)


# 1. GET endpoint: Serves the main page when visiting http://localhost:5000/
@app.route('/', methods=['GET'])
def home():
    """Render the home page for the API demo."""
    return render_template('index.html', title='Flask API Demo')


# 2. POST endpoint: Accepts JSON data and returns a JSON response
@app.route('/api/greet', methods=['POST'])
def greet():
    """
    Example POST endpoint that reads a JSON payload (e.g. {"name": "Alice"})
    and returns a greeting message as JSON.
    """
    # Parse incoming JSON body (defaults to an empty dict if none is sent)
    data = request.get_json(silent=True) or {}
    name = data.get('name', 'World')

    # Return a JSON response along with HTTP status code 200 (OK)
    return jsonify({
        'message': f'Hello, {name}!',
        'received': data,
    }), 200


if __name__ == '__main__':
    # Run the development server on http://localhost:5000
    app.run(debug=True)

