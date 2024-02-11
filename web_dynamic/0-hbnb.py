#!/usr/bin/python3
"""
    a script that starts a Flask web application
"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    all_states = storage.all(State).values()
    all_states = sorted(all_states, key=lambda k: k.name)
    ste_cty = []

    for state in all_states:
        ste_cty.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           all_states=ste_cty,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000


            @app.route('/0-hbnb/', strict_slashes=False)
            def hbnb():
            all_states = storage.all(State).values()
                all_states = sorted(all_states, key=lambda k: k.name)
                    ste_cty = []

                        for state in all_states:
                                ste_cty.append([state, sorted(state.cities, key=lambda k: k.name)])

                                    amenities = storage.all(Amenity).values()
                                        amenities = sorted(amenities, key=lambda k: k.name)

                                            places = storage.all(Place).values()
                                                places = sorted(places, key=lambda k: k.name)

                                                    return render_template('0-hbnb.html',
                                                                                   all_states=ste_cty,
                                                                                                              amenities=amenities,
                                                                                                                                         places=places,
                                                                                                                                                                    cache_id=uuid.uuid4())


                                                if __name__ == "__main__":
                                                    app.run(host='0.0.0.0', port=5000


                                                        @app.route('/0-hbnb/', strict_slashes=False)
                                                        def hbnb():
                                                        all_states = storage.all(State).values()
                                                            all_states = sorted(all_states, key=lambda k: k.name)
                                                                ste_cty = []

                                                                    for state in all_states:
                                                                            ste_cty.append([state, sorted(state.cities, key=lambda k: k.name)])

                                                                                amenities = storage.all(Amenity).values()
                                                                                    amenities = sorted(amenities, key=lambda k: k.name)

                                                                                        places = storage.all(Place).values()
                                                                                            places = sorted(places, key=lambda k: k.name)

                                                                                                return render_template('0-hbnb.html',
                                                                                                                               all_states=ste_cty,
                                                                                                                                                          amenities=amenities,
                                                                                                                                                                                     places=places,
                                                                                                                                                                                                                cache_id=uuid.uuid4())


                                                                                            if __name__ == "__main__":
                                                                                                app.run(host='0.0.0.0', port=5000)))
