"""
Application entry point.
"""

from hbnb.app import create_app

app = create_app()

@app.route('/')
def home():
    return {"message": "HBnB API is running"}, 200

if __name__ == '__main__':
    app.run(debug=True)