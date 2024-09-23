import csv

class User:
    def __init__(self, username, user_id, firstname, lastname, status):
        self.username = username
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.status = status  

    def __repr__(self):
        return (f"User(username={self.username}, user_id={self.user_id}, "
                f"firstname={self.firstname}, lastname={self.lastname}, "
                f"status={self.status})")

class Access_Data:
    pass

class User_Data_Processor:
    def __init__(self, file_path='Python_Workshop/week7/username.csv'):
        self.file_path = file_path
        self.users = []
        self.ids = set()
        self.load_data()

    def load_data(self):
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            
            for row in reader:
                username, user_id, firstname, lastname, status = row
                self.ids.add(user_id)
                self.users.append(User(username, user_id, firstname, lastname, status))

    def count_users(self):
        return len(self.users)

    def list_ids(self):
        return list(self.ids)

    def sorted_users(self):
        return sorted(self.users, key=lambda u: (u.username, u.user_id, u.lastname))

    def active_users(self):
        return [user for user in self.users if user.status == 'active']

    def inactive_users(self):
        return [user for user in self.users if user.status == 'inactive']

    def print_count(self):
        print(f'Anzahl der Personen: {self.count_users()}')

    def print_ids(self):
        print('Benutzte IDs:')
        for user_id in self.list_ids():
            print(user_id)

    def print_sorted_users(self):
        print('Sortierte Liste (username; ID, Lastname):')
        for user in self.sorted_users():
            print(f'{user.username}; {user.user_id}, {user.lastname}')

    def print_active_users(self):
        print('Aktive Benutzer:')
        for user in self.active_users():
            print(f'{user.username}; {user.user_id}, {user.lastname}')

    def print_inactive_users(self):
        print('Inaktive Benutzer:')
        for user in self.inactive_users():
            print(f'{user.username}; {user.user_id}, {user.lastname}')

def main():
    processor = User_Data_Processor()
    processor.print_count()
    processor.print_ids()
    processor.print_sorted_users()
    processor.print_active_users()
    processor.print_inactive_users()

if __name__ == '__main__':
    try:
        main()
    except:
        pass