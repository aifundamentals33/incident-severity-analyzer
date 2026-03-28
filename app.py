from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to My Flask App</h1><p>This is the homepage.</p>'

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'success',
        'message': 'API is working correctly',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
