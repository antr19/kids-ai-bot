# импортируем классы, используемые для определения атрибутов модели
from sqlalchemy import Column, Integer, String, create_engine, UniqueConstraint
from sqlalchemy.orm import sessionmaker

# объект для подключения ядро базы данных
from sqlalchemy.ext.declarative import declarative_base

# создаем класс, от которого будут наследоваться модели
Base = declarative_base()

engine = create_engine("sqlite:///attachments.db")

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Attachment(Base):
    __tablename__ = 'attachments'
    id = Column(Integer, primary_key=True)
    command = Column(String(200), nullable=False)
    text = Column(String(200), nullable=True)
    path_to_file = Column(String(200), nullable=True)

    __table_args__ = (
        UniqueConstraint('command'),
    )

    def __init__(self, **kwargs):
        self.command = kwargs.get('command')
        self.text = kwargs.get('text')
        self.path_to_file = kwargs.get('path_to_file')


async def shutdown(_):
    session.close()


Base.metadata.create_all(engine)
