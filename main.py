"""電圧降下計算アプリケーションのメインモジュール。

Tkinterを使用してGUIを提供し、ユーザーの入力に基づいた計算を行います。
"""

import tkinter as tk
from tkinter import messagebox, ttk


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
        self._setup_output_area()
        self._setup_action_and_graph_area()

    def _setup_input_rows(self) -> None:
        """入力項目(ラジオボタンおよび電圧・電流等のエントリ)のセットアップ"""
        # 電源種別(プルダウン)
        self.power_specs = tk.StringVar(value="三相 AC")

        # ラベル部分を column 0 (右寄せ) に配置
        f_lbl_power = tk.Frame(self.main_frame)
        f_lbl_power.grid(row=0, column=0, padx=5, pady=2, sticky=tk.E)
        tk.Label(f_lbl_power, text="電源種別:").pack(side=tk.LEFT)

        # コンボボックス部分を column 1 (左寄せ) に配置
        f_ent_power = tk.Frame(self.main_frame)
        f_ent_power.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W)
        self.power_combo = ttk.Combobox(
            f_ent_power,
            textvariable=self.power_specs,
            values=["三相 AC", "単相 AC", "直流"],
            state="readonly",
            width=17,
        )
        self.power_combo.pack(side=tk.LEFT)

        # 値が変更されたときに _on_power_spec_change を呼び出す
        self.power_specs.trace_add("write", self._on_power_spec_change)

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

            if attr_name == "voltage_entry":
                # 電圧入力用のエントリを作成(初期値は440)
                widget = tk.Entry(f_ent, justify=tk.RIGHT)
                widget.insert(0, "440")
            elif attr_name == "wire_area_entry":
                # 電線断面積選択用のプルダウン(Combobox)を作成
                widget = ttk.Combobox(
                    f_ent,
                    values=[
                        "1.5",
                        "2.5",
                        "4",
                        "6",
                        "10",
                        "16",
                        "25",
                        "35",
                        "50",
                        "70",
                        "95",
                        "120",
                        "150",
                        "185",
                    ],
                    width=17,
                )
                widget.set("2.5")
            else:
                widget = tk.Entry(f_ent, justify=tk.RIGHT)

            widget.pack(side=tk.LEFT)
            # インスタンス変数として動的に登録
            # (self.voltage_entry などでアクセス可能にする)
            setattr(self, attr_name, widget)

    def _setup_output_area(self) -> None:
        """計算結果表示用のエリアをセットアップ"""
        # 計算結果表示用フレーム
        self.result_frame = tk.LabelFrame(
            self.main_frame,
            text="計算結果",
            padx=10,
            pady=10,
        )
        self.result_frame.grid(
            row=8,
            column=0,
            padx=5,
            pady=10,
            columnspan=2,
            sticky=tk.EW,
        )

        # 結果表示用ラベル
        self.voltage_drop_label = tk.Label(self.result_frame, text="電圧降下(V): -")
        self.voltage_drop_rate_label = tk.Label(
            self.result_frame,
            text="電圧降下率(%): -",
        )
        self.voltage_drop_label.pack(anchor=tk.W)
        self.voltage_drop_rate_label.pack(anchor=tk.W)

        # 電線自動選定表示用フレーム
        self.auto_select_frame = tk.LabelFrame(
            self.main_frame,
            text="電線自動選定",
            padx=10,
            pady=10,
        )
        self.auto_select_frame.grid(
            row=9,
            column=0,
            padx=5,
            pady=10,
            columnspan=2,
            sticky=tk.EW,
        )
        self.auto_select_label = tk.Label(
            self.auto_select_frame,
            text="電線断面積(mm2): -",
        )
        self.auto_select_label.pack(anchor=tk.W)

    def _setup_action_and_graph_area(self) -> None:
        """ボタンとグラフ描画エリアのセットアップ"""
        # 計算ボタン
        sf_btn = tk.Frame(self.main_frame)
        sf_btn.grid(row=7, column=0, padx=5, pady=10, columnspan=2)
        tk.Button(sf_btn, text="計算開始", command=self.on_button_click).pack()

        # グラフ表示用フレーム
        # 入力項目の右側(column=2)に配置することでレイアウトを整理
        self.fig_frame = tk.Frame(self.main_frame, borderwidth=1, relief=tk.SUNKEN)
        self.fig_frame.grid(
            row=0,
            column=2,
            padx=10,
            pady=5,
            rowspan=10,
            sticky=tk.NSEW,
        )
        tk.Label(self.fig_frame, text="[ここにグラフを表示]").pack(expand=True)

    def _on_power_spec_change(self, *args) -> None:
        """電源種別が変更された際に、適切な初期電圧を自動設定する"""
        if not hasattr(self, "voltage_entry"):
            return

        selection = self.power_specs.get()
        self.voltage_entry.delete(0, tk.END)  # 現在の入力をクリア
        if selection == "直流":
            self.voltage_entry.insert(0, "24")
        elif selection == "単相 AC":
            self.voltage_entry.insert(0, "220")
        else:
            self.voltage_entry.insert(0, "440")

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
