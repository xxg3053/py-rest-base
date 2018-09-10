from app.libs.redprint import Redprint

# 实例化红图
api = Redprint('book')

@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create():
    return 'create book'