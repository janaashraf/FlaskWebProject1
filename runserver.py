"""
This script runs the FlaskWebProject1 application using a production-ready server.
"""

from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    # Use Somee.com's recommended server host and port settings
    HOST = '0.0.0.0'  # Listen on all available network interfaces
    PORT = int(environ.get('PORT', '5555'))  # Somee.com might provide PORT as environment variable

    # Ensure app runs with production settings
    app.run(HOST, PORT)
