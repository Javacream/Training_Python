import unittest
from phone_service import PhoneService
class PhoneServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phone_service = PhoneService()
    def test_valid_params_creates_phone(self):
        id = 42
        name = 'Google Pixel'
        description = 'an android phone'
        self.phone_service.create(id, name, description)

    def test_existing_id_raises_error(self):
        id = 42
        name = 'Google Pixel'
        description = 'an android phone'
        self.phone_service.create(id, name, description)
        with self.assertRaises(Exception):
            self.phone_service.create(id, name, description)

    def test_none_id_raises_error(self):
        id = None
        name = 'Google Pixel'
        description = 'an android phone'
        with self.assertRaises(Exception):
            self.phone_service.create(id, name, description)
    def test_none_name_raises_error(self):
        id = 42
        name = None
        description = 'an android phone'
        with self.assertRaises(Exception):
            self.phone_service.create(id, name, description)
    def test_none_description_raises_error(self):
        id = 42
        name = 'Google Pixel'
        description = None
        with self.assertRaises(Exception):
            self.phone_service.create(id, name, description)

if __name__ == '__main__':
    unittest.main()