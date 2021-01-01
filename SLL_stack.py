#Stack with singly linked list implementation 
#Uses a stack to scan strings to see if they use parentheses right 
class SLL: 
  #Singly Linked List Node (inner class) ---------------------
  class SLLNode:
    #Constructor
    def __init__(self,data,next_node=None):
      self.data = data
      self.next_node = next_node
    #Get value of item 
    def get_data(self):
      return self.data
    #get the next node 
    def get_next_node(self):
      return self.next_node
    #Set the next node 
    def set_next_node(self,new_next_node):
      self.next_node = new_next_node

  #Singly Linked List ----------------------------------------------
  #Constructor 
  def __init__(self,head = None):
    self.head = self.SLLNode(head)

  #Display 
  def display(self):
    curr_node = self.head
    print("HEAD:",end = " ")
    print(str(curr_node.get_data()),end=" ")  
    for i in range(self.return_size()-1):
      curr_node = curr_node.get_next_node()
      print(str(curr_node.get_data()),end=" ")  
      
  #pop (return last entered element)
  def pop(self):
    returning = self.head 
    previous = self.head.get_next_node()
    self.head = previous 
    return returning 
  
  #Insert a new item in the list 
  def insert(self, data): 
    new_node = self.SLLNode(data)
    if self.head == None: 
      self.head = new_node
    else: 
      new_node.set_next_node(self.head)
      self.head = new_node
  
  #Get the size of the list 
  def return_size(self):
    current_node = self.head 
    size = 0 
    while current_node != None and current_node.get_data()!=None: 
      size += 1
      current_node = current_node.get_next_node()
    return int(size)
  
  #Remove a node 
  def remove_node(self,value_of_node):
    previous = None
    current_node = self.head 
    found = False
    while current_node != None and found == False:
      if current_node.get_data() == value_of_node:
        found = True 
      else: 
        previous = current_node
        current_node = current_node.get_next_node()
    if current_node == None:
      raise ValueError("Error: not in list")
    elif previous == None: 
      self.head = current_node.get_next_node()
    else: 
      previous.set_next_node(current_node.get_next_node())
  
def parathesis_editor(sentance):
  if not isinstance(sentance, str):
    raise ValueError("not a string!")
  list_of_para = SLL()
  for i in range(len(sentance)):
    if sentance[i] == "{" or sentance[i] == "(" or sentance[i] == "[":
      list_of_para.insert(sentance[i])
      
    if sentance[i] == "}" or sentance[i] == ")" or sentance[i] == "]":
      if sentance[i] == "}" and str(list_of_para.head.get_data())=="{":
        list_of_para.pop()
      if sentance[i] == "]" and str(list_of_para.head.get_data())=="[":
        list_of_para.pop()
      if sentance[i] == ")" and str(list_of_para.head.get_data())=="(":
        list_of_para.pop()

  if list_of_para.return_size() == 0:
    return "ALL GOOD! :)"
  elif list_of_para.return_size() > 0: 
    return "NOT OK! "


print(parathesis_editor("[]")) #Should return "ALL GOOD"
print(parathesis_editor("[]{}")) #Should return "ALL GOOD"
print(parathesis_editor("[{}]")) # Should return "ALL GOOD"
print(parathesis_editor("[}")) #Should return "NOT OK"

#TESTING THE SLL 
#nodia = SLL.SLLNode("30")
#my_list = SLL("30")
#my_list.insert("20") 
#my_list.insert("10") 
#my_list.insert("0") 
#my_list.display()
#my_list.remove_node("10")
#my_list.display()
#my_list.pop()
#my_list.display()

      
#new_list = SLL(SLL.SLLNode("30"))
#new_list.display()
#new_list.insert(SLL.SLLNode("20"))
#new_list.insert(SLL.SLLNode("10"))
#new_list.display()
