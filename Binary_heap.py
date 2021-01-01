## This file has functions to make a binary heap ##

#Step 0 - import relevant classes  --------------------------------------------------------
import unittest
import math

#Step 1 - implement tools for next function  --------------------------------------------------------

#These functions give you the indexes of the children or parent of a node at index i in an array 
def parent(i: int)->int:
  return math.floor((i-1)/2)
def left_child(i: int) -> int:
  return 2*i + 1
def right_child(i: int) -> int:
  return 2*i + 2
  
#This function swaps two items in a list and returns the list (with the swapped items)
def swap_list(arr:list,index_1:int,index_2:int)-> list:
  arr[index_1],arr[index_2]=arr[index_2],arr[index_1]
  return arr

#Step 2 - institue sift up --------------------------------------------------------
#Swap a node with its parents / ancestors until it is in the right place in the binary heap  
def sift_up(arr:list,index:int)->list:
  i_parent = parent(index)
  if arr[index]>arr[i_parent]:
    new_arr = swap_list(arr,index,i_parent)
    if i_parent != 0: 
      return sift_up(new_arr,i_parent)
    else:
      return arr
  else:
    return arr 

#Step 3 - institute sift down --------------------------------------------------------
#Swap a node with its child / descendants until it is in the right place in the binary heap  
def sift_down(arr:list,index:int)->list:
  right_kid = right_child(index)
  left_kid = left_child(index)
  max_index = index
  if right_kid < len(arr) and arr[right_kid] > arr[max_index]:
    max_index = right_kid
  if left_kid < len(arr) and arr[left_kid] > arr[max_index]:
    max_index = left_kid
  if max_index != index: 
    arr = swap_list(arr,index,max_index)
    return sift_down(arr,max_index)
  else: return arr


#Step 4 - final function --------------------------------------------------------
#Creates the binary heap
def create_binary_heap(arr:list)-> list:
  size = len(arr) 
  for i in range((size-2)//2,-1,-1):
    arr = sift_down(arr,i)
  return arr 

#Step 5 - testing and debugging --------------------------------------------------------
class testing(unittest.TestCase): 
  def test_parent(self): 
    self.assertEqual(parent(2),0)
  def test_sift_up(self):
    self.assertEqual(sift_up([8,7,6,2,10,4,3],4),[10,8,6,2,7,4,3])
  def test_sift_up1(self):
    self.assertEqual(sift_up([10,8,6,9,7,4,3],3),[10,9,6,8,7,4,3])
  def test_sift_down(self):
    self.assertEqual(sift_down([0,7,2,4,5,1,0],0),[7,5,2,4,0,1,0])
  def test_sift_down1(self):
    self.assertEqual(sift_down([8,7,2,5,6,3],1),[8,7,2,5,6,3])
  def test_create_binary_heap(self):
    self.assertEqual(create_binary_heap([8,5,10]),[10,5,8])
    
if __name__ == '__main__':
  unittest.main()
