import unittest
from lab_1 import Programe
class TestPrograme(unittest.TestCase):
  def setUp(self):
    self.somethingTest = Programe()
#Так як у мої функції значення передаються при вводі, то і в тести їх також потрібно вводити з клавіатури. Зарання
  #вводиться лишеочікуваний результат
  def test_equation1(self):
    self.assertEqual(self.somethingTest.equation1(), 49.606)#Ожидаемый результат

  def test_equation2(self):
    self.assertEqual(self.somethingTest.equation2(), 289.475)

  def test_equation3(self):
    self.assertEqual(self.somethingTest.equation3(), 45.456)

  def test_equation4(self):
    self.assertEqual(self.somethingTest.equation4(), 12.942)

if __name__ == "__main__":
  unittest.main()