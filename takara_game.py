import tkinter as tk
from tkinter import messagebox, ttk
import random

class TreasureHuntGUI:
    def __init__(self):
        self.TAKARA_NUM = 8  # 宝の数
        self.SIZE = 10       # フィールドの1辺のサイズ
        self.field = []      # ゲームフィールド
        self.buttons = []    # ボタンの配列
        self.phase = 1       # 現在のフェーズ
        self.treasures_found = 0  # 見つけた宝の数
        self.game_over = False
        
        # フィールドの状態
        self.UNKNOWN = -1    # 未調査
        self.TREASURE = -2   # 宝（隠れている）
        self.FOUND = -3      # 見つけた宝
        
        # GUIの初期化
        self.setup_gui()
        self.init_game()
        
    def setup_gui(self):
        """GUIを設定"""
        self.root = tk.Tk()
        self.root.title("🏴‍☠️ 宝探しゲーム 💰")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(False, False)
        
        # ウィンドウを中央に配置
        self.center_window()
        
        # スタイルの設定
        self.setup_styles()
        
        # メインフレーム
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(padx=20, pady=20)
        
        # タイトル
        title_label = tk.Label(main_frame, 
                              text="🏴‍☠️ 宝探しゲーム 💰",
                              font=('Arial', 24, 'bold'),
                              fg='#f39c12',
                              bg='#2c3e50')
        title_label.pack(pady=(0, 10))
        
        # 説明文
        info_text = """10×10のフィールドに8個の宝が隠されています
マスをクリックして宝を探しましょう！
数字は周囲8マスにある宝の数を示します"""
        
        info_label = tk.Label(main_frame,
                             text=info_text,
                             font=('Arial', 12),
                             fg='#ecf0f1',
                             bg='#2c3e50',
                             justify='center')
        info_label.pack(pady=(0, 15))
        
        # ゲーム情報フレーム
        info_frame = tk.Frame(main_frame, bg='#2c3e50')
        info_frame.pack(pady=(0, 15))
        
        # フェーズ表示
        self.phase_label = tk.Label(info_frame,
                                   text=f"フェーズ: {self.phase}",
                                   font=('Arial', 14, 'bold'),
                                   fg='#3498db',
                                   bg='#2c3e50')
        self.phase_label.pack(side='left', padx=(0, 30))
        
        # 残り宝表示
        self.treasures_label = tk.Label(info_frame,
                                       text=f"残り宝: {self.TAKARA_NUM}",
                                       font=('Arial', 14, 'bold'),
                                       fg='#e74c3c',
                                       bg='#2c3e50')
        self.treasures_label.pack(side='left')
        
        # ゲームボードフレーム
        board_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=3)
        board_frame.pack(pady=10)
        
        # 列ラベル
        label_frame = tk.Frame(board_frame, bg='#34495e')
        label_frame.grid(row=0, column=0, columnspan=11, pady=5)
        
        tk.Label(label_frame, text="", width=3, bg='#34495e').grid(row=0, column=0)
        for i in range(self.SIZE):
            tk.Label(label_frame,
                    text=chr(ord('a') + i),
                    font=('Arial', 12, 'bold'),
                    fg='#f39c12',
                    bg='#34495e',
                    width=3).grid(row=0, column=i+1)
        
        # ゲームボード
        self.buttons = []
        for y in range(self.SIZE):
            row = []
            # 行ラベル
            tk.Label(board_frame,
                    text=str(y),
                    font=('Arial', 12, 'bold'),
                    fg='#f39c12',
                    bg='#34495e',
                    width=3).grid(row=y+1, column=0)
            
            for x in range(self.SIZE):
                btn = tk.Button(board_frame,
                               text="+",
                               font=('Arial', 12, 'bold'),
                               width=3,
                               height=1,
                               command=lambda r=y, c=x: self.on_cell_click(c, r),
                               bg='#7f8c8d',
                               fg='white',
                               relief='raised',
                               bd=2)
                btn.grid(row=y+1, column=x+1, padx=1, pady=1)
                row.append(btn)
            self.buttons.append(row)
        
        # ボタンフレーム
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(pady=15)
        
        # リセットボタン
        reset_btn = tk.Button(button_frame,
                             text="🔄 ゲームリセット",
                             font=('Arial', 12, 'bold'),
                             command=self.reset_game,
                             bg='#e67e22',
                             fg='white',
                             relief='raised',
                             bd=3,
                             padx=20,
                             pady=5)
        reset_btn.pack(side='left', padx=(0, 10))
        
        # ヘルプボタン
        help_btn = tk.Button(button_frame,
                            text="❓ ヘルプ",
                            font=('Arial', 12, 'bold'),
                            command=self.show_help,
                            bg='#9b59b6',
                            fg='white',
                            relief='raised',
                            bd=3,
                            padx=20,
                            pady=5)
        help_btn.pack(side='left', padx=(0, 10))
        
        # 終了ボタン
        quit_btn = tk.Button(button_frame,
                            text="❌ 終了",
                            font=('Arial', 12, 'bold'),
                            command=self.root.quit,
                            bg='#c0392b',
                            fg='white',
                            relief='raised',
                            bd=3,
                            padx=20,
                            pady=5)
        quit_btn.pack(side='left')
        
        # メッセージ表示用ラベル
        self.message_label = tk.Label(main_frame,
                                     text="ゲーム開始！マスをクリックして宝を探そう！",
                                     font=('Arial', 12, 'bold'),
                                     fg='#2ecc71',
                                     bg='#2c3e50',
                                     wraplength=400)
        self.message_label.pack(pady=10)
    
    def setup_styles(self):
        """ボタンスタイルを設定"""
        self.colors = {
            'unknown': '#7f8c8d',      # 未調査
            'revealed': '#ecf0f1',     # 調査済み
            'treasure': '#f1c40f',     # 宝
            'danger': '#e74c3c'        # 危険（多くの宝がある）
        }
    
    def center_window(self):
        """ウィンドウを画面中央に配置"""
        self.root.update_idletasks()
        width = 700
        height = 800
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def init_game(self):
        """ゲームを初期化"""
        self.field = [[self.UNKNOWN for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.phase = 1
        self.treasures_found = 0
        self.game_over = False
        
        # 宝をランダムに配置
        self.place_treasures()
        
        # ボタンをリセット
        self.reset_buttons()
        
        # 情報を更新
        self.update_info()
        
        # メッセージを更新
        self.update_message("ゲーム開始！マスをクリックして宝を探そう！", '#2ecc71')
    
    def place_treasures(self):
        """宝をランダムに配置"""
        placed = 0
        while placed < self.TAKARA_NUM:
            x = random.randint(0, self.SIZE - 1)
            y = random.randint(0, self.SIZE - 1)
            
            if self.field[y][x] != self.TREASURE:
                self.field[y][x] = self.TREASURE
                placed += 1
    
    def reset_buttons(self):
        """すべてのボタンをリセット"""
        for y in range(self.SIZE):
            for x in range(self.SIZE):
                btn = self.buttons[y][x]
                btn.config(text="+",
                          bg=self.colors['unknown'],
                          fg='white',
                          state='normal',
                          relief='raised')
    
    def count_treasures(self, x, y):
        """指定した座標の周囲8マスの宝の数をカウント"""
        count = 0
        
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < self.SIZE and 0 <= ny < self.SIZE:
                    if self.field[ny][nx] in [self.TREASURE, self.FOUND]:
                        count += 1
        
        return count
    
    def on_cell_click(self, x, y):
        """セルがクリックされた時の処理"""
        if self.game_over:
            return
        
        current_value = self.field[y][x]
        btn = self.buttons[y][x]
        
        if current_value == self.TREASURE:
            # 宝を発見！
            self.field[y][x] = self.FOUND
            self.treasures_found += 1
            
            treasure_count = self.count_treasures(x, y)
            btn.config(text=f"💎{treasure_count}",
                      bg=self.colors['treasure'],
                      fg='#8b4513',
                      state='disabled',
                      relief='sunken')
            
            self.update_message("🎉 宝を発見！！ ✨", '#f39c12')
            
            if self.treasures_found == self.TAKARA_NUM:
                self.game_over = True
                self.show_all_treasures()
                self.update_message("🏆 全ての宝を見つけました！クリア！！ 🎉", '#2ecc71')
                messagebox.showinfo("ゲームクリア！", 
                                   f"おめでとうございます！\n{self.phase}手でクリアしました！")
                
        elif current_value == self.FOUND:
            self.update_message("⚠️ その宝はすでに見つけています", '#e67e22')
            self.phase -= 1  # フェーズを戻す
            
        elif current_value >= 0:
            self.update_message("⚠️ そこはすでに調べ終わっています", '#e67e22')
            self.phase -= 1  # フェーズを戻す
            
        else:
            # 通常のマスを調査
            treasure_count = self.count_treasures(x, y)
            self.field[y][x] = treasure_count
            
            # ボタンの表示を更新
            if treasure_count == 0:
                btn.config(text="0",
                          bg=self.colors['revealed'],
                          fg='#7f8c8d',
                          state='disabled',
                          relief='sunken')
                self.update_message("💔 この周囲には宝がありません", '#95a5a6')
            else:
                # 宝の数に応じて色を変更
                if treasure_count >= 4:
                    bg_color = self.colors['danger']
                    fg_color = 'white'
                elif treasure_count >= 2:
                    bg_color = '#e67e22'
                    fg_color = 'white'
                else:
                    bg_color = self.colors['revealed']
                    fg_color = '#2c3e50'
                
                btn.config(text=str(treasure_count),
                          bg=bg_color,
                          fg=fg_color,
                          state='disabled',
                          relief='sunken')
                
                self.update_message(f"💡 周囲に {treasure_count} 個の宝があります", '#3498db')
        
        self.phase += 1
        self.update_info()
    
    def show_all_treasures(self):
        """ゲーム終了時に全ての宝を表示"""
        for y in range(self.SIZE):
            for x in range(self.SIZE):
                if self.field[y][x] == self.TREASURE:
                    btn = self.buttons[y][x]
                    treasure_count = self.count_treasures(x, y)
                    btn.config(text=f"💎{treasure_count}",
                              bg='#f39c12',
                              fg='#8b4513',
                              state='disabled')
    
    def update_info(self):
        """ゲーム情報を更新"""
        self.phase_label.config(text=f"フェーズ: {self.phase}")
        self.treasures_label.config(text=f"残り宝: {self.TAKARA_NUM - self.treasures_found}")
    
    def update_message(self, text, color):
        """メッセージを更新"""
        self.message_label.config(text=text, fg=color)
    
    def reset_game(self):
        """ゲームをリセット"""
        if messagebox.askyesno("リセット確認", "ゲームをリセットしますか？"):
            self.init_game()
    
    def show_help(self):
        """ヘルプを表示"""
        help_text = """🏴‍☠️ 宝探しゲーム ヘルプ 💰

【ゲームの目的】
10×10のフィールドに隠された8個の宝をすべて見つけること

【遊び方】
• マスをクリックして調査します
• 数字は周囲8マスにある宝の数を示します
• 💎マークは見つけた宝を表します
• すべての宝を見つけるとクリアです！

【マスの意味】
• + : 未調査のマス
• 数字 : 周囲の宝の数
• 💎数字 : 見つけた宝（数字は周囲の宝の数）

【色の意味】
• グレー : 未調査
• 白 : 調査済み（宝なし）
• オレンジ : 調査済み（宝が近くにある）
• 赤 : 調査済み（宝がたくさん近くにある）
• 金 : 宝を発見！

がんばって全ての宝を見つけよう！"""
        
        messagebox.showinfo("ヘルプ", help_text)
    
    def run(self):
        """ゲームを実行"""
        self.root.mainloop()

def main():
    """メイン関数"""
    game = TreasureHuntGUI()
    game.run()

if __name__ == "__main__":
    main()