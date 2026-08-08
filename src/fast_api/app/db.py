# orm - object relational mapping
# we will use SQLAlchemy to map our Python classes to database tables and vice versa. This allows us to interact with the database using Python objects instead of writing raw SQL queries.

from collections.abc import AsyncGenerator
import uuid 
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, relationship
import datetime
Base = declarative_base()



DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # this is the database URL for a SQLite database named test.db located in the current directory. The aiosqlite driver is used for asynchronous database operations.



class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String(255), nullable=False)
    filetype = Column(String(50), nullable=False)
    filename = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(DateTime, server_default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")


# this part of the code creates an asynchronous engine and session maker for interacting with the database. The create_async_engine function is used to create an asynchronous engine that connects to the database specified by DATABASE_URL. The async_sessionmaker function is used to create a session maker that will be used to create asynchronous sessions for interacting with the database. The expire_on_commit=False argument is used to prevent SQLAlchemy from expiring objects in the session after a commit, which can be useful in certain scenarios where you want to keep using the objects after committing changes to the database.
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()