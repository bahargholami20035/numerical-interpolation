# Lagrange and Cubic Spline Interpolation

This Jupyter Notebook (`lagrange_spline_interpolation.ipynb`) demonstrates and compares Lagrange and Cubic Spline interpolation methods using Python.  It covers several examples, including mitigating Runge's phenomenon with Chebyshev nodes.

## Functionality

The code performs the following:

1.  **Lagrange Interpolation:** Implements Lagrange interpolation using `scipy.interpolate.lagrange`.
2.  **Cubic Spline Interpolation:** Implements cubic spline interpolation using `scipy.interpolate.CubicSpline`.
3.  **Chebyshev Nodes:** Includes a function to calculate Chebyshev nodes, which are strategically placed to reduce oscillations in polynomial interpolation (especially useful for higher-degree polynomials).
4.  **Visualization:**  Provides a plotting function (`plot_it`) to visualize the original data points, the Lagrange interpolating polynomial, the cubic spline, and (optionally) the true function.
5.  **Examples:**
    *   **Example 1:** Interpolates the sine function (`sin(x)`).
    *   **Example 2:** Interpolates a set of arbitrary data points.
    *   **Example 3:** Demonstrates Runge's phenomenon by interpolating the Runge function (1 / (1 + 25x²)) with equally spaced nodes.  This shows the characteristic oscillations of high-degree Lagrange interpolation near the endpoints.
    *   **Example 4:**  Repeats the Runge function interpolation, but this time using Chebyshev nodes. This significantly reduces the oscillations seen in Example 3, illustrating the benefit of Chebyshev nodes.

## Dependencies

The code requires the following Python libraries:

*   `matplotlib`: For plotting.
*   `numpy`: For numerical operations.
*   `scipy`: For interpolation functions (`lagrange` and `CubicSpline`).

You can install these using pip:

```bash
pip install matplotlib numpy scipy
