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
        self.title("クラスベース Tkinter アプリ")
        self.geometry("400x300")
        self.minsize(300, 200)

        # --- コンポーネント(ウィジェット)の作成 ---
        self.create_widgets()

    def create_widgets(self) -> None:
        """ウィジェットの作成と配置を行うメソッド"""
        # メインフレーム
        self.main_frame = tk.Frame(self, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # ラベル
        self.label = tk.Label(
            self.main_frame,
            text="ようこそ、Tkinter アプリへ!",
            font=("Arial", 14),
        )
        self.label.pack(pady=10)

        # エントリー(入力フォーム)
        self.entry = tk.Entry(self.main_frame, font=("Arial", 12), width=25)
        self.entry.pack(pady=10)
        self.entry.insert(0, "ここに入力してください")

        # ボタン
        self.button = tk.Button(
            self.main_frame,
            text="クリックして実行",
            command=self.on_button_click,
            bg="#007bff",
            fg="white",
            padx=10,
            pady=5,
        )
        self.button.pack(pady=10)

    def on_button_click(self) -> None:
        """ボタンが押されたときのイベントハンドラ"""
        input_text = self.entry.get()
        messagebox.showinfo("メッセージ", f"入力されたテキスト:\n{input_text}")


# --- アプリケーションの起動 ---
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
