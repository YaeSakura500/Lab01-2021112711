import unittest
import networkx as nx
import random
from cul import cul  # 确保导入您的类


class TestRandomWalk(unittest.TestCase):
    def setUp(self):
        # 创建一个图和cul实例以供测试
        self.G = nx.DiGraph()
        self.G.add_nodes_from([0, 1, 2])
        self.G.add_edge(0, 1)
        self.G.add_edge(1, 2)
        self.adj_mat = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
        self.word2node = {'a': 0, 'b': 1, 'c': 2}
        self.node2word = {0: 'a', 1: 'b', 2: 'c'}
        self.cul_instance = cul(self.G, self.adj_mat, self.word2node, self.node2word)

    def test_random_walk_no_out_edges(self):
        # 测试没有出边的情况
        self.G.remove_edge(1, 2)
        self.G.remove_edge(0, 1)
        # 重新创建cul实例
        updated_cul_instance = cul(self.G, self.adj_mat, self.word2node, self.node2word)
        result = updated_cul_instance.random_walk()
        self.assertIn(result, ['a', 'b', 'c'])

    def test_random_walk_with_out_edges(self):
        # 测试正常情况，有出边可以遍历
        result = self.cul_instance.random_walk()
        self.assertIn(result, ['a b c', 'b c', 'c'])

    def test_random_walk_edge_visited(self):
        # 测试边被访问过的情况
        self.G.add_edge(2, 0)
        result = self.cul_instance.random_walk()  # 第二次调用
        self.assertIn(result, ['a b c a', 'b c a b', 'c a b c'])


if __name__ == '__main__':
    unittest.main()
