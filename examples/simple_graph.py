#!/usr/bin/python3

from graphviz import Digraph


class SimpleGraph:

    def __init__(self):
        pass

    def simpleGraph(self):
        dot = Digraph(comment='The Round Table')
        dot.node('P', 'Khirod')
        dot.node('C1', 'Kshyama')
        dot.node('C2', 'Krishya')

        #dot.edges(['PC1', 'PC2'])
        dot.edge('C1', 'C2', constraint='false')

        return dot

    def drawGraph(self):
        self.simpleGraph().render('test-output/round-table.gv', view=True)

    def printGraphSource(self):
        print(self.simpleGraph())


g = SimpleGraph()
print(g)
#g.printGraphSource()
g.drawGraph()
