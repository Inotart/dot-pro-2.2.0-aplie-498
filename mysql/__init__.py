"本库只是存储了mysql的数据库账号密码"
class user:
    host=''
    port=0
    user=''
    password=''
    db=''
    charset=''
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        raise Exception("你不应该修改这个!")
class slob:
    host=''
    port=0
    user=''
    password=''
    db=''
    charset=''
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        raise Exception("你不应该修改这个!")
class slob_type:
    host=''
    port=0
    user=''
    password=''
    db=''
    charset=''
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        raise Exception("你不应该修改这个!")
class at:
    host=''
    port=0
    user=''
    password=''
    db=''
    charset=''
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        raise Exception("你不应该修改这个!")