import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_base_model_init(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertIsInstance(b1.id, str)

    def test_base_model_str(self):
        b1 = BaseModel()
        b1_str = str(b1)
        self.assertEqual(b1_str, f"[BaseModel] ({b1.id}) {b1.__dict__}")

    def test_base_model_save(self):
        b1 = BaseModel()
        updated_at = b1.updated_at
        b1.save()
        self.assertGreater(b1.updated_at, updated_at)

    def test_base_model_to_dict(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict["id"], str)
        self.assertIsInstance(b1_dict["created_at"], str)
        self.assertIsInstance(b1_dict["updated_at"], str)
        self.assertIsInstance(b1_dict["__class__"], str)
        self.assertEqual(b1_dict["__class__"], "BaseModel")

if __name__ == '__main__':
    unittest.main()
