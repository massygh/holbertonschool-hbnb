#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
from model.place import Place
from persistence.ipersistence_manager import IPersistenceManager
from persistence.place_repository import PlaceRepository
# Modification du sys.path
sys.path.append(os.path.abspath
                (os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath
                (os.path.join(os.path.dirname(__file__), '..', '..', 'model')))
sys.path.append(os.path.abspath
                (os.path.join
                 (os.path.dirname(__file__), '..', '..', 'persistence')))


class TestPlaceRepository(unittest.TestCase):
    def setUp(self):
        self.repository = PlaceRepository()
        self.place1 = Place("Place 1", "Description 1")
        self.place2 = Place("Place 2", "Description 2")
        self.repository.save(self.place1)
        self.repository.save(self.place2)

    def test_save(self):
        place3 = Place("Place 3", "Description 3")
        self.repository.save(place3)
        self.assertEqual(len(self.repository.get_all()), 3)

    def test_get(self):
        place = self.repository.get(self.place1.place_id)
        self.assertEqual(place, self.place1)

    def test_get_all(self):
        places = self.repository.get_all()
        self.assertEqual(len(places), 2)

    def test_update(self):
        updated_data = {"name": "Updated Place",
                        "description": "Updated Description"}
        self.repository.update(self.place1.place_id, updated_data)
        place = self.repository.get(self.place1.place_id)
        self.assertEqual(place.name, "Updated Place")
        self.assertEqual(place.description, "Updated Description")

    def test_delete(self):
        self.repository.delete(self.place1.place_id)
        self.assertEqual(len(self.repository.get_all()), 1)


if __name__ == '__main__':
    unittest.main()