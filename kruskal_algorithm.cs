// Step 0: import relevant classes 
using System;
using System.Collections.Generic;

// Step 1: Implement disjointed set class
class DisjointSet 
{
  //field of nodes 
  public List<string> nodes; 

  //constructor
  public DisjointSet(List<string> set_elements){
    nodes = set_elements; 
  }

  // join two sets
  public static DisjointSet Union(DisjointSet set_1, DisjointSet set_2){
    List<string> temp_list = new List<string>();
    for (int e = 0 ; e < set_1.nodes.Count; e++){
      temp_list.Add(set_1.nodes[e]);
    }
    for (int i = 0 ; i < set_2.nodes.Count; i++){
      temp_list.Add(set_2.nodes[i]);
    }
    DisjointSet ds = new DisjointSet(temp_list);
    return ds; 
  }

  //is an item in a set? 
  public bool set_find(string s){
    return nodes.Contains(s); 
  }

  //check if two sets are the same 
  public static bool is_same_set(DisjointSet ds1, DisjointSet ds2) 
  {
    if (ds1.nodes.Count != ds2.nodes.Count)
    {
      return false; 
    }
    
    for (int i = 0 ; i < ds1.nodes.Count; i++)
    {
      if (ds1.nodes[i] != ds2.nodes[i])
      {
        return false; 
      }
    }
    return true; 
  }
}

//Step 2: Implement Graph class 

//Edge class 
class Edge { 
  public string starting_node;
  public int length; 
  public string ending_node;

  public Edge(string s_node,int len,string e_node){
    starting_node = s_node;
    length = len;
    ending_node = e_node;
  }
  
  public void PrintEdge(){
    Console.WriteLine(starting_node +" -> "+ending_node+" | "+Convert.ToString(length)); 
  }

  public static void PrintListEdge(List<Edge> list_edges){
    for (int i = 0 ; i< list_edges.Count; i++){
      list_edges[i].PrintEdge();
    }
  }

  //code for the insert sort from Geeks for Geeks 
  public static List<Edge> sort_edges(List<Edge> list_edges){
    int n = list_edges.Count; 

    for (int i  = 1 ; i< n ; ++i){
      Edge key = list_edges[i];
      int j = i - 1; 

      while (j >= 0 && list_edges[j].length > key.length){
        list_edges[j +1] = list_edges[j];
        j = j -1;
      }

      list_edges[j+1] = key; 
    }
    return list_edges;
  }
}

// Graph class 
class Graph {
  private List<string> names_of_nodes;
  private List<Edge> list_edges; 

  // constructor 
  public Graph(List<string> node_names, List<Edge> edge_list){
    names_of_nodes = node_names; 
    list_edges = edge_list; 
  }

  // Step 3: implement Kruskal's algorithm 
  public int kruskal_alg(){
    //making some variables
    List<Edge> edge_copy = new List<Edge>(); 
    List<DisjointSet> dss = new List<DisjointSet>(); 
    int sum = 0; 

    //copying the field of edge list to a temp (so I don't accidentally alter it ) [IDK how c# works with aliasing local vars to parameters]
    for (int e = 0 ; e< list_edges.Count; e++){
      edge_copy.Add(list_edges[e]);
    }

    // creating a separate disjointed set for each node 
    for (int u = 0 ; u< names_of_nodes.Count; u++){
      List<string> temporary_ls = new List<string>();
      temporary_ls.Add(names_of_nodes[u]);
      DisjointSet temp_ds = new DisjointSet(temporary_ls);
      dss.Add(temp_ds);
    }

    //while loop to pick shortest edges
    while (dss.Count > 1 ){
      Edge new_edge = edge_copy[0];
      edge_copy.RemoveAt(0);
      DisjointSet ds_w_snode = null;
      DisjointSet ds_w_enode = null;
      for (int q = 0 ; q<dss.Count ; q ++){
        if (dss[q].set_find(new_edge.starting_node)){
          ds_w_snode = dss[q];
          break;
        }
      }
      for (int w = 0 ; w<dss.Count ; w ++){
        if (dss[w].set_find(new_edge.ending_node)){
          ds_w_enode = dss[w];
          break;
        }
      }
      if (ds_w_snode == null || ds_w_enode == null){
        throw new InvalidOperationException("Couldn't find sets with those nodes");
      }
      if (DisjointSet.is_same_set(ds_w_snode,ds_w_enode)){
        continue; 
      }
      else{
        DisjointSet adding_ds = null; 
        adding_ds = DisjointSet.Union(ds_w_enode,ds_w_snode);
        dss.Remove(ds_w_enode);
        dss.Remove(ds_w_snode);
        dss.Add(adding_ds);
        sum += new_edge.length;
      }
    }
    return sum; 
  }
}



