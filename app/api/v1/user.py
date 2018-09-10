from app.libs.redprint import Redprint

# 实例化红图
api = Redprint('user')

@api.route('', methods=['GET'])
def get_user():
    return 'get user'


@api.route('', methods=['POST'])
def create():
    return 'create user'