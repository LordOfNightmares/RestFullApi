from app import api, app

# Routes
from methods.RestTEST import Hello
from methods.Organisation import OrganisationHTTP

api.add_resource(Hello, '/Hello')
api.add_resource(OrganisationHTTP, '/Organisation')

if __name__ == "__main__":
    app.run(debug=True)
