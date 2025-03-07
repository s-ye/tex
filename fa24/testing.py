from sage.all import *
from sage.combinat.diagram import RotheDiagram


pi = Permutation([3, 1, 5, 7, 4, 2, 6, 8])

rothe_diagram = RotheDiagram(pi)

rothe_diagram.pp()
