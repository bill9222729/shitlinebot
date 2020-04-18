from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(String(100), primary_key=True)
    user_name = Column(String(100), nullable=True)
    phone_number = Column(String(100), nullable=True)
    home_address = Column(String(100), nullable=True)
    company_address = Column(String(100), nullable=True)
    created_time = Column(DateTime(), nullable=False)
    is_member = Column(Boolean, nullable=False)
    is_signup = Column(Boolean, nullable=False)
    edit_user_name = Column(Boolean, nullable=False)
    edit_home_address = Column(Boolean, nullable=False)
    edit_company_address = Column(Boolean, nullable=False)
    #name = Column(String(50), unique=True)
    #email = Column(String(120), unique=True)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name
        self.home_address = '尚未填寫住家地址或是地標'
        self.company_address = '尚未填寫公司地址或是地標'
        self.created_time = datetime.datetime.now()
        self.is_member = False
        self.is_signup = False
        self.edit_user_name = False
        self.edit_home_address = False
        self.edit_company_address = False

    def __repr__(self):
        return '<User %r>' % (self.id)