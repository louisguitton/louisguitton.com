from app import db
from playhouse.migrate import *


migrator = SqliteMigrator(db)

social_id = CharField(null=False, unique=True, default='facebook')
id = BigIntegerField(primary_key=True)

migrate(
    migrator.drop_column('user', 'id', id),
)
