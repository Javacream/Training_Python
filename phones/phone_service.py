from phone import Phone

class PhoneService:
    def __init__(self) -> None:
        self.phones = dict()
    def create(self, id, name, description):
        if id == None or name == None or description == None:
            raise Exception(f'all params must be set')
        if id in self.phones.keys():
            raise Exception(f'{id} is unavailable' )
        new_phone = Phone(id, name, description)
        self.phones[id] = new_phone
    def find_by(self, id):
        if id == None:
            raise Exception(f'id must be set')
        return self.phones.get(id)