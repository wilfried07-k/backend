# init_db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

# URL de connexion (à adapter si besoin)
DATABASE_URL = "postgresql://kana:kana123@localhost/ia_db"

# Création du moteur
engine = create_engine(DATABASE_URL, echo=True)

# Base déclarative
class Base(DeclarativeBase):
    pass

# Modèle User simple
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String)

print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Terminé.")
