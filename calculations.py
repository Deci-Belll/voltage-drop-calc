"""電圧降下計算に関連する定数と計算ロジックを管理するモジュール。

電線の規格(断面積)や抵抗値のデータを提供し、
それらに基づいた電圧降下および電圧降下率の計算を行います。
"""

# 電線抵抗(Ω/km)のデータ
SQR = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185]
R20km = [
    12.2,
    7.56,
    4.7,
    3.11,
    1.84,
    1.16,
    0.734,
    0.529,
    0.391,
    0.27,
    0.195,
    0.154,
    0.126,
    0.1,
]
R20m = dict(zip(SQR, R20km, strict=True))


class VoltageDropCalculator:
    """電圧降下の計算を行うためのクラス。

    三相交流や直流・単相交流の計算ロジックを提供し、
    電線の抵抗値データに基づいて電圧降下を算出します。
    """

    def __init__(self) -> None:
        """VoltageDropCalculator クラスを初期化します。"""

    def v_drop_3p(self, current: float, sqr: float, length: float, num: int) -> float:
        """三相交流の電圧降下を計算する関数"""
        vd = R20m[sqr] * 1.3 * 2 * length * (current / num) * (1.732 / 2) / 1000
        return vd

    def v_drop_dc(self, current: float, sqr: float, length: float, num: int) -> float:
        """単相・直流の電圧降下を計算する関数"""
        vd = R20m[sqr] * 1.3 * 2 * length * (current / num) / 1000
        return vd

    def v_drop(
        self,
        r: int,
        current: float,
        sqr: float,
        length: float,
        num: int,
    ) -> float:
        """三相交流か単相・直流かを判断して、適切な電圧降下を計算する関数"""
        if r == 0:
            return self.v_drop_3p(current, sqr, length, num)
        return self.v_drop_dc(current, sqr, length, num)


def plot_sqr(x: list[float], y: list[float], r: int, rate: float):
    """電線の断面積と電圧降下率の関係をグラフ化し、Figureオブジェクトを返します。"""
    import matplotlib as mpl
    from matplotlib.figure import Figure

    # Figureインスタンスを生成する
    fig = Figure(figsize=(5, 4), dpi=100)
    # メモリを内側にする
    mpl.rcParams["xtick.direction"] = "in"
    mpl.rcParams["ytick.direction"] = "in"

    ax1 = fig.add_subplot(111)
    ax1.yaxis.set_ticks_position("both")
    ax1.yaxis.set_ticks_position("both")

    ax1.set_xlabel("Cable sq (mm2)")
    ax1.set_ylabel("Voltage drop (%)")
    if r <= 1:
        ax1.set_ylim(0, 7)
        ax1.set_xlim(0, 120)
    else:
        ax1.set_ylim(0, 15)
        ax1.set_xlim(0, 120)
    ax1.plot(x, y, marker="o")
    ax1.grid()
    ax1.plot([0, 120], [rate, rate], color="red", linestyle="--")

    return fig
