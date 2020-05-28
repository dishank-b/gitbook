# Robotics

## State Space Representation

A **state-space representation** is a mathematical model of a physical system as a set of input, output and state variables related by first-order [differential equations](https://en.wikipedia.org/wiki/Differential_equation) or [difference equations](https://en.wikipedia.org/wiki/Difference_equation). State variables are variables whose values evolve through time in a way that depends on the values they have at any given time and also depends on the externally imposed values of input variables.   
Output variables’ values depend on the values of the state variables.

The "[state space](https://en.wikipedia.org/wiki/State_space)" is the [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space) in which the variables on the axes are the state variables. The state of the system can be represented as a vector within that space.

In continuous time domain:

$$
\dot{x(t}) = Ax(t)+Bu(t) \\y(t) = Cx(t) +Du(t)
$$

Discrete time domain:

$$
\dot{x(k+1}) = Ax(k)+Bu(k) \\y(k) = Cx(k) +Du(k)
$$

Time Variant version:

In above equations, $$A,B,C,D$$are constants which shows that system is time invariant wrt the matrices i.e same $$x(t)$$is same for two different $$t_1, t_2$$, then the system is same.   
Where as the matrices can be time dependent if we have $$A(t), B(t), C(t), D(t)$$. I.e the system dynamics may change with time. This is also called **non-stationery system.** 

### Explaining the variables: 

$$x(t)$$is an state variable. An state variable is the smallest possible subset of system variables that can represent the entire state of the system at any given time.   
An system can be anything, such as car moving on road is a system. In this case, this system can be represent by the position of car and it's velocity, as these variables gives the complete information about the system.   
State variables must be linearly independent ie. no variable should be linear combinations of other variables. 

**NOTE:** We can also include the acceleration of the car as the state variable, but rather it's considered the input to the system, as it can be directly controlled externally and not really dependent on anything in the system. 

\*\*\*\*$$u(t )$$is an input variable to the system. For example, acceleration \(pedal/throttle\) is a input.  

$$y(t)$$is the output of the system or some variable of the system which can be measured. Now it's really system dependent that what is your output or what are you measuring. For example in system, position of car is our output and we can measure it, or may be it's velocity is output and we have odometer to measure it. Or may be we can measure both position and velocity, and which case basically we can observer whole state variable or system state.   
Generally, $$y(t)$$can be end result of our process/system which we actually care about. Or it can be something that can be easily measured through some sensor. 

**NOTE:** It generally upon us to consider which variables as part of the input, and what variables to think as the output/measurement. You can interpret variables according to your design of system and how you want to solve your problem. 

### Explaining the equations and what they represent. 

First equation, shows that the rate of change of system at any time depends upon the state of the system and input to the system at that time. This is called the transition equation of the system, and basically shows the dynamic of the system. 

For ex, in our example of car. Let state be car position and velocity then, 

$$x(t) = [p,v]$$and then $$\dot{x(t)} = [\dot{p}, \dot{v}] = [p,a]$$. and out input $$u(t)$$is basically the acceleration. So our first equation will be:

$$
[\dot{p}, \dot{v}] = A*[p,v]+B*a
$$

where 

$$
A=
\begin{bmatrix}
0 & 1 \\
0 & 0 
\end{bmatrix}, 
B=\begin{bmatrix}
0  \\
1
\end{bmatrix}
$$

Hence, we represent our system dynamics using this equation. 

Coming to the 2nd equation, it basically tells the relation between our output/measurement and system state and input. In most of the cases you will found that $$D=0$$i.e our output is function of system state only. Now let's say we are measuring the velocity or it's out output. Then the equation will be

$$
y(t) = [v] = Cx(t)\\
C= \begin{bmatrix}
0 & 1 
\end{bmatrix}
$$

### Properties

* This is used to represent any dynamical system. 
* These equation can be used to denote any linear system. Even if system is non-linear we can first linearize the system around some point and then use it in this form. 
* Given state at any time $$t$$you can predict the next state at time $$t+1$$using the first equation.
* You can choose state and output variables as per your problem formulation. 
* This is used a lot in control systems and Kalman Filter also uses this as it's basis. 

## Kalman Filter

Kalman Filter is mostly used in state tracking and state prediction applications. This filter is mean square error minimizer and along with this is also maximum likelihood estimator. 

### Derivation of Kalman Filter

{% embed url="http://web.mit.edu/kirtley/kirtley/binlustuff/literature/control/Kalman%20filter.pdf" %}

In most applications, the internal state is much larger \(more [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_%28physics_and_chemistry%29)\) than the few "observable" parameters which are measured. However, by combining a series of measurements, the Kalman filter can estimate the entire internal state.

{% embed url="https://stats.stackexchange.com/questions/86075/kalman-filter-equation-derivation" %}

{% embed url="https://en.wikipedia.org/wiki/Kalman\_filter" %}

{% embed url="https://webee.technion.ac.il/people/shimkin/Estimation09/ch4\_KFderiv.pdf" %}

### Practical Examples

{% embed url="https://www.intechopen.com/books/introduction-and-implementations-of-the-kalman-filter/introduction-to-kalman-filter-and-its-applications" %}

### Detailed Formulations of Problem: General Filtering, Extended Kalman Filter

Read these files for better and general understanding. 

1.

{% embed url="https://arxiv.org/pdf/1910.03558.pdf" %}

2.

{% embed url="http://users.isr.ist.utl.pt/~mir/pub/kalman.pdf" %}

{% embed url="https://arxiv.org/abs/1811.11618" %}



