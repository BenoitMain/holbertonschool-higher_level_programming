#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.

This script connects to a MySQL database using SQLAlchemy ORM,
retrieves all State objects whose name contains the letter 'a',
sorts them by states.id in ascending order, and prints them in the format:
<state id>: <state name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
        State.name.contains("a")).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
