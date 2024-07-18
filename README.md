# GraphMatrix: Adjacency Matrix Representation for Graphs
This program, GraphMatrix, allows you to create a representation of a graph using an adjacency matrix. Here's what you can do with it:

## Functionality:

  -  Enter the number of vertices in your graph (between 2 and 5).
  -  Provide edge triplets for each connection in the graph. These triplets specify the origin vertex, destination vertex, and weight of the connection (all integers).
  -  The program validates the input to ensure vertex indices are within the valid range.
  -  It builds an adjacency matrix based on the provided edge information.
  -  Finally, it prints the resulting adjacency matrix.

## Optional (Undirected Graphs):

  -  The code includes a commented-out line to handle undirected graphs. If your graph has connections that go in both directions (i.e., vertex A to B and B to A have the same weight), uncomment the line matrix[j][i] = w within the loop that reads edge triplets.
