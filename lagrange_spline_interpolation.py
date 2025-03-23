import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange, CubicSpline

# --- Function to be approximated ---
def f1(x):
    return np.sin(x)

# --- Lagrange Interpolation ---
def lagrange_interp(x_nodes, y_nodes, x_eval):
    poly = lagrange(x_nodes, y_nodes)
    return poly(x_eval)

# --- Cubic Spline Interpolation ---
def cubic_spline_interp(x_nodes, y_nodes, x_eval):
    cs = CubicSpline(x_nodes, y_nodes)
    return cs(x_eval)

# --- Chebyshev Nodes Calculation ---
def chebyshev_nodes(n, a=-1, b=1):
    k = np.arange(1, n + 1)
    return 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * k - 1) * np.pi / (2 * n))

# --- Plotting Function ---
def plot_it(x_nodes, y_nodes, x_eval, y_lagrange, y_spline, true_func=None):
    plt.figure(figsize=(10, 6))
    plt.plot(x_nodes, y_nodes, 'ro', label='Data')
    plt.plot(x_eval, y_lagrange, 'b-', label='Lagrange')
    plt.plot(x_eval, y_spline, 'g-', label='Spline')
    
    if true_func:
        y_true = true_func(x_eval)
        plt.plot(x_eval, y_true, 'k--', label='True')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Main Execution Function ---
def main():
    # Example 1: sin(x)
    print("Example 1: sin(x)")
    x_n = np.linspace(0, 2 * np.pi, 5)
    y_n = f1(x_n)
    x_e = np.linspace(0, 2 * np.pi, 100)
    
    y_lag = lagrange_interp(x_n, y_n, x_e)
    y_spl = cubic_spline_interp(x_n, y_n, x_e)
    plot_it(x_n, y_n, x_e, y_lag, y_spl, true_func=f1)

    # Example 2: Arbitrary Data Points
    print("\nExample 2: Data points")
    x_data = np.array([0, 1, 2, 3, 4, 5])
    y_data = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])
    x_eval2 = np.linspace(0, 5, 100)
    
    y_lagrange2 = lagrange_interp(x_data, y_data, x_eval2)
    y_spline2 = cubic_spline_interp(x_data, y_data, x_eval2)
    plot_it(x_data, y_data, x_eval2, y_lagrange2, y_spline2)

    # Example 3: Runge's Phenomenon
    print("\nExample 3: Runge's Phenomenon")
    def runge(x):
        return 1 / (1 + 25 * x**2)
    
    n_nodes = 15
    x_nodes_runge = np.linspace(-1, 1, n_nodes)
    y_runge = runge(x_nodes_runge)
    x_eval_runge = np.linspace(-1, 1, 200)
    
    y_lr = lagrange_interp(x_nodes_runge, y_runge, x_eval_runge)
    y_sr = cubic_spline_interp(x_nodes_runge, y_runge, x_eval_runge)
    plot_it(x_nodes_runge, y_runge, x_eval_runge, y_lr, y_sr, true_func=runge)

    # Example 4: Chebyshev Nodes
    print("\nExample 4: Chebyshev Nodes")
    n_cheb = 15
    x_cheb = np.sort(chebyshev_nodes(n_cheb))  # Ensure strictly increasing order
    y_cheb = runge(x_cheb)
    xe_cheb = np.linspace(-1, 1, 200)
    
    y_lag_cheb = lagrange_interp(x_cheb, y_cheb, xe_cheb)
    y_spl_cheb = cubic_spline_interp(x_cheb, y_cheb, xe_cheb)
    plot_it(x_cheb, y_cheb, xe_cheb, y_lag_cheb, y_spl_cheb, true_func=runge)

if __name__ == "__main__":
    main()
