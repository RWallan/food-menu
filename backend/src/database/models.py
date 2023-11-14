from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Food(Base):
    __tablename__ = "foods"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float]
    image: Mapped[str]
