from app import flask_app  # Import the Flask app instance from app module
import app.routes  # Ensure routes are imported after app initialization

if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=5000)
