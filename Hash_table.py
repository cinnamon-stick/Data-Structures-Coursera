class HashTable: 
  #Constructor 
  def __init__(self,x:int,p:int,m:int):
    """
    @param x: randomly chosen # for the hash function
    @param p: huge prime number (>10^7)
    @param m: the cardinality 
    """
    self.x = x 
    self.p = p 
    self.m = m 
    self.table = [[None for e in range(1)] for j in range(m)]
  
  #Table getter
  def get_table(self):
    return self.table

  #Hash table print function
  def print_hash(self):
    print("HASH TABLE:")
    for i in range(self.m):
      print(str(i)+": "+str(self.table[i]))

  #Get the hash function (PRIVATE)
  def __get_hash(self,string)->int:
    s_len = len(string)
    char_list = [] 
    for e in string:
      entering = ord(e)
      char_list.append(entering)
    sum = 0 
    for i in range(s_len): 
      sum+=(char_list[i] * (self.x**i)) % self.p
    sum = sum % self.m
    return sum 

  #Add to the hash table (will SKIP on duplicates)
  def add(self,string, value):
    index = self.__get_hash(string)
    thing_to_add = (string, value)
    if self.table[index][0] == None:
      self.table[index][0] = thing_to_add
      return 
    for i in range(len(self.table[index])):
      if self.table[index][i][0] == string:
        return 
    self.table[index].append(thing_to_add)
  
  #delete a key from the hash table 
  def delete(self,string): 
    index = self.__get_hash(string)
    thing_to_remove = None 
    for i in range(len(self.table[index])):
      if self.table[index][i][0] == string:
        thing_to_remove = self.table[index][i]
        break
    if thing_to_remove !=None:
      self.table[index].remove(thing_to_remove)
      return
    raise Exception("I couldn't find the item to remove")

ht = HashTable(31, 1618402549,3)
ht.add("Hello!",10)
ht.add("This",1000)
ht.add("is",0)
ht.add("my",3)
ht.add("test",99)
ht.add("to",21)
ht.add("see",10)
ht.add("if",1000)
ht.add("this",0)
ht.add("works",3)
ht.add("!",99)
ht.add("!",21) #duplicate - should be deleted
ht.print_hash()
