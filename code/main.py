import unittest
from cul import cul
import trans


class TestCalcShortestPath(unittest.TestCase):
    def setUp(self):
        # 初始化类实例
        sentence = 'To @ explore strange new worlds,\nTo seek out new life and new civilizations?.'
        m, w2n, n2w = trans.text2matrix(sentence)
        G = trans.matrix2graph(n2w, m)
        self.mycul = cul(G, m, w2n, n2w)

    def test_single_word(self):
        # 测试单个单词的情况
        # self.assertIsInstance(self.mycul.calc_shortest_path(['to']), str)
        self.assertEqual(self.mycul.calc_shortest_path(['to']),
                         'Length:1\nto>seek\nLength:4\nto>seek>out>new>worlds\nLength:2\nto>seek>out\nLength:4\nto>seek>out>new>civilizations\nLength:1\nto>explore\nLength:3\nto>seek>out>new\nLength:0\nto\nLength:4\nto>seek>out>new>life\nLength:5\nto>seek>out>new>life>and\nLength:2\nto>explore>strange')

    def test_two_words(self):
        # 测试两个单词的情况
        self.assertEqual(self.mycul.calc_shortest_path(['explore', 'strange']), 'Length:1\nexplore>strange\n')

    def test_no_word_in_graph(self):
        # 测试图中不存在的单词
        self.assertEqual(self.mycul.calc_shortest_path(['ababa']), 'No word1 in the graph!')

    def test_too_many_words(self):
        # 测试输入超过两个单词的情况
        self.assertEqual(self.mycul.calc_shortest_path(['To', 'life', 'and']), 'Too many words in the input')

    def test_no_word1_or_word2_in_graph(self):
        # 测试图中不存在的两个单词
        self.assertEqual(self.mycul.calc_shortest_path(['ababa', 'aaaaaaa']), 'No word1 or word2 in the graph!')

    def test_no_input(self):
        # 测试图中不存在的两个单词
        self.assertEqual(self.mycul.calc_shortest_path([]), 'Invalid input')


if __name__ == '__main__':
    unittest.main()
