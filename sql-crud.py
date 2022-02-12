from sqlalchemy import (
    create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    ''' Docstring '''
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    nationality = Column(String())
    famous_for = Column(String())


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margareth_hamilton = Programmer(
    first_name="Margareth",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apolo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft Corporation"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web (WWW)"
)

emidio_valereto = Programmer(
    first_name="Emidio",
    last_name="Valeretto",
    gender="Male",
    nationality="Brazilian",
    famous_for="Full Stack Software Developer"
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margareth_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(emidio_valereto)
# session.commit()

# people = session.query(Programmer)

# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")

#     session.commit()

# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Code Institute Student"

# session.commit()

fname = input("Enter a first name: ")
lname = input("Enter a last name: ")

programmer = session.query(Programmer).filter_by(
    first_name=fname,
    last_name=lname).first()

if programmer is not None:
    print(f"Programmer found: {programmer.first_name} {programmer.last_name} ")
    confirmation = input(
        "Are you sure you want to delete this record? [y/n] => "
    )
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer deleted successfully")
    else:
        print("Programmer not deleted.")
else:
    print("Record not found!")

programmers = session.query(Programmer)

for programmer in programmers:
    print(
        f"{programmer.id} | "
        f"{programmer.first_name} {programmer.last_name} | "
        f"{programmer.gender} | "
        f"{programmer.nationality} | "
        f"{programmer.famous_for}"
        )
