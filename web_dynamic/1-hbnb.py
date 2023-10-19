#!/usr/bin/python3
# This is a shebang line specifying the Python interpreter to be used.

""" Starts a Flash Web Application """
# This is a docstring providing a brief description of the script's purpose.

from models import storage
# Import the 'storage' object from the 'models' module.

from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
# Import various models (State, City, Amenity, Place) from their respective modules.

from os import environ
# Import the 'environ' object from the 'os' module.

from flask import Flask, render_template
# Import the 'Flask' class and the 'render_template' function from the 'flask' module.

from uuid import uuid4
# Import the 'uuid4' function from the 'uuid' module.

app = Flask(__name__)
# Create a Flask application instance with the current module name.

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    # Define a function called 'close_db' to close the SQLAlchemy session when the application context is torn down.
    storage.close()

@app.route('/1-hbnb', strict_slashes=False)
# Define a route for the web application with the path '/1-hbnb'.

def hbnb():
    """ HBNB is alive! """
    # Define a function called 'hbnb' that will handle requests to the '/1-hbnb' route.
    states = storage.all(State).values()
    # Get all State objects from the storage and retrieve their values.
    states = sorted(states, key=lambda k: k.name)
    # Sort the states by their 'name' attribute.
    st_ct = []

    for state in states:
        # Loop through the sorted states.
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])
        # For each state, append a list containing the state and its associated cities sorted by name.

    amenities = storage.all(Amenity).values()
    # Get all Amenity objects from the storage and retrieve their values.
    amenities = sorted(amenities, key=lambda k: k.name)
    # Sort the amenities by their 'name' attribute.

    places = storage.all(Place).values()
    # Get all Place objects from the storage and retrieve their values.
    places = sorted(places, key=lambda k: k.name)
    # Sort the places by their 'name' attribute.

    id = str(uuid4())
    # Generate a random UUID and convert it to a string.
    return render_template('1-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=id)
    # Render an HTML template called '1-hbnb.html' and pass data (states, amenities, places, cache_id) to it.

if __name__ == "__main__":
    """ Main Function """
    # Check if the script is being run as the main program.
    app.run(host='0.0.0.0', port=5000, debug=True)
    # If so, run the Flask application with specified settings (host, port, and debug mode).
    