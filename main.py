"""電圧降下計算アプリケーションのメインモジュール。

Tkinterを使用してGUIを提供し、ユーザーの入力に基づいた計算を行います。
"""

import tkinter as tk
from tkinter import messagebox


class MainApplication(tk.Tk):
    """アプリケーションのメインウィンドウを表すクラス"""

    def __init__(self) -> None:
        """MainApplication クラスのインスタンスを初期化し、GUI の基本設定を行います。"""
        super().__init__()

        # --- ウィンドウの基本設定 ---
        self.title("電圧降下計算")
        self.geometry("800x600")
        self.minsize(300, 200)

        # --- コンポーネント(ウィジェット)の作成 ---
        self.create_widgets()

    def create_widgets(self) -> None:
        """ウィジェットの作成と配置を行うメソッド"""
        # メインフレーム
        self.main_frame = tk.Frame(self, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self._setup_input_rows()
        self._setup_action_and_graph_area()

    def _setup_input_rows(self) -> None:
        """入力項目(ラジオボタンおよび電圧・電流等のエントリ)のセットアップ"""
        # 電源種別(ラジオボタン)
        self.power_specs = tk.IntVar(value=0)
        sf0 = tk.Frame(self.main_frame)
        sf0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        for i, label in enumerate(["三相 AC", "単相 AC", "直流"]):
            tk.Radiobutton(sf0, text=label, variable=self.power_specs, value=i).pack(
                side=tk.LEFT,
            )

        # 入力項目(ラベルとエントリ)の定義
        fields = [
            ("電圧(V):", "voltage_entry"),
            ("電流(A):", "current_entry"),
            ("電線断面積(mm2):", "wire_area_entry"),
            ("電線長(m):", "wire_length_entry"),
            ("電線本数(本):", "wire_count_entry"),
            ("許容電圧降下率(%):", "voltage_drop_rate_entry"),
        ]

        for i, (label_text, attr_name) in enumerate(fields, start=1):
            # ラベル用フレーム(右寄せ)
            f_lbl = tk.Frame(self.main_frame)
            f_lbl.grid(row=i, column=0, padx=5, pady=2, sticky=tk.E)
            tk.Label(f_lbl, text=label_text).pack(side=tk.LEFT)

            # エントリ用フレーム(左寄せ)
            f_ent = tk.Frame(self.main_frame)
            f_ent.grid(row=i, column=1, padx=5, pady=2, sticky=tk.W)
            entry = tk.Entry(f_ent, justify=tk.RIGHT)
            entry.pack(side=tk.LEFT)
            # インスタンス変数として動的に登録
            # (self.voltage_entry などでアクセス可能にする)
            setattr(self, attr_name, entry)

    def _setup_action_and_graph_area(self) -> None:
        """ボタンとグラフ描画エリアのセットアップ"""
        # 計算ボタン
        sf_btn = tk.Frame(self.main_frame)
        sf_btn.grid(row=7, column=0, padx=5, pady=10, columnspan=2)
        tk.Button(sf_btn, text="計算開始", command=self.on_button_click).pack()

        # グラフ表示用フレーム
        # 入力項目の右側(column=2)に配置することでレイアウトを整理
        self.fig_frame = tk.Frame(self.main_frame, borderwidth=1, relief=tk.SUNKEN)
        self.fig_frame.grid(row=0, column=2, padx=10, pady=5, rowspan=9, sticky=tk.NSEW)
        tk.Label(self.fig_frame, text="[ここにグラフを表示]").pack(expand=True)

    def on_button_click(self) -> None:
        """ボタンが押されたときのイベントハンドラ"""
        try:
            # 例として電圧を取得して表示
            voltage = self.voltage_entry.get()
            messagebox.showinfo("計算開始", f"入力された電圧: {voltage}V")
        except AttributeError:
            messagebox.showerror("エラー", "ウィジェットが正しく初期化されていません。")


# --- アプリケーションの起動 ---
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
