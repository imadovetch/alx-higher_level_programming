#!/usr/bin/python3
""" script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa """

import sys
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    upd = sessionmaker(bind=engine)
    session = upd()

    states = session.query(State).order_by(State.id)

    for instance in states:
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
