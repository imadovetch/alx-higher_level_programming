#!/usr/bin/python3
""" script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa """

import sys
from model_state import State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        query = select(State).order_by(State.id.asc()) \
            .where(State.name.like("%a%"))
        states = connection.execute(query)
        for state in states:
            print(f"{state.id}: {state.name}")

    engine.dispose()
