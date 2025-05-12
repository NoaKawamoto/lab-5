from dataclasses import dataclass, field
import unittest

@dataclass
class BubbleSort:
    def bubble_sort(self, arr: list[int]):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.sorter = BubbleSort()

    def test_unsorted(self):
        arr = [6, 3, 2, 9, 1]
        expected = [1, 2, 3, 6, 9]
        self.sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_reverse(self):
        arr = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        self.sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_duplicates(self):
        arr = [4, 1, 1, 9, 4]
        expected = [1, 1, 4, 4, 9]
        self.sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_single(self):
        arr = [9]
        expected = [9]
        self.sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_empty_list(self):
        arr = []
        expected = []
        self.sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

if __name__ == "__main__":
    unittest.main()

