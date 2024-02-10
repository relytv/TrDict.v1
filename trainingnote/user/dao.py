from sqlalchemy import select
from sqlalchemy.orm import selectinload
from trainingnote.base.base import Base
from trainingnote.user.models import User
from trainingnote.database import async_session_maker
from trainingnote.user.schemas import UserRelDTO


class UserDAO(Base):
    model = User

    @classmethod
    async def get_all_trainings(cls, user_id):
        async with async_session_maker() as session:
            query = select(cls.model).options(selectinload(cls.model.training)).where(cls.model.id == user_id)
            res = await session.execute(query)
            res_orm = res.scalars().all()
            print(res_orm)
            result_dto = [
                UserRelDTO.model_validate(row, from_attributes=True) for row in res_orm
            ]
            print(result_dto)
            return result_dto
