#!/usr/bin/python3
"""Test cases for the BaseModel class"""
import unittest
import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""

    def test_module_documentation(self):
        """Test documentation for the module"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_constructor_documentation(self):
        """Test documentation for the constructor"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        """Test creation of class and to_dict"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):
        """Test dictionary model"""
        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Andres"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Andres")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
            }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

    def test_datetime_model(self):
        """Test datetime in base model"""
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)

    def test_uuid(self):
        """Test different uuids"""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_string_representation(self):
        """Test the magic method __str__"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id

        expected = '[BaseModel] ({}) {}'\
                   .format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    def test_constructor_kwargs(self):
        """Test constructor with kwargs as attribute values"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        json_attributes = obj.to_dict()

        obj2 = BaseModel(**json_attributes)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)

    def test_file_save(self):
        """Test that information is saved to file"""
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())

if __name__ == '__main__':
    unittest.main()