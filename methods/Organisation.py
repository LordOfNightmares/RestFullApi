from methods.Resource import AuthenticatedResource

organisation = [
    {'name': 'O1',
     'description': 'salary',
     'amount': 5000}
]


class Entity:
    def __init__(self):
        self.entities = {}

    def add(self, entity):
        self.entities[entity.get_id()] = entity

    def get_id(self):
        return self.id

    def all(self):
        return self.entities

    def get(self, id):
        return self.entities[id]

    def __str__(self):
        _dict = dict(self)
        return "{" + ",\n ".join('{}:\'{}\''.format(k, _dict[k]) for k in _dict.keys()) + "}"


class Organisation(AuthenticatedResource):
    def __init__(self):
        self.entity = Entity()
        self.file = open("file.txt", 'a')

    def post(self):
        self.id = 0
        self.entity.name = 'O1',
        self.entity.description = 'salary',
        self.entity.amount = 5000
        self.entity.add(self.entity)
        self.file.write("post\n")

    def put(self):
        self.file.write("put\n")

    def delete(self):
        self.file.write("delete\n")

    def get(self):
        self.file.write("get\n")

    def all(self):
        self.file.write("get_all\n")
