import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('maze.png') # read an image from a file using
cv2.circle(img,(5,220), 3, (255,0,0), -1) # add a circle at (5, 220)
cv2.circle(img, (25,5), 3, (0,0,255), -1) # add a circle at (5,5)
plt.figure(figsize=(7,7))
plt.imshow(img) # show the image
plt.show()

class Vertex:
    def __init__(self,x_coord,y_coord):
        self.x=x_coord
        self.y=y_coord
        self.d=float('inf') #current distance from source node
        self.parent_x=None
        self.parent_y=None
        self.processed=False
        self.index_in_queue=None

    def find_shortest_path(img,src,dst):
        pq=[] #min-heap priority queue
        imagerows,imagecols=img.shape[0],img.shape[1]
        matrix = np.full((imagerows, imagecols), None)
        #access matrix elements by matrix[row][col]
        #fill matrix with vertices
        for r in range(imagerows):
            for c in range(imagecols):
                matrix[r][c]=Vertex(c,r)
                matrix[r][c].index_in_queue=len(pq)
                pq.append(matrix[r][c])
        #set source distance value to 0
        matrix[source_y][source_x].d=0
        #maintain min-heap invariant (minimum d Vertex at list index 0)
        pq = bubble_up(pq, matrix[source_y][source_x].index_in_queue)


