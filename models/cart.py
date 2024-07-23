from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Cart(Base):
    __tablename__ = 'cart'
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False, default=1)
    products: Mapped["Product"] = db.relationship()
    
    
