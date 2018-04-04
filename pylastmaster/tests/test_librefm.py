#!/usr/bin/env python
"""
Integration (not unit) tests for pylast.py
"""
import unittest

from flaky import flaky

import pylast

from .test_pylast import load_secrets


@flaky(max_runs=5, min_passes=1)
class TestPyLastWithLibreFm(unittest.TestCase):
    """Own class for Libre.fm because we don't need the Last.fm setUp"""

    def test_libre_fm(self):
        # Arrange
        secrets = load_secrets()
        username = secrets["username"]
        password_hash = secrets["password_hash"]

        # Act
        network = pylast.LibreFMNetwork(
            password_hash=password_hash, username=username)
        artist = network.get_artist("Radiohead")
        name = artist.get_name()

        # Assert
        self.assertEqual(name, "Radiohead")

    def test_repr(self):
        # Arrange
        secrets = load_secrets()
        username = secrets["username"]
        password_hash = secrets["password_hash"]
        network = pylast.LibreFMNetwork(
            password_hash=password_hash, username=username)

        # Act
        representation = repr(network)

        # Assert
        self.assertTrue(representation.startswith("pylast.LibreFMNetwork("))


if __name__ == '__main__':
    unittest.main(failfast=True)
