from pony.orm.core import PrimaryKey, Required

from app import db


class Organisation(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Required(str)
    Description = Required(str)
    Position = Required(str)


db.generate_mapping(create_tables=True)
