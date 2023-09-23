#!/usr/bin/python3
"""List all records in the table staes from a database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    result = session.query(State).order_by(State.id).all()
    for state in result:
        print(f"{state.id}: {state.name}")
    session.close()
