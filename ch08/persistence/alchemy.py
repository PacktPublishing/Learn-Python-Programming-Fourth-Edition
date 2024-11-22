# persistence/alchemy.py
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session

from alchemy_models import Person, Email, Base

# swap these lines to work with an actual DB file
# engine = create_engine('sqlite:///example.db')
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)


def display_info(session):
    # get all emails first
    emails = select(Email)

    # display results
    print("All emails:")
    for email in session.scalars(emails):
        print(f" - {email.person.name} <{email.email}>")

    # display how many objects we have in total
    people = session.scalar(
        select(func.count()).select_from(Person)
    )
    emails = session.scalar(
        select(func.count()).select_from(Email)
    )

    print("Summary:")
    print(f" {people=}, {emails=}")


with Session(engine) as session:

    # Create a couple of people
    anakin = Person(name="Anakin Skywalker", age=32)
    obione = Person(name="Obi-Wan Kenobi", age=40)

    # Add emails for both of them
    obione.emails = [
        Email(email="obi1@example.com"),
        Email(email="wanwan@example.com"),
    ]

    # another way: we can simply append
    anakin.emails.append(Email(email="ani@example.com"))
    anakin.emails.append(Email(email="evil.dart@example.com"))
    anakin.emails.append(Email(email="vader@example.com"))

    # Add people to the session. This adds emails too.
    session.add(anakin)
    session.add(obione)
    session.commit()

    # Query and display both
    obione = session.scalar(
        select(Person).where(Person.name.like("Obi%"))
    )
    print(obione, obione.emails)

    anakin = session.scalar(
        select(Person).where(Person.name == "Anakin Skywalker")
    )
    print(anakin, anakin.emails)

    # capture anakin.id
    anakin_id = anakin.id

    # then delete the object
    del anakin

    display_info(session)

    # Fetch anakin directly by its id
    anakin = session.get(Person, anakin_id)

    # Delete anakin from the database
    session.delete(anakin)
    session.commit()

    # let us do it again and see the changes
    display_info(session)


"""
$ python alchemy.py
Obi-Wan Kenobi(id=2) [obi1@example.com, wanwan@example.com]

Anakin Skywalker(id=1) [
    ani@example.com, evil.dart@example.com, vader@example.com
]

All emails:
 - Anakin Skywalker <ani@example.com>
 - Anakin Skywalker <evil.dart@example.com>
 - Anakin Skywalker <vader@example.com>
 - Obi-Wan Kenobi <obi1@example.com>
 - Obi-Wan Kenobi <wanwan@example.com>
Summary:
 people=2, emails=5

All emails:
 - Obi-Wan Kenobi <obi1@example.com>
 - Obi-Wan Kenobi <wanwan@example.com>
Summary:
 people=1, emails=2
"""
