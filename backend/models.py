from sqlalchemy import Boolean, Column, Integer, String, create_engine, JSON
from sqlalchemy.orm import DeclarativeBase


def init_engine(url:str):
    engine = create_engine(url)
    return engine

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    coins = Column(Integer, default=0)
    energy = Column(Integer, default=500)
    max_energy = Column(Integer, default=500)
    coins_per_click = Column(Integer, default= 1)
    country = Column(String(255))
    jwt = Column(String(255))
    has_print_bot = Column(Boolean,default=False)
    multi_print_lvl = Column(Integer, default=1)
    recharging_speed_lvl = Column(Integer, default=1)
    energy_limit_lvl = Column(Integer, default=1)
    printed_notes = Column(Integer, default=0)
class Ref(Base):
    __tablename__ = 'ref'
    
    id = Column(Integer, primary_key=True)
    creator_user = Column(Integer)
    come_user = Column(Integer)
class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    type = Column(Integer, default=0)
    data = Column(JSON)
    
    #   {'title': 'Join our socials', 'icon': TiSocialYoutube, 'money': '60 000 000', 'complited': false 'tasks': [
    #            { 'title': 'Join the Telegram chat', 'status': 'Go', 'finished': false, 'url': 'https://youtube.com' },
    #            { 'title': 'Join the Telegram chat', 'status': 'Go', 'finished': false, 'url': 'https://youtube.com' },
    #            { 'title': 'Join the Telegram chat', 'status': 'Go', 'finished': false, 'url': 'https://youtube.com' },
    #        ],
    #    }
    