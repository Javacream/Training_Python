from dvdp import DVD

class DVDService:
    def __init__(self) -> None:
        self.dvd = dict()
    def create(self, id, name, description):
        if id == None or name == None or description == None:
            raise Exception(f'alle paramter muessen gestzt sein')
        if id in self.dvds.keys():
            raise Exception(f'{id} is nicht da' )
        new_dvd = DVD(id, name, description)
        self.dvd[id] = new_dvd
    def find_by(self, id):
        if id == None:
            raise Exception(f'id muss schon sein!')
        return self.dvds.get(id)