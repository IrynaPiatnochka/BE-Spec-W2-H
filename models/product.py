from dataclasses import fields
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

from models.schemas.cartSchema import CartSchema

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(250), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    
    carts: Mapped["Cart"] = db.relationship("Cart", back_populates="product")

    