
import databases
import sqlalchemy
import ormar

DATABASE_URL = "sqlite:///pharm.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata

class Pharmacie(ormar.Model):
    class Meta(BaseMeta):
        tablename= "pharmacie"

    id: int  = ormar.Integer(primary_key=True)
    nom:str = ormar.String(max_length=200)
    contact1: str |None = ormar.String(max_length=20)
    contact2: str| None = ormar.String(max_length=20, nullable=True)
    lng: float | None = ormar.Float(nullable=True)
    lat: float |None = ormar.Float(nullable=True)
    adresse: str |None = ormar.String(max_length=200)
    isOpen: bool = ormar.Boolean(default=True)
    isActive: bool = ormar.Boolean(default=True)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)