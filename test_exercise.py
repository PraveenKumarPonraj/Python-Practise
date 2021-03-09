import unittest
import exercise

class ElevatorTest(unittest.TestCase):
    

    def test_input_user(self):
        self.assertNotEqual(4,3,msg=None)
        print("not equal")


if __name__=='__main__':
    unittest.main()        