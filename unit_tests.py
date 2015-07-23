# Let's write some tests for a nightly build

import unittest
from app import gameloop

class TestGameLoop(unittest.TestCase):
    def test_gameloop(self):
      #self.assertTrue(gameloop())
      with self.assertRaises(SystemExit):
        gameloop()