class MainClass {

  public static void Main (string[] args) {
    /*  This is the graph: 
         B
  2 -> / | \ <- 3
      A  |<-4 D
  5 -> \ |  / <- 1
         C
    Shortest path should be 6
    */
    Edge ed1 = new Edge("A",2,"B");
    Edge ed2 = new Edge("B",3,"D");
    Edge ed3 = new Edge("D",1,"C");
    Edge ed4 = new Edge("B",4,"C");
    Edge ed5 = new Edge("A",5,"C");

    List<Edge> edge_l = new List<Edge>();

    edge_l.Add(ed1);
    edge_l.Add(ed2);
    edge_l.Add(ed3);
    edge_l.Add(ed4);
    edge_l.Add(ed5);

    edge_l = Edge.sort_edges(edge_l);
    Edge.PrintListEdge(edge_l);

    List<string> node_name = new List<string>();
    node_name.Add("A");
    node_name.Add("B");
    node_name.Add("C");
    node_name.Add("D");

    Graph g = new Graph(node_name,edge_l);
    Console.WriteLine(g.kruskal_alg());

    /* Testing steps:
    1) Test edge class (here's what's left:)
      - test edge sort +
    2) Test disjoint set (here's what's left:)
      - test i ~
    3) Test kruskal's algorithm 
      - traverse with simple 
      - actually test 
    */

    
    /*//TESTING EDGE CLASS --------------------------
    Edge e1 = new Edge("A",4,"B");
    Edge e2 = new Edge("A",2,"D");
    Edge e3 = new Edge("D",3,"E");
    Edge e4 = new Edge("E",1,"A");
    Edge e5 = new Edge("E",5,"B");
    Edge e6 = new Edge("E",9,"F");
    Edge e7 = new Edge("B",6,"F");
    Edge e8 = new Edge("B",8,"C");
    Edge e9 = new Edge("C",1,"F");
    
    List<Edge> edge_list = new List<Edge>();

    edge_list.Add(e1);
    edge_list.Add(e2);
    edge_list.Add(e3);
    edge_list.Add(e4);
    edge_list.Add(e5);
    edge_list.Add(e6);
    edge_list.Add(e7);
    edge_list.Add(e8);
    edge_list.Add(e9);

    edge_list = Edge.sort_edges(edge_list);

    List<string> names = new List<string>(); 
    names.Add("A");
    names.Add("B");
    names.Add("C");
    names.Add("D");
    names.Add("E");
    names.Add("F");*/

    /*//Testing the edge sort 
    Edge e1 = new Edge("A",4,"B");
    Edge e2 = new Edge("A",2,"D");
    Edge e3 = new Edge("D",3,"E");
    Edge e4 = new Edge("E",1,"A");

    List<Edge> edge_list = new List<Edge>();

    edge_list.Add(e1);
    edge_list.Add(e2);
    edge_list.Add(e3);
    edge_list.Add(e4);

    edge_list = Edge.sort_edges(edge_list);
    Edge.PrintListEdge(edge_list);*/

    
    /*//TESTING DISJOINT SET ----------------------
    List<string> ls3 = new List<string>();
    ls3.Add("C");
    List<string> ls4 = new List<string>();
    ls4.Add("C");
    DisjointSet ds3 = new DisjointSet(ls3);
    DisjointSet ds4 = new DisjointSet(ls4); 
    Console.WriteLine(DisjointSet.is_same_set(ds3,ds4));*/
  }
}
