from pony.orm.core import db_session


class DatabaseMethods:
    def __init__(self, cls):
        self.cls = cls

    @db_session
    def __add__(self, *args, **kwargs):
        if not kwargs or len(args) > 0:
            if self.cls.__name__ == 'Organisation':
                kwargs = {'Name': args[0],
                          'Description': args[1],
                          'Position': args[2]}
        self.cls(**kwargs)

    @db_session
    def __update__(self, *args, **kwargs):
        if not kwargs or len(args) > 0:
            if self.cls.__name__ == 'Organisation':
                kwargs = {'id': args[0],
                          'Name': args[1],
                          'Description': args[2],
                          'Position': args[3]}
        self.cls.set(**kwargs)

    @db_session
    def __get__(self, id):
        try:
            return self._get_dict(self.cls[id])
        except Exception as e:
            return e

    @db_session
    def __delete__(self, id):
        try:
            elm = self.cls[id]
            self.cls[id].delete()
            return "{} was deleted".format(elm)
        except Exception as e:
            return e

    @db_session
    def __all__(self):
        return [self._get_dict(obj) for obj in self.cls.select()]

    def _get_dict(self, obj):
        return {attr.name: attr.__get__(obj) for attr in obj._attrs_}
