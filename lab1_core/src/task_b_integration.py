import math


def debye_integrand(x: float) -> float:
    if abs(x) < 1e-12:
        return 0.0
    ex = math.exp(x)
    return (x**4) * ex / ((ex - 1.0) ** 2)


def trapezoid_composite(f, a: float, b: float, n: int) -> float:
    # TODO B1: 实现复合梯形积分
    if n <= 0:
        raise ValueError("n must be a positive integer")
    h = (b - a) / n
    total = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        x = a + i * h
        total += f(x)
    return h * total


def simpson_composite(f, a: float, b: float, n: int) -> float:
    # TODO B2: 实现复合 Simpson 积分，并检查 n 为偶数
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n % 2 != 0:
        raise ValueError("simpson_composite requires an even number of subintervals")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        total += 4.0 * f(x) if i % 2 != 0 else 2.0 * f(x)
    return h * total / 3.0


def debye_integral(T: float, theta_d: float = 428.0, method: str = "simpson", n: int = 200) -> float:
    # TODO B3: 计算 Debye 积分 I(theta_d/T)
    if T <= 0.0:
        raise ValueError("Temperature T must be positive")
    if n <= 0:
        raise ValueError("n must be a positive integer")
    y = theta_d / T
    method_lower = method.strip().lower()
    if method_lower == "trapezoid":
        return trapezoid_composite(debye_integrand, 0.0, y, n)
    if method_lower == "simpson":
        return simpson_composite(debye_integrand, 0.0, y, n)
    raise ValueError("Unknown method. Use 'simpson' or 'trapezoid'.")
