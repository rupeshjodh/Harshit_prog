import unittest
class TestCaseDemo(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("setUpClass method execution...!")

    def setUp(self):
        print("setUp method execution....!")

    def test_method1(self): # it should be prefix with test
        print("test method execution.....!")
        print(10/0)
    # def test_method2(self): # it should be prefix with test
    #     print("test method2 execution.....!")

    # def test_method3(self): # it should be prefix with test
    #     print("test method3 execution.....!")    

    # def test_method4(self): # it should be prefix with test
    #     print("test method4 execution.....!")   

    def tearDown(self):
        print("tearDown method execution...!")

    # @classmethod
    # def tearDownClass(cls):
    #     print("tearDownClass method execution...!")

unittest.main()
