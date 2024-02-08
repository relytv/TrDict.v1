from database import async_session_maker
from sqlalchemy import select, insert


class Base:
    model = None

    @classmethod
    async def find_by_id(cls, model_id):
        with async_session_maker as session:
            query = select(cls.model).where(cls.model.id == model_id)
            res = await session.execute(query)
            return res.scalar_one_or_none()
