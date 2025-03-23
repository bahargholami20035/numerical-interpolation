# Python Interpolation Examples

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains Python code demonstrating Lagrange and cubic spline interpolation methods. It includes examples of:

*   Interpolating a simple function (sin(x)).
*   Interpolating arbitrary data points.
*   Illustrating Runge's phenomenon with high-degree polynomial interpolation.
*   Mitigating Runge's phenomenon using Chebyshev nodes.

## Table of Contents
* [Getting Started](#getting-started)
  *  [Prerequisites](#prerequisites)
  *  [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
  *  [Example 1: Sine Function](#example-1-sine-function)
  *  [Example 2: Data Points](#example-2-data-points)
  *  [Example 3: Runge's Phenomenon](#example-3-runges-phenomenon)
  *  [Example 4: Chebyshev Nodes](#example-4-chebyshev-nodes)
* [Contributing](#contributing)
* [License](#license)

## Getting Started

### Prerequisites

To run this code, you will need the following Python libraries:

*   NumPy
*   SciPy
*   Matplotlib

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```
    (Replace `YOUR_GITHUB_USERNAME` and `YOUR_REPOSITORY_NAME` with your actual GitHub username and the repository name you chose.)

2.  **Install the required libraries:**

    ```bash
    pip install numpy scipy matplotlib
    ```

## Usage

To run the interpolation examples, simply execute the Python script:

```bash
python interpolation_demo.py
