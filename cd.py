class CD:
    def __init__(self, cd_id, name, description):
        if not name:
            raise ValueError("Der Name darf nicht leer sein.")
        self.cd_id = cd_id
        self.name = name
        self.description = description

class CDManagement:
    def __init__(self):
        self.cds = {}

    def add_new_cd(self, cd_id, name, description):
        if cd_id in self.cds:
            raise ValueError("Eine CD mit dieser ID existiert bereits.")
        self.cds[cd_id] = CD(cd_id, name, description)
        print(f"CD '{name}' mit ID {cd_id} wurde hinzugefügt.")

    def search_new_cd(self, cd_id):
        if cd_id in self.cds:
            cd = self.cds[cd_id]
            return f"ID: {cd.cd_id}, Name: {cd.name}, Beschreibung: {cd.description}"
        else:
            return f"Keine CD mit der ID {cd_id} gefunden."
        
import pytest

class TestCDManagement:
    @pytest.fixture
    def management(self):
        return CDManagement()

    def test_add_cd(self, management):
        management.add_new_cd(1, "Album A", "Beschreibung of Album A")
        assert len(management.cds) == 1
        assert management.cds[1].name == "Album A"

    def test_add_cd_duplicate_id(self, management):
        management.add_new_cd(1, "Album A", "Beschreibung of Album A")
        with pytest.raises(ValueError):
            management.add_new_cd(1, "Album B", "Beschreibung of Album B")

    def test_add_cd_empty_name(self, management):
        with pytest.raises(ValueError):
            management.add_new_cd(2, "", "Beschreibung of Album B")

    def test_search_cd_exists(self, management):
        management.add_new_cd(1, "Album A", "Beschreibung of Album A")
        result = management.search_new_cd(1)
        assert result == "ID: 1, Name: Album A, Beschreibung: Beschreibung of Album A"

    def test_search_cd_not_exists(self, management):
        result = management.search_new_cd(999)
        assert result == "Keine CD mit der ID 999 gefunden."
        
def main():
    management = CDManagement()


    management.add_new_cd(1, "Album A", "Beschreibung von Album A")
    management.add_new_cd(2, "Album B", "Beschreibung von Album B")


    print(management.search_new_cd(1))
    print(management.search_new_cd(3))  # Beispiel für nicht vorhandene ID

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Programm manuell beendet")