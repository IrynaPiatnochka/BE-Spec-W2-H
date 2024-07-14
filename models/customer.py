from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(250), nullable=False)
    email: Mapped[str] = mapped_column(db.String(250), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(16), nullable=False)
    username: Mapped[str] = mapped_column(db.String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(250), nullable=False)
            
    
    
    
