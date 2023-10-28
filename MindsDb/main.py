import sql
import mindsdb
from mindsdb import Predictor
from models.Users import config

mdb = mindsdb.Predictor()

# Define the database connection in MindsDB
mdb.learn(
    from_data=f'postgresql://{config.db_config.username}:{config.db_config.password}@{config.db_config.host}:{config.db_config.port}/{config.db_config.database}',
    to_predict='column_to_predict'
)
