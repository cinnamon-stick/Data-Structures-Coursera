## This file can be used to determine if a directional graph is cyclical or acyclical ##
#Step 0: Import relevant classes ________________________________________________________
import unittest

#Step 1: Create Node class ________________________________________________________
class Node: 
  def __init__(self, value, explored:bool = False, burned:bool = False ):
    self.value = value 
    self.explored = explored 
    self.burned = burned
  #burn + explored will be utilized in the cyclical test algorithm 
  def burn(self):
    self.burned = True
  def has_explored(self): 
    self.explored = True 
  def reset(self):
    self.burned = False
    self.explored = False 

#Step 2: Create Line class ________________________________________________________
class Line: 
  def __init__(self, this_node:Node, entry_nodes:list, exit_nodes:list): 
    #entry nodes - the ones that have edges that lead to the current node (not strictly necessary but enhances clarity) 
    # ^ all functions can work without an entry_nodes list 
    #exit nodes - the edges of the current node that lead out
    #this node - the line that this current node represents
    self.this_node = this_node
    self.exit_nodes = exit_nodes
    self.entry_nodes = entry_nodes 
  
  def print_line(self): 
    #print the entry nodes (the nodes that lead to the current node)
    #if there are entry nodes print them out
    if len(self.entry_nodes) != 0: 
      print("[",end="")
      for i in self.entry_nodes[0:len(self.entry_nodes)-1]: 
        print(str(i.value),end=", ")
      print(str(self.entry_nodes[len(self.entry_nodes)-1].value),end="] -> ")
    #if there are no entry nodes
    else: 
      print("[] ->",end="")
    
    #print this node
    print(self.this_node.value,end=" -> ")
    
    #if there are exit nodes print them out
    if len(self.exit_nodes) != 0: 
      print("[",end="")
      for e in self.exit_nodes[0:len(self.exit_nodes)-1]: 
        print(str(e.value),end=", ")
      print(str(self.exit_nodes[len(self.exit_nodes)-1].value),end="]\n")
    else:
      print("[]")

#Step 3: Create Graph class and cyclical tester algorithm ______________________________
class Graph: 
  def __init__(self, line_list:list):
    self.line_list = line_list
  
  def cyclical_tester(self, starting_ln=None,list_of_predecessors=[]):
    """
    is there a cycle in the graph? (AKA is the graph a DAG [Directioal, Acyclical Graph])
    Do not enter any paramenters (starting_ln and list_of_predecessors) - those variables are for the recursion 
    Cycles occur when we reach a node that has already been explored   
    O(|V|*|E|) time (I believe amortized time is better)
    """
    
    if len(self.line_list) == 0:
      raise ValueError("The graph is empty...")

    if starting_ln == None: 
      starting_ln = self.line_list[0]
    
    starting_ln.this_node.has_explored() 
    next_up_node = None 
    if len(starting_ln.exit_nodes) != 0: 
      for i in starting_ln.exit_nodes:
        if not i.burned:
          next_up_node = i 
          break
    if next_up_node == None:
      starting_ln.this_node.burn() 
      if len(list_of_predecessors) != 0 : 
        return self.cyclical_tester(list_of_predecessors.pop(),list_of_predecessors)
      else: 
        self.reset()
        return False 
    else:
      if next_up_node.explored:
        self.reset()
        return True
      else: 
        new_starting_line = self.find_line(next_up_node)
        list_of_predecessors.append(starting_ln) 
        return self.cyclical_tester(new_starting_line,list_of_predecessors)
  
  #helper functions
  def find_line(self,a_node): 
    # O(|V|) time 
    for i in self.line_list: 
      if i.this_node.value == a_node.value: 
        return i
    raise ValueError("I don't think that node was in the list.")

  def reset(self): 
    #if you want to run cyclical_tester on a graph multiple
    # times, you have to reset the graph before you can do it 
    for i in self.line_list: 
      i.this_node.reset()
    # O(|V|) time 

#Step 4: testing & debugging ____________________________________________________________
class testing(unittest.TestCase): 
  def test_single_node(self):
    G = Node("G")
    gLine = Line(G,[],[])
    my_graph = Graph([gLine])
    self.assertEqual(my_graph.cyclical_tester(),False)

class testing_1(unittest.TestCase):
  def test_acyclic(self): 
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E") 

    aLine = Line(A,[],[B,E])
    bLine = Line(B,[A,E], [C,D])
    cLine = Line(C,[B],[])
    dLine = Line(D,[B],[])
    eLine = Line(E,[A],[B])
    
    g1 = Graph([aLine, bLine,cLine,dLine,eLine])
    self.assertEqual(g1.cyclical_tester(),False)
  
class testing_2(unittest.TestCase):
  def test_cyclic(self):
    A = Node("A")
    B = Node("B")

    aLine = Line(A,[B],[B])
    bLine = Line(B,[A],[A])

    this_graph = Graph([aLine,bLine])
    self.assertEqual(this_graph.cyclical_tester(),True)

    
if __name__ == '__main__':
  unittest.main()
