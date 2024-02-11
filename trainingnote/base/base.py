from trainingnote.database import async_session_maker
from sqlalchemy import select, insert, update


class Base:
    model = None

    @classmethod
    async def find_by_id(cls, model_id):
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.id == model_id)
            res = await session.execute(query)
            return res.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            res = await session.execute(query)
            return res.scalars().all()

    @classmethod
    async def delete(cls, model_id: int):
        async with async_session_maker() as session:
            model = await session.get(cls.model, model_id)
            await session.delete(model)
            await session.commit()
            return {"deleted": True}

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, model_id, **data):
        async with async_session_maker() as session:
            query = update(cls.model).values(**data).where(cls.model.id == model_id)
            await session.execute(query)
            await session.commit()