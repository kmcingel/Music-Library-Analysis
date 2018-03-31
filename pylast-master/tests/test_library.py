#!/usr/bin/env python
"""
Integration (not unit) tests for pylast.py
"""
import unittest

import pylast

from .test_pylast import PyLastTestCase


class TestPyLastLibrary(PyLastTestCase):

    def test_repr(self):
        # Arrange
        library = pylast.Library(user=self.username, network=self.network)

        # Act
        representation = repr(library)

        # Assert
        self.assertTrue(representation.startswith("pylast.Library("))

    def test_str(self):
        # Arrange
        library = pylast.Library(user=self.username, network=self.network)

        # Act
        string = str(library)

        # Assert
        self.assertTrue(string.endswith("'s Library"))

    def test_library_is_hashable(self):
        # Arrange
        library = pylast.Library(user=self.username, network=self.network)

        # Act/Assert
        self.helper_is_thing_hashable(library)

    def test_cacheable_library(self):
        # Arrange
        library = pylast.Library(self.username, self.network)

        # Act/Assert
        self.helper_validate_cacheable(library, "get_artists")

    def test_get_user(self):
        # Arrange
        library = pylast.Library(user=self.username, network=self.network)
        user_to_get = self.network.get_user(self.username)

        # Act
        library_user = library.get_user()

        # Assert
        self.assertEqual(library_user, user_to_get)


if __name__ == '__main__':
    unittest.main(failfast=True)
