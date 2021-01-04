class Node:
  def __init__(self,value,explored: bool = False):
    """
    @param value: the value that the node represents
    @params neighbors: list of the values of the neighbors
    """
    self.value = value 
    self.explored = explored

  def has_been_discovered(self):
    self.explored = True 
    #will be utilized in the path finding function

class Line:
  def __init__(self, first_node,list_of_neighbors): 
    """Represents the relationships (neighbors) of a node 
    NOTE: THIS DOES NOT REPRESENT AN EDGE, BUT RATHER, A COLLECTION OF RELATED EDGES
    """
    self.first_node = first_node #the node that this line represents (first_node is kind of a misnomer, sorry about that )
    self.list_of_neighbors = list_of_neighbors #a list of the neighbors 
  
  def println(self): 
    #prints the line
    print(str(self.first_node.value) +" -> ",end="[")
    for i in self.list_of_neighbors[0:len(self.list_of_neighbors)-1]: 
      print(str(i.value),end=", ")
    print(str(self.list_of_neighbors[len(self.list_of_neighbors)-1].value),end="]")


class Graph: 
  def __init__(self,node_list:list):
    #put in your lines 
    self.node_list = node_list

  def is_there_a_path(self,starting_line:Line, ending_node:Node,list_of_nodes = []): 
    #if we've reached the target, return true (we're done, there 
    #clearly is a path)
    if starting_line.first_node.value == ending_node.value:
      return True
    #If we're running this function, the starting_line's node must have 
    #been found / discovered, so we don't want to find it again and get 
    #stuck in a loop
    # set has been discovered to true 
    starting_line.first_node.has_been_discovered()
    # put that node in our list (so we know to come back to it if we 
    #reach a dead end )
    list_of_nodes.append(starting_line)
    
    #we're going to see if we have any unexplored nodes that are connected to our starting_line
    # node 
    new_node_to_search = None 
    for edges in starting_line.list_of_neighbors:
      if not edges.explored:
        new_node_to_search = edges
        break 
        # ^ if we found an unexplored node, let's stop looking for
        # an unexplored edge (break) and roll with that edge
        
    #if we didn't find an unexplored edge ...
    if new_node_to_search == None: 
      #remove this node (because we checked and there was nothing new, so let's remove it so we don't look at it again and waste time)
      list_of_nodes.pop()
      #if the node is (basically) empty, we have exhausted all our options and there is no path from the starting node to the ending node
      if len(list_of_nodes) <=1:
        return False

      #if we didn't find an unexplored edge for this node, but we have other nodes to try, let's
      # circle back to a node we found earlier and see if we have any options left there  
      else:
        list_of_nodes.pop()
        return self.is_there_a_path(list_of_nodes[-1],ending_node,list_of_nodes)

    #if we did find new node connected to our current node, and it matches our target, 
    # hooray! We've reached our goal (and therefore there is a path) 
    if new_node_to_search.value == ending_node.value: 
      return True 
    #if we found a non-target, connected node, let's roll with that new node and see
    # what new connections we can find from it
    else: 
      for y in self.node_list:
        if y.first_node.value == new_node_to_search.value:
          return self.is_there_a_path(y,ending_node,list_of_nodes)
          break
            
#testing
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
G = Node("G")
l1 = Line(A, [B,C,D])
l2 = Line(B, [A,E])
l3 = Line(C,[A])
l4 = Line(D,[A,E])
l5 = Line(E,[B,D])
l6 = Line(G,[])
g = Graph([l1,l2,l3,l4,l5])

print(g.is_there_a_path(l2,G))
