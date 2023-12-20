from sqlalchemy import delete, insert, select
from sqlalchemy.orm import subqueryload,load_only

from dbsession import get_session
from helper import get_only_selected_fields, get_valid_data
from models import user_model
from scalars.user_scalar import AddUser, User, UserDeleted, UserExists, UserNotFound


async def get_users(info):
    """ Get all users resolver """
    selected_fields = get_only_selected_fields(user_model.User,info)
    async with get_session() as s:
        sql = select(user_model.User).options(load_only(*selected_fields)) \
        .order_by(user_model.User.name)
        db_users = (await s.execute(sql)).scalars().unique().all()

    users_data_list = []
    for user in db_users:
        user_dict = get_valid_data(user,user_model.User)
        users_data_list.append(User(**user_dict))

    return users_data_list

async def get_user(user_id, info):
    """ Get specific user by id resolver """
    selected_fields = get_only_selected_fields(user_model.User,info)
    async with get_session() as s:
        sql = select(user_model.User).options(load_only(*selected_fields)) \
        .filter(user_model.User.id == user_id).order_by(user_model.User.name)
        db_user = (await s.execute(sql)).scalars().unique().one()
    
    user_dict = get_valid_data(db_user,user_model.User)
    return User(**user_dict)

async def delete_user(user_id):
    """ Delete user resolver """
    async with get_session() as s:
        sql = select(user_model.User).where(user_model.User.id == user_id)
        existing_db_user = (await s.execute(sql)).first()
        if existing_db_user is None:
            return UserNotFound()

        query = delete(user_model.User).where(user_model.User.id == user_id)
        await s.execute(query)
        await s.commit()
    
    return UserDeleted()