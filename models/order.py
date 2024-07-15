from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from sqlalchemy import Column, Integer, Date, ForeignKey, Table
from typing import List


order_product = db.Table(
    "order_product",
    Base.metadata,  
    db.Column("order_id", db.ForeignKey("orders.id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("products.id"), primary_key=True))

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey("customers.id"))
    
    customer: Mapped["Customer"] = db.relationship(back_populates="orders")
    products: Mapped[List["Product"]] = db.relationship(secondary="order_product", back_populates="orders")


    