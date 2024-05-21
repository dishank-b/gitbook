# Geometrical Representation

### **Matrix**



**Matrices are linear transformations on a vector space.**

Matrix is basically set of column vectors. And those column vectors basically denotes the bases of coordinate system.&#x20;

Let $$\bf u, \bf v$$be the two basis vectors of a coordinate system, then for any point $$P$$, the coordinates will be written as number of step in the direction of $$\bf u$$and $$\bf v$$it will take from origin to point $$P$$. So,

$$
P = x\textbf u+y\textbf v
$$

So the cooridnates of point $$P$$will be $$[x,y]$$in the coordinate system whose basis vectors are $$\bf u, \bf v$$

Now let be the matrix containing the bases vector as:

$$
M = [\bf u, \bf v] \\ 
= \begin{bmatrix}
u_1 & v_1\\
u_2 & v_2 
\end{bmatrix}
$$

Now to denote the point P, we show it as matrix multiplication. Essentially $$P = M\bf x$$where $$M$$is the basis matrix and $$x$$is the coordinate vector in the basis $$\bf u, \bf v$$. So

$$
P = M\bf x = [\bf u , \bf v]\begin{bmatrix}
x\\
y
\end{bmatrix} =  x \textbf u+y \textbf v
$$

**Hence**, **when it comes to geometry, matrices are merely a notational device of writing down the base vectors of a coordinate system.**

**Homogeneous coordinates** have an additional coordinate marking the coordinate vector as a point (non-zero) or a directional vector (zero). These extended vectors allow translations to be written as matrices as well.

### **Resources**

{% embed url="https://www.coranac.com/documents/geomatrix#:~:text=When%20it%20comes%20to%20geometry,scalars%20for%20the%20base%20vectors." %}

{% embed url="http://gregorygundersen.com/blog/2018/10/24/matrices" %}

### **Determinant**

Determinant of a matrix basically represents the local, linearized rate of volume change of a transformation.

It's equal to the multiplication of all eigenvalues of the matrix.&#x20;
