from sqlalchemy.orm import declarative_base,Mapped,mapped_column
from sqlalchemy import String, Integer, Boolean, ForeignKey

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
