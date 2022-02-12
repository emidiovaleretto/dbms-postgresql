from sqlalchemy import (
    create_engine, Column, Float, Integer, String)
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


class FavoriteGames(base):
    '''Class Favorite Games'''

    __tablename__ = "FavoriteGames"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    console = Column(String)
    publisher = Column(String)
    release_year = Column(Integer)
    price = Column(Float)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

resident_evil = FavoriteGames(
    name="Resident Evil",
    console="PS4",
    publisher="Capcom",
    release_year=2017,
    price=15.99
)

call_of_duty = FavoriteGames(
    name="Call of Duty: Modern Walfare",
    console="PS4",
    publisher="Activision",
    release_year=2019,
    price=44.99
)

gran_turismo = FavoriteGames(
    name="Gran Turismo",
    console="PS4",
    publisher="Sony Computer Entertainment",
    release_year=2017,
    price=28.99
)

hitman = FavoriteGames(
    name="Hitman 2",
    console="PS4",
    publisher="Warner Bros",
    release_year=2018,
    price=12.99
)

gran_theft_auto = FavoriteGames(
    name="Gran Theft Auto V (GTA)",
    console="PS4",
    publisher="Rockstar",
    release_year=2014,
    price=28.99
)

spider_man = FavoriteGames(
    name="Spider Man",
    console="PS4",
    publisher="Sony Computer Entertainment",
    release_year=2018,
    price=34.99
)

last_of_us = FavoriteGames(
    name="Last of Us Remastered",
    console="PS4",
    publisher="Sony Computer Entertainment",
    release_year=2014,
    price=28.99
)

god_of_war = FavoriteGames(
    name="God of War",
    console="PS4",
    publisher="Sony Computer Entertainment",
    release_year=2018,
    price=27.99
)

# session.add(resident_evil)
# session.add(call_of_duty)
# session.add(gran_turismo)
# session.add(hitman)
# session.add(gran_theft_auto)
# session.add(spider_man)
# session.add(last_of_us)
# session.add(god_of_war)

# game_id = int(input("Enter an ID: "))
# game = session.query(FavoriteGames).filter_by(id=game_id).first()
# print(f"Found game: {game.name}")
# price = float(input("What is the new price: "))
# game.price = price

# my_games = session.query(FavoriteGames)

# for game in my_games:
#     if game.console == "PS4":
#         game.console = "Playstation 4"
#     else:
#         print("Console not defined.")

#     session.commit()

game_id = int(input("Enter an ID: "))

game_to_delete = session.query(FavoriteGames).filter_by(id=game_id).first()

if game_to_delete is not None:
    print(f"Game found: {game_to_delete.name}.")
    confirmation = input("Are you sure you want to delete this record? [y/n] => ")
    if confirmation.lower() == "y":
        session.delete(game_to_delete)
        session.commit()
        print("Game deleted successfully.")
    else:
        print("Game not deleted.")
else:
    print("Game not found!")


games = session.query(FavoriteGames)

for game in games:
    print(
        f"{game.id} | "
        f"{game.name} | "
        f"{game.console} | "
        f"{game.publisher} | "
        f"{game.release_year} | "
        f"{game.price} | "
    )

# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL Language"
# )

# margareth_hamilton = Programmer(
#     first_name="Margareth",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apolo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft Corporation"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web (WWW)"
# )

# emidio_valereto = Programmer(
#     first_name="Emidio",
#     last_name="Valeretto",
#     gender="Male",
#     nationality="Brazilian",
#     famous_for="Full Stack Software Developer"
# )

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

# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")

# programmer = session.query(Programmer).filter_by(
#     first_name=fname,
#     last_name=lname).first()

# if programmer is not None:
#     print(f"Programmer found: {programmer.first_name} {programmer.last_name}.")
#     confirmation = input(
#         "Are you sure you want to delete this record? [y/n] => "
#     )
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer deleted successfully")
#     else:
#         print("Programmer not deleted.")
# else:
#     print("Record not found!")

# programmers = session.query(Programmer)

# for programmer in programmers:
#     print(
#         f"{programmer.id} | "
#         f"{programmer.first_name} {programmer.last_name} | "
#         f"{programmer.gender} | "
#         f"{programmer.nationality} | "
#         f"{programmer.famous_for}"
#         )
