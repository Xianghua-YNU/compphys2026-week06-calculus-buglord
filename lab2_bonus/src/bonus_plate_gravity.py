import numpy as np

G = 6.674e-11

def gauss_legendre_1d(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def gauss_legendre_2d(n):
    x1d, w1d = gauss_legendre_1d(n)
    x2d = np.meshgrid(x1d, x1d)
    w2d = np.outer(w1d, w1d)
    return x2d, w2d

def plate_force_z(z, L=10.0, M_plate=1e4, m_particle=1.0, n=8):
    sigma = M_plate / (L ** 2)
    x_nodes, w_nodes = gauss_legendre_2d(n)
    a = -L / 2
    b = L / 2
    dx = (b - a) / 2
    x = a + dx * (x_nodes[0] + 1)
    y = a + dx * (x_nodes[1] + 1)
    r_sq = x ** 2 + y ** 2 + z ** 2
    integrand = z / (r_sq ** (3/2))
    integral = dx ** 2 * np.sum(w_nodes * integrand)
    Fz = G * sigma * m_particle * integral
    return Fz

if __name__ == "__main__":
    z_vals = np.linspace(0.2, 10, 50)
    Fz_vals = np.array([plate_force_z(z) for z in z_vals])
    print("z (m) | Fz (N)")
    print("-" * 15)
    for z, Fz in zip(z_vals[::5], Fz_vals[::5]):
        print(f"{z:5.2f}  | {Fz:.6e}")
