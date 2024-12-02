import unittest

class practive(unittest.TestCase):
    def test_assertequal(self):
        result = 3
        
        self.assertequal(result,9,"Right its equal")

    def test_asserttrue(self):
        add = 4

        self.asserttrue(add % 2 == 0, "This will return 0")

    
if __name__ == "__main__":
    unittest.main()
