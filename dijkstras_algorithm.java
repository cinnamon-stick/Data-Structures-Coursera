// Step 0: importing and making helpful classes -----------------------------
import java.util.*; 

// Step 1: implement graph --------------------------------------------------
class AdjacencyMatrix {
  //fields
  private int[][] matrix; 
  private String[] node_names;

  // constructor
  public AdjacencyMatrix(int[][] mat,String[] nodes) {
    if (mat.length != nodes.length) {
      throw new java.lang.Error("Matrix and nodes don't match");
    }
    this.node_names = nodes;
    this.matrix = mat;
  }

  //print out the graph 
  public String toString() {
    String printstatement = "";
    for (int i = 0; i<matrix.length;i++){
      for (int j = 0; j<matrix[i].length;j++){
        Integer mat_element = new Integer(matrix[i][j]);
        printstatement = printstatement + mat_element.toString()+ " ";
      }
      printstatement = printstatement +"\n";
    }
    printstatement = printstatement +"\nNodes are: ";
    for (int e = 0 ; e < node_names.length; e++){ 
      printstatement = printstatement +node_names[e]+" ";
    }
    return printstatement;
  }

  //Dijkstra's algorithm ///////////////////////////////////////////////////
  public int dijkAlg(String starting_node, String ending_node) {
    //making some variables
    int curr_index = -1;
    int ending_index = -1;
    ArrayList<Integer> nodeQueue = new ArrayList<Integer>();

    //finding the index where starting_node lies in our matrix
    for (int j = 0; j < node_names.length; j++){
      if (node_names[j].equals(starting_node)){
        curr_index = j;
      }
    }

    //finding the ending node index
    for (int y = 0; y < node_names.length; y++){
      if (node_names[y].equals(ending_node)){
        ending_index = y;
      }
    }

    //filling in the queue 
    for (int i = 0 ; i < node_names.length; i++){
      if (i!=curr_index){
        nodeQueue.add(i,Integer.MAX_VALUE);
      }
      else {
        nodeQueue.add(curr_index,0);
      }
    }


    //Evalutating values loop 
    while (nodeQueue.size() != 0 ){

      // Are we done? 
      if (curr_index == ending_index){
        return nodeQueue.get(ending_index);
      }

      //check edges and reassign lowest way to get to a node
      for (int u = 0 ; u<matrix[curr_index].length; u++){
        if (matrix[curr_index][u] != 0 ){
          int new_val = nodeQueue.get(curr_index) + matrix[curr_index][u];
          if (new_val < nodeQueue.get(u)){
            nodeQueue.set(u,new_val);
          }
        }
      }

      //effectively deleting the node we just processed
      nodeQueue.set(curr_index,Integer.MAX_VALUE);

      //finding next node to process
      int temp_min = Integer.MAX_VALUE;
      int temp_min_index = -1; 
      for (int p = 0 ; p < nodeQueue.size();p++ ){
        if (nodeQueue.get(p)<temp_min){
          temp_min = nodeQueue.get(p);
          curr_index = p;
        }
      }
    }

    return -1; // this means that the method has failed
  }
}

// Step 3: Testing --------------------------------------------------
class Main {
  public static void main(String[] args) {
    //Test 1 - should produce 7 
    int[][] mat = new int[5][5];
    mat[0][1] = 4;
    mat[0][2] = 2;
    mat[1][3] = 1;
    mat[2][3] = 4;
    mat[3][4] = 2; 
    String[] nodes = new String[5];
    nodes[0] = "A";
    nodes[1] = "B";
    nodes[2] = "C";
    nodes[3] = "D";
    nodes[4] = "E"; 
    AdjacencyMatrix my_graph = new AdjacencyMatrix(mat,nodes);
    System.out.println(my_graph.dijkAlg("A","E"));

    //Test 2 - should produce 2 
    int[][] mat2 = new int[2][2];
    mat2[0][1] = 2;
    String[] nodes2 = new String[2];
    nodes2[0] = "A";
    nodes2[1] = "B"; 
    AdjacencyMatrix my_graph2 = new AdjacencyMatrix(mat2,nodes2);
    System.out.println(my_graph2.dijkAlg("A", "B"));
  }
}
