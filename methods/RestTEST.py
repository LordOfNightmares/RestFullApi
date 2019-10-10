from methods.Authentication import AuthenticatedResource


class Hello(AuthenticatedResource):
    def get(self):
        return {"message": "Hello,GET World!"}

    def post(self):
        return {"message": "Hello,POST World!"}

    def delete(self):
        return {"message": "Hello,DELETE World!"}

    def put(self):
        return {"message": "Hello,PUT World!"}
