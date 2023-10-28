from reflex import DBConfig
import reflex as rx

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
