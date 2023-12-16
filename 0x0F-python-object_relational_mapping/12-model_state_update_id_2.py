#!/usr/bin/python3
""" script that changes the name of a State
object from the database hbtn_0e_6_usa """

import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    upd = sessionmaker(bind=engine)
    session = upd()
    updateState = session.query(State).filter_by(id=2).first()

    if updateState:
        updateState.name = 'New Mexico'
        session.commit()
    session.close()
