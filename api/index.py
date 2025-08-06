from app import app
from waitress import serve

if __name__ == "__main__":
    print("Starting up...")
    serve(app, host='0.0.0.0', port=6979)
    print("Server Closed")
