from app import api, app

# Routes
from methods.RestTEST import Hello
from methods.Organisation import Organisation

api.add_resource(Hello, '/Hello')
api.add_resource(Organisation, '/Organisation')

if __name__ == "__main__":
    app.run(debug=True)
