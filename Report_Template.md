# 第 6 周实验报告：数值积分与物理场重建

## 1. 小组信息

**小组 ID**：  
**成员名单**：

| 任务 | 负责同学 | Commit Hash | 贡献说明 |
|---|---|---|---|
| Task A |  |  |  |
| Task B |熊家逸20241050206  | Enumerating objects: 9, done.Counting objects: 100% (9/9), done.Delta compression using up to 2 threadsCompressing objects: 100% (5/5), done.Writing objects: 100% (5/5), 1012 bytes 1012.00 KiB/s, done.Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)remote: Resolving deltas: 100% (2/2), completed with 2 local objects.To https://github.com/Xianghua-YNU/compphys2026-week06-calculus-buglord   d1bed09..0b9ef1d  main -> main|完成lab1 partB  |
| Task C |  |  |  |
| Bonus |  |  |  |

---

## 2. Task A：3-α 温度敏感性指数（23分）

- 你实现的 `rate_3alpha(T)` 与 `sensitivity_nu(T0,h)` 核心思路：  
- 使用的温度点与步长：  
- 计算结果表：

| T0 (K) | ν(T0) |
|---:|---:|
| 1.0e8 |  |
| 2.5e8 |  |
| 5.0e8 |  |
| 1.0e9 |  |

- 物理解释：在低温与高温区，ν 的变化说明了什么？

---

## 3. Task B：梯形 vs Simpson + Debye 积分（24分）

- 你实现的两个积分器是否通过偶数分段与边界检查：trapezoid_composite(f, a, b, n):检查 n > 0若 n <= 0 会抛出 ValueErrorsimpson_composite(f, a, b, n):检查 n > 0检查 n 必须为偶数若 n 为奇数会抛出 ValueError所以两个积分器都做了边界检查；Simpson 方法额外强制要求偶数分段。  
- 同一参数下方法比较：

| 方法 | n | 积分值 | 误差估计 | 结论 |
|---|---:|---:|---:|---|
| 梯形法 | 100 |0.20003333300000006 |3.33×10⁻⁵  |  精度一般|
| Simpson 法 | 100 |  0.20000000133333332|  1.33×10⁻⁹|明显更高精度  |

- 对 Debye 积分结果的解释：  debye_integral 结果符合预期且为正值Simpson 法在 Debye 积分上同样比梯形法更准确这说明在相同分段数下，Simpson 法对于这种平滑积分核收敛更快

---

## 4. Task C：带电圆环电势场（23分）

- 你实现的点电势函数与网格电势函数说明：  
- 数值稳定性处理（例如：靠近圆环时的截断策略）：  
- 结果图（至少 1 张）：

![ring-potential](请替换为你的图片路径)

- 物理解释：等势线分布体现了怎样的空间对称性？

---

## 5. Bonus：方板引力场（30分）

- 你实现的二维高斯积分方案：  
- 参数设置（L, M_plate, n）：  
- 结果表：

| z (m) | Fz (N) |
|---:|---:|
| 0.2 |  |
| 1.0 |  |
| 5.0 |  |
| 10.0 |  |

- 你对近场/远场行为的解释：  

---

## 6. AI 代码审查记录（必填）

- 你使用的关键 Prompt：  
- AI 输出中你识别出的错误或不严谨点（至少 2 条）：  
- 你的修正依据（数值分析 or 物理约束）：  
