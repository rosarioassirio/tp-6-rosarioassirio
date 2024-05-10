import unittest.mock
import lists as ex1


class TP6ListsCases(unittest.TestCase):

    def test_remove_elements(self):
        list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        result1 = ex1.remove_elements(list1)
        expected1 = ['Green', 'White', 'Black']
        self.assertEqual(expected1, result1)

        list2 = ['Audi', 'BMW', 'Porsche', 'Aston Martin']
        result2 = ex1.remove_elements(list2)
        expected2 = ['BMW', 'Porsche', 'Aston Martin']
        self.assertEqual(expected2, result2)

        list3 = []
        result3 = ex1.remove_elements(list3)
        expected3 = []
        self.assertEqual(expected3, result3)

    def test_add_elements(self):
        list1 = ['Red', 'Green', 'White', 'Black']
        result1 = ex1.add_elements(list1)
        expected1 = ['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']
        self.assertEqual(expected1, result1)

        list2 = []
        result2 = ex1.add_elements(list2)
        expected2 = ['Pink', 'Yellow']
        self.assertEqual(expected2, result2)

        list3 = [0, 1, 2]
        result3 = ex1.add_elements(list3)
        expected3 = ['Pink', 0, 1, 2, 'Yellow']
        self.assertEqual(expected3, result3)

    def test_is_empty(self):
        list1 = []
        result1 = ex1.is_empty(list1)
        self.assertTrue(result1)

        list2 = ["Red", "Green", "White", "Black"]
        result2 = ex1.is_empty(list2)
        self.assertFalse(result2)

        list3 = [1, 2]
        result3 = ex1.is_empty(list3)
        self.assertFalse(result3)

        list4 = [True]
        result4 = ex1.is_empty(list4)
        self.assertFalse(result4)

    def test_check_lists(self):
        list1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
        list2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
        result1 = ex1.check_lists(list1, list2)
        self.assertTrue(result1)

        list3 = ['Black', 'Pink', 'Green', 'White']
        list4 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
        result2 = ex1.check_lists(list3, list4)
        self.assertFalse(result2)

        list5 = ['Black', 'Pink']
        list6 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
        result3 = ex1.check_lists(list5, list6)
        self.assertFalse(result3)

        list7 = ['Black', 'Pink', 'Green', 'White']
        list8 = ['Red']
        result4 = ex1.check_lists(list7, list8)
        self.assertFalse(result4)

    def test_list_of_lists(self):
        list_of_lists1 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
        result1 = ex1.list_of_lists(list_of_lists1)
        expected1 = [[1, 2], [5, 6, 7], [11, 12]]
        self.assertEqual(expected1, result1)

        list_of_lists2 = [[], [4, 5, 6], [10, 11, 12]]
        result2 = ex1.list_of_lists(list_of_lists2)
        expected2 = [[], [5, 6], [11, 12]]
        self.assertEqual(expected2, result2)

        list_of_lists3 = [[1, 2], [], [12]]
        result3 = ex1.list_of_lists(list_of_lists3)
        expected3 = [[1, 2], [], [12]]
        self.assertEqual(expected3, result3)

        list_of_lists4 = [[1], [4], []]
        result4 = ex1.list_of_lists(list_of_lists4)
        expected4 = [[1], [], []]
        self.assertEqual(expected4, result4)


if __name__ == '__main__':
    unittest.main()
