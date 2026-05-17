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

        # サブフレーム
        self.sub_frame_0 = tk.Frame(self.main_frame)
        self.sub_frame_1_1 = tk.Frame(self.main_frame)
        self.sub_frame_1_2 = tk.Frame(self.main_frame)
        self.sub_frame_2_1 = tk.Frame(self.main_frame)
        self.sub_frame_2_2 = tk.Frame(self.main_frame)
        self.sub_frame_3_1 = tk.Frame(self.main_frame)
        self.sub_frame_3_2 = tk.Frame(self.main_frame)
        self.sub_frame_4_1 = tk.Frame(self.main_frame)
        self.sub_frame_4_2 = tk.Frame(self.main_frame)
        self.sub_frame_5_1 = tk.Frame(self.main_frame)
        self.sub_frame_5_2 = tk.Frame(self.main_frame)
        self.sub_frame_6_1 = tk.Frame(self.main_frame)
        self.sub_frame_6_2 = tk.Frame(self.main_frame)
        self.sub_frame_7 = tk.Frame(self.main_frame)
        self.sub_frame_8 = tk.Frame(self.main_frame)
        self.sub_frame_9 = tk.Frame(self.main_frame)
        self.fig_frame = tk.Frame(self.main_frame)

        # サブフレームの配置
        self.sub_frame_0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self.sub_frame_1_1.grid(row=1, column=0, padx=5, pady=5)
        self.sub_frame_1_2.grid(row=1, column=1, padx=5, pady=5)
        self.sub_frame_2_1.grid(row=2, column=0, padx=5, pady=5)
        self.sub_frame_2_2.grid(row=2, column=1, padx=5, pady=5)
        self.sub_frame_3_1.grid(row=3, column=0, padx=5, pady=5)
        self.sub_frame_3_2.grid(row=3, column=1, padx=5, pady=5)
        self.sub_frame_4_1.grid(row=4, column=0, padx=5, pady=5)
        self.sub_frame_4_2.grid(row=4, column=1, padx=5, pady=5)
        self.sub_frame_5_1.grid(row=5, column=0, padx=5, pady=5)
        self.sub_frame_5_2.grid(row=5, column=1, padx=5, pady=5)
        self.sub_frame_6_1.grid(row=6, column=0, padx=5, pady=5)
        self.sub_frame_6_2.grid(row=6, column=1, padx=5, pady=5)
        self.sub_frame_7.grid(row=7, column=0, padx=5, pady=5)
        self.sub_frame_8.grid(row=8, column=0, padx=5, pady=5)
        self.sub_frame_9.grid(row=9, column=0, padx=5, pady=5)
        self.fig_frame.grid(row=0, column=1, padx=5, pady=5, columnspan=9)

        # 各種ウィジェットの作成
        # ラジオボタン

        power_specs = tk.IntVar()
        rad1 = tk.Radiobutton(
            self.sub_frame_0,
            text="三相 AC",
            variable=power_specs,
            value=0,
        )
        rad1.pack(side=tk.LEFT)
        rad2 = tk.Radiobutton(
            self.sub_frame_0,
            text="単相 AC",
            variable=power_specs,
            value=1,
        )
        rad2.pack(side=tk.LEFT)
        rad3 = tk.Radiobutton(
            self.sub_frame_0,
            text="直流",
            variable=power_specs,
            value=2,
        )
        rad3.pack(side=tk.LEFT)

        # ラベルとエントリー

        label1 = tk.Label(self.sub_frame_1_1, text="電圧(V):")
        voltage_entry = tk.Entry(self.sub_frame_1_2)
        label1.pack(side=tk.LEFT)
        voltage_entry.pack(side=tk.LEFT)

        label2 = tk.Label(self.sub_frame_2_1, text="電流(A):")
        current_entry = tk.Entry(self.sub_frame_2_2)
        label2.pack(side=tk.LEFT)
        current_entry.pack(side=tk.LEFT)

        label3 = tk.Label(self.sub_frame_3_1, text="電線断面積(mm2):")
        wire_area_entry = tk.Entry(self.sub_frame_3_2)
        label3.pack(side=tk.LEFT)
        wire_area_entry.pack(side=tk.LEFT)

        label4 = tk.Label(self.sub_frame_4_1, text="電線長(m):")
        wire_length_entry = tk.Entry(self.sub_frame_4_2)
        label4.pack(side=tk.LEFT)
        wire_length_entry.pack(side=tk.LEFT)

        label5 = tk.Label(self.sub_frame_5_1, text="電線本数(本):")
        wire_count_entry = tk.Entry(self.sub_frame_5_2)
        label5.pack(side=tk.LEFT)
        wire_count_entry.pack(side=tk.LEFT)

        label6 = tk.Label(self.sub_frame_6_1, text="許容電圧降下率(%):")
        voltage_drop_rate_entry = tk.Entry(self.sub_frame_6_2)
        label6.pack(side=tk.LEFT)
        voltage_drop_rate_entry.pack(side=tk.LEFT)



    def on_button_click(self) -> None:
        """ボタンが押されたときのイベントハンドラ"""
        input_text = self.entry.get()
        messagebox.showinfo("メッセージ", f"入力されたテキスト:\n{input_text}")


# --- アプリケーションの起動 ---
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
