import unittest
import pk

class Sample(unittest.TestCase):
    def setUp(self):
        self.a=30
        self.b=10

    def tearDown(self):
        print("end")    
    def test_add(self):
        print("addition")
        result = pk.add(self.a,self.b)
        self.assertEqual(result,self.a+self.b)
        print(self.a+self.b)

    def test_sub(self):
        print("subtraction")
        result = pk.sub(self.a,self.b)
        self.assertEqual(result,self.a-self.b)
        print(self.a-self.b)
      
       

if __name__=='__main__':
    unittest.main()    