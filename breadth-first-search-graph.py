# Step 0: Import relevant packages ---------------------------
import unittest 

# Step 1: Implement classes -----------------------------------
class Airport_Node(object):
  """Requirement: total number of nodes < 999"""
  def __init__(self, airport_name:str, discovered:bool = False, parent = None, dist_from_source:int = 999):
    self.airport_name = airport_name
    self.discovered = discovered
    self.parent = None 
    self.dist_from_source = dist_from_source
  
  def set_parent(self,new_parent):
    self.parent = new_parent
  def discover(self): 
    self.discovered = True 
  
class Line: 
  def __init__(self, this_node:Airport_Node, exit_nodes:list): 
    self.this_node = this_node
    self.exit_nodes = exit_nodes
  
  def print_line(self):     
    #print this line
    print(self.this_node.value,end=" -> ")
    if len(self.exit_nodes) != 0: 
      print("[",end="")
      for e in self.exit_nodes[0:len(self.exit_nodes)-1]: 
        print(str(e.value),end=", ")
      print(str(self.exit_nodes[len(self.exit_nodes)-1].value),end="]\n")
    else:
      print("[]")

class Graph: 
  def __init__(self, line_list:list):
    self.line_list = line_list

# Step 2: Implement BFS (Breadth First Search) -------------
  def BFS(self,starting_line): 
    starting_line.this_node.dist_from_source = 0 
    starting_line.this_node.discover() 
    queue = [starting_line] 
    while len(queue) != 0: 
      new_sn = queue.pop()
      for exiting_nodes in new_sn.exit_nodes: 
        if not exiting_nodes.discovered:
          queue.insert(0,self.find_line(exiting_nodes))
          exiting_nodes.dist_from_source = new_sn.this_node.dist_from_source + 1 
          exiting_nodes.parent = new_sn.this_node

  
  def find_line(self, starting_node):
    for i in self.line_list: 
      if i.this_node.airport_name == starting_node.airport_name: 
        return i 
    raise ValueError(str(starting_node.value)+" node was not in the list.")





#Step 3: Testing and debugging ------------------------
class Testing_1(unittest.TestCase): 
  def test_node1(self): 
    a1 = Airport_Node("O'Hare")
    self.assertEqual(a1.dist_from_source,999)
  def test_node2(self): 
    a2 = Airport_Node("NYC")
    a2.discover()
    self.assertEqual(a2.discovered,True)

class Testing_BFS(unittest.TestCase): 
  def test_emptycase(self): 
    a1 = Airport_Node("SFO") 
    l1 = Line(a1,[])
    g1 = Graph([l1])
    g1.BFS(l1)
    self.assertEqual(a1.dist_from_source,0)
  def test_this_case(self): 
    a2 = Airport_Node("San Carlos")
    a3 = Airport_Node("My airport")
    a4 = Airport_Node("Small airport")
    l2 = Line(a2,[a3])
    l3 = Line(a3,[])
    l4 = Line(a4,[])
    g2 = Graph([l2,l3,l4])
    g2.BFS(l2)
    self.assertEqual(a3.dist_from_source, 1)

if __name__ == '__main__':
  unittest.main()
