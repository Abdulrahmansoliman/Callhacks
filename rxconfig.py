import reflex as rx

config = rx.Config(
    app_name="Callhacks",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    db_create_tables=True
)