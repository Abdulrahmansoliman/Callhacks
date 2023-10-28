from Callhacks.Callhacks import rx
from reflex import DBConfig

config = rx.Config(
    app_name="Classifier",
    db_url="sqlite:///reflex.db",
    db_config=rx.DBConfig(engine="postgresql+psycopg2", username="Classifier",
                          password="12345", host="localhost", port=5432, database="reflex"),

)


DBConfig.sqlite(database="reflex.db")
DBConfig.postgresql(username="Classifier", password="12345",
                    host="localhost", port=5432, database="reflex")
DBConfig.postgresql_psycopg2(username="Classifier",
                             password="12345", host="localhost", port=5432, database="reflex")

class User(rx.Model, table=True):
    username: str
    email: str
    password: str
