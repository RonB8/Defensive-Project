import uuid




class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_name(self):
        return self.__name


class Users:
    def __init__(self):
        self.users_list = []
        self.id_list = []

    def register(self, name: str):
        if any(usr.get_name() == name for usr in self.users_list):
            return None

        new_uuid = uuid.uuid4()
        while new_uuid in self.id_list:
            new_uuid = uuid.uuid4()

        new_user = User(new_uuid, name)
        self.users_list.append(new_user)
        return new_uuid

    def exist(self, name) -> bool:
        for user in self.users_list:
            if user.get_name() == name:
                return True
        return False
