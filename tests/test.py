from program import VkApi
import unittest

with open(r'token.txt', 'r', encoding='windows-1251') as f:
    access_token = f.read()
api = VkApi(access_token)


class ApiTests(unittest.TestCase):
    def test_friends(self):
        id = 38940203
        friends = VkApi(access_token).get_friends(id)
        self.assertEqual(17, len(friends))

    def test_closed_friends(self):
        id = 1
        friends = VkApi(access_token).get_closed_friends(id)
        self.assertEqual(0, len(friends))


if __name__ == '__main__':
    unittest.main()
