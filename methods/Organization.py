from flask_restful import Resource


class Entity(Resource):
    def __init__(self):
        self.entities = {}

    def add(self, entity):
        self.entities[entity.getID()] = entity

    def all(self):
        return self.entities

    def get(self, id):
        return self.entities[id]

    def __str__(self):
        _dict = dict(self)
        return "{" + ",\n ".join('{}:\'{}\''.format(k, _dict[k]) for k in _dict.keys()) + "}"


class Organisation(Entity):
    def __init__(self, file):
        super(Entity).__init__()
        self.file = open(file, 'w')

    def add(self, entity):
        self.file.write("put")

    def delete(self, id):
        entity = Entity()
        self.file.write("delete")
        del entity

    def get(self, id):
        self.file.write("get")
        return super().all()

    def all(self):
        self.file.write("get_all")
        return super().all()
