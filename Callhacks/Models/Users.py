import reflex as rx
class User(rx.Model, table=True):
    username: str
    email: str
    password: str


with rx.session() as session:
    session.add(
        User(username="test", email="admin@pynecone.io", password="admin"))
    session.commit()
