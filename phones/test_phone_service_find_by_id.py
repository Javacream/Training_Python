import unittest
from phone_service import PhoneService
from phone import Phone

class PhoneServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phone_service = PhoneService()
        self.phone_service.phones[666] = Phone(666, 'test-name', 'test-description')
    def test_id_666_finds_phone(self):
        id = 666
        phone = self.phone_service.find_by(id)
        self.assertEqual('test-name', phone.name)
        self.assertEqual('test-description', phone.description)
    def test_id_1_finds_none(self):
        id = 1
        phone = self.phone_service.find_by(id)
        self.assertIsNone(phone)

if __name__ == '__main__':
    unittest.main()