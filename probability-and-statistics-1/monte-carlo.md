# Monte Carlo

**Monte Carlo methods**, or **Monte Carlo experiments**, are a broad class of [computational](https://en.wikipedia.org/wiki/Computation) [algorithms](https://en.wikipedia.org/wiki/Algorithm) that rely on repeated [random sampling](https://en.wikipedia.org/wiki/Random_sampling) to obtain numerical results. The underlying concept is to use [randomness](https://en.wikipedia.org/wiki/Randomness) to solve problems that might be [deterministic](https://en.wikipedia.org/wiki/Deterministic_system) in principle.

Monte Carlo simulation furnishes the decision-maker with a range of possible outcomes and the probabilities they will occur for any choice of action.

Monte Carlo Simulation solves deterministic problems using a probabilistic analog.

### Explanation

Monte Carlo methods vary, but tend to follow a particular pattern:

1. Define a domain of possible inputs
2. Generate inputs randomly from a [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution) over the domain
3. Perform a [deterministic](https://en.wikipedia.org/wiki/Deterministic_algorithm) computation on the inputs
4. Aggregate the results

For example, consider a [quadrant \(circular sector\)](https://en.wikipedia.org/wiki/Circular_sector#Quadrant) inscribed in a [unit square](https://en.wikipedia.org/wiki/Unit_square). Given that the ratio of their areas is π/4, the value of [π](https://en.wikipedia.org/wiki/Pi) can be approximated using a Monte Carlo method:[\[12\]](https://en.wikipedia.org/wiki/Monte_Carlo_method#cite_note-FOOTNOTEKalosWhitlock2008-12)

1. Draw a square, then [inscribe](https://en.wikipedia.org/wiki/Inscribed_figure) a quadrant within it
2. [Uniformly](https://en.wikipedia.org/wiki/Uniform_distribution_%28continuous%29) scatter a given number of points over the square
3. Count the number of points inside the quadrant, i.e. having a distance from the origin of less than 1
4. The ratio of the inside-count and the total-sample-count is an estimate of the ratio of the two areas, π/4. Multiply the result by 4 to estimate π.

![](../.gitbook/assets/image%20%2862%29.png)

In this procedure the domain of inputs is the square that circumscribes the quadrant. We generate random inputs by scattering grains over the square then perform a computation on each input \(test whether it falls within the quadrant\). Aggregating the results yields our final result, the approximation of π.

There are two important points:

1. If the points are not uniformly distributed, then the approximation will be poor.
2. There are a large number of points. The approximation is generally poor if only a few points are randomly placed in the whole square. On average, the approximation improves as more points are placed.

### Definition

**Monte Carlo simulation:** a simulation is a fictitious representation of reality, uses repeated sampling to obtain the statistical properties of some phenomenon \(or behavior\).  
**Monte Carlo method:** technique that can be used to solve a mathematical or statistical problem

Examples:

* Simulation: Drawing **one** pseudo-random uniform variable from the interval \[0,1\] can be used to simulate the tossing of a coin: If the value is less than or equal to 0.50 designate the outcome as heads, but if the value is greater than 0.50 designate the outcome as tails. This is a simulation, but not a Monte Carlo simulation.
* Monte Carlo method: Pouring out a box of coins on a table, and then computing the ratio of coins that land heads versus tails is a Monte Carlo method of determining the behavior of repeated coin tosses, but it is not a simulation.
* Monte Carlo simulation: Drawing **a large number** of pseudo-random uniform variables from the interval \[0,1\] at one time, or once at a large number of different times, and assigning values less than or equal to 0.50 as heads and greater than 0.50 as tails, is a Monte Carlo simulation of the behavior of repeatedly tossing a coin.

