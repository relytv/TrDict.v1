from base.base import Base
from trainingnote.user.models import User


class UserDAO(Base):
    model = User
