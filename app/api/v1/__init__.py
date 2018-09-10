from flask import Blueprint

from app.api.v1 import book, user


# 注册v1版本的蓝图
def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    book.api.register(bp_v1)
    user.api.register(bp_v1)

    return bp_v1