import unittest
import ageCalc

class Test_ageCalc(unittest.TestCase):
  def test_expected_data(self):
    test_param = 1974
    result = ageCalc.calculateAge(test_param)
    self.assertEqual(result,49)
    
  def test_incorrect_type(self):
    test_param = "some String"
    result = ageCalc.calculateAge(test_param)
    self.assertIsInstance(result,ValueError)
    
  def test_none_input(self):
    test_param = None
    result = ageCalc.calculateAge(test_param)
    self.assertEqual(result,'Please enter a number')
  def presence_check_test(self):
    test_param = ''
    result = ageCalc.calculateAge(test_param)
    self.assertEqual(result,'Please enter a number')
#running the test
if __name__ =='__main__':
  unittest.main()