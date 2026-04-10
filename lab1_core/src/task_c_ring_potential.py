import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def ring_potential_point(x: float, y: float, z: float, a: float = 1.0, q: float = 1.0, n_phi: int = 720) -> float:
    phi = np.linspace(0, 2 * np.pi, n_phi + 1)
    dphi = 2 * np.pi / n_phi
    term1 = (x - a * np.cos(phi)) ** 2
    term2 = (y - a * np.sin(phi)) ** 2
    term3 = z ** 2
    f = 1.0 / np.sqrt(term1 + term2 + term3)
    integral = simpson(f, dx=dphi)
    V = (q / (2 * np.pi)) * integral
    return V

def ring_potential_grid(y_grid, z_grid, x0: float = 0.0, a: float = 1.0, q: float = 1.0, n_phi: int = 720):
    Ny = len(y_grid)
    Nz = len(z_grid)
    V_grid = np.zeros((Nz, Ny))
    phi = np.linspace(0, 2 * np.pi, n_phi + 1)
    dphi = 2 * np.pi / n_phi
    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)
    const = q / (2 * np.pi)
    for i in range(Nz):
        z = z_grid[i]
        for j in range(Ny):
            y = y_grid[j]
            term1 = (x0 - a * cos_phi) ** 2
            term2 = (y - a * sin_phi) ** 2
            term3 = z ** 2
            f = 1.0 / np.sqrt(term1 + term2 + term3)
            integral = simpson(f, dx=dphi)
            V_grid[i, j] = const * integral
    return V_grid

def axis_potential_analytic(z: float, a: float = 1.0, q: float = 1.0) -> float:
    return q / np.sqrt(a * a + z * z)

def compute_electric_field(V_grid, y_grid, z_grid):
    dy = y_grid[1] - y_grid[0]
    dz = z_grid[1] - z_grid[0]
    dV_dy = np.gradient(V_grid, dy, axis=1)
    dV_dz = np.gradient(V_grid, dz, axis=0)
    E_y = -dV_dy
    E_z = -dV_dz
    return E_y, E_z

if __name__ == "__main__":
    y = np.linspace(-2.0, 2.0, 100)
    z = np.linspace(-2.0, 2.0, 100)
    Y, Z = np.meshgrid(y, z)
    V = ring_potential_grid(y, z)
    E_y, E_z = compute_electric_field(V, y, z)

    plt.figure(figsize=(8,6))
    plt.contour(Y, Z, V, 20, cmap='viridis')
    plt.colorbar()
    plt.xlabel('y')
    plt.ylabel('z')
    plt.axis('equal')
    plt.show()

    plt.figure(figsize=(8,6))
    plt.streamplot(Y, Z, E_y, E_z, color='r', density=1.5)
    plt.contour(Y, Z, V, 10, cmap='viridis', alpha=0.7)
    plt.xlabel('y')
    plt.ylabel('z')
    plt.axis('equal')
    plt.show()
