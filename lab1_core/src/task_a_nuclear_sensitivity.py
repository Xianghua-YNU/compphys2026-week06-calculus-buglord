import numpy as np


def rate_3alpha(T: float) -> float:
    T8 = T / 1.0e8
    return 5.09e11 * (T8 ** (-3.0)) * np.exp(-44.027 / T8)


def finite_diff_dq_dT(T0: float, h: float = 1e-8) -> float:
    # TODO A1: 使用前向差分实现 dq/dT
    """
    用前向差分近似计算 dq/dT 在 T0 处的值
    :param T0: 参考温度 (K)
    :param h: 相对步长，默认 1e-8
    :return: dq/dT 的近似值
    """
    delta_T = h * T0
    q0 = rate_3alpha(T0)
    q1 = rate_3alpha(T0 + delta_T)
    return (q1 - q0) / delta_T
    #raise NotImplementedError("TODO A1")


def sensitivity_nu(T0: float, h: float = 1e-8) -> float:
    # TODO A2: 根据 nu = (T/q) * dq/dT 计算温度敏感性指数
    """
    计算温度敏感性指数 v(T0)
    :param T0: 参考温度 (K)
    :param h: 相对步长，默认 1e-8
    :return: v 的值
    """
    q0 = rate_3alpha(T0)
    dq_dT = finite_diff_dq_dT(T0, h)
    return (T0 / q0) * dq_dT
    #raise NotImplementedError("TODO A2")


def nu_table(T_values, h: float = 1e-8):
    # TODO A3: 返回 [(T, nu(T)), ...]
    """
    批量计算多个温度点的敏感性指数
    :param T_values: 温度列表/数组 (K)
    :param h: 相对步长，默认 1e-8
    :return: 列表 [(T0, nu0), (T1, nu1), ...]
    """
    result = []
    for T in T_values:
        nu = sensitivity_nu(T, h)
        result.append((T, nu))
    return result
    #raise NotImplementedError("TODO A3")

if __name__ == "__main__":
    # 要求的必算温度点
    T_list = [1.0e8, 2.5e8, 5.0e8, 1.0e9, 2.5e9, 5.0e9]
    table = nu_table(T_list)
    
    # 按要求格式输出
    print("温度敏感性指数计算结果：")
    for T, nu in table:
        print(f"{T:.3e} K : nu = {nu:.2f}")