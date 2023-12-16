#!/usr/bin/python3
""" script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa """

import sys
from model_state import State
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        transaction = connection.begin()
        queryName = insert(State).values(name="Louisiana")
        connection.execute(queryName)
        queryName = select(State).where(State.name == "Louisiana")
        state = connection.execute(queryName).fetchone()
        if state:
            print(state.id)
        transaction.commit()

    engine.dispose()
