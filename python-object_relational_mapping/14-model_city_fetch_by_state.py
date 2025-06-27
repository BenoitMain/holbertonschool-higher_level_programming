#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa,
showing the state and city in the format <state name>: (<city id>) <city name>
"""

import sys
from model_state import Base, State
from model_city import City
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
    results = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all())
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
