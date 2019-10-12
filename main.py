from app import api, app
from methods.Organisation import Organisation1, Organisation2
# Routes
from methods.RestTEST import Hello

api.add_resource(Hello, '/Hello')
api.add_resource(Organisation1, '/Organisation')
api.add_resource(Organisation2, '/Organisation/<int:id>')
if __name__ == "__main__":
    # production
    # from waitress import serve
    #
    # serve(app)
    # develpment
    app.run(debug=True)
