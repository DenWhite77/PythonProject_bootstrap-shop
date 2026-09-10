import unittest
from urllib.parse import parse_qs


class TestServer(unittest.TestCase):

    def test_parse_post_data(self):
        post_data = "name=Denis&email=denis%40mail.ru&message=Hello"

        data = parse_qs(post_data)

        self.assertEqual(data["name"][0], "Denis")
        self.assertEqual(data["email"][0], "denis@mail.ru")
        self.assertEqual(data["message"][0], "Hello")


if __name__ == "__main__":
    unittest.main()
