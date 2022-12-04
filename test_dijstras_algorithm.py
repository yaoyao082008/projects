import unittest
import dijstras_algorithm

class testDijstras(unittest.TestCase):

    def test_shortest_path(self):
        graph={
            'a':[['b',2],['d',8]],
            'b':[['a',2],['d',5],['e',6]],
            'c':[['e',9],['f',3]],
            'd':[['a',8],['b',5],['e',3],['f',2]],
            'e':[['b',6],['d',3],['f',1],['c',9]],
            'f':[['d',2],['e',1],['c',3]],
        }

        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'b',1),2)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'c',1),12)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'d',1),7)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'e',1),8)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'f',1),9)

    def test_graph0(self):
        graph={
            'a':[['c',3],['f',2]],
            'b':[['e',2],['f',6],['g',2],['d',1]],
            'c':[['a',3],['e',1],['f',2]],
            'd':[['c',4],['b',1]],
            'e':[['c',1],['f',3],['b',2]],
            'f':[['a',2],['e',3],['c',2],['g',5]],
            'g':[['f',5],['b',2]]
        }

        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'c',1),3)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'f',1),2)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'e',1),4)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'b',1),6)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'g',1),7)
        self.assertEqual(dijstras_algorithm.shortestPath('a',graph,'d',1),7)
    
    def test_grap2(self):
        graph={}
        self.assertRaises(Exception,dijstras_algorithm.shortestPath,'a',graph,'b',3)

if __name__=='__main__':
    unittest.main()