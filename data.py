
class Request:
    def __init__(self, client_ID, version, code, payload_size, payload):
        self.client_ID = client_ID
        self.version = version
        self.code = code
        self.payload_size = payload_size
        self.payload = payload
    
    REGISTRY = 825
    SEND_PUBLIC_KEY = 826
        


class Payload:
    pass


class UUID:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    

class UUIDCollection:
    def __init__(self):
        self.uuid_list = []

    def add(self, uuid_obj: UUID):
        self.uuid_list.append(uuid_obj)

    def exist(self, user_name) ->bool:
        for user in self.uuid_list:
            if user.name == user_name:
                return True
        return False


