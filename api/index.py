from app import app
from waitress import serve

if __name__ == "__main__":
    print("Starting up...")
    serve(app, port=6979)
    print("Server Closed")
