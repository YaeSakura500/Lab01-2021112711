import trans
import cul

m, w2n, n2w=trans.text2matrix()
G = trans.matrix2graph(n2w, m)
trans.showDirectedGraph(G)
mycul = cul.cul(G, m, w2n, n2w)
out = mycul.queryBridgeWords('new', 'and')
print(out)
out2 = mycul.generateNewText("Seek to explore new and exciting synergies")
print(out2)