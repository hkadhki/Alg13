def runge_kutta_4(f, x0, y0, x_end, h):
    x = x0
    y = y0
    n_steps = int((x_end - x0) / h)
    for _ in range(n_steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return y


def f(x, y):
    return 2 * x

x0 = 0
y0 = 1
x_end = 1
h = 0.1

y_result = runge_kutta_4(f, x0, y0, x_end, h)

print(f"Решение в точке x = {x_end}: y = {y_result:.4f}")