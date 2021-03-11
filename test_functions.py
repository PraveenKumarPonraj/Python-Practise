import unittest
import functions
class Testfunc(unittest.TestCase):
    def test_my_function(self):
        
        self.assertEqual(functions.end,5)
        self.assertEqual(functions.start,0)
        

    def test_my_function(self):
        end = 5
        user_input = 4
        
        message="incorrect try again "

        self.assertLess(user_input,end,message)

    

if __name__ == '__main__':
    unittest.main()