<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-C-A8B9CC.svg?logo=c&style=for-the-badge">
</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [ディレクトリ構成](#ディレクトリ構成)
4. [開発環境構築](#開発環境構築)
5. [トラブルシューティング](#トラブルシューティング)

<!-- READMEの作成方法のドキュメントのリンク -->

<!-- Dockerfileのドキュメントのリンク -->

<br />
<!-- プロジェクト名を記載 -->

## 宝探しゲーム（Treasure Hunt Game）

<img src="https://img.shields.io/badge/-C-A8B9CC.svg?logo=c&style=for-the-badge">を用いた宝探しゲームです。

<!-- プロジェクトについて -->

## プロジェクトについて

10×10のグリッド上に隠された8個の宝物を探す、シンプルなコンソールゲームです。プレイヤーは座標（例：c3、f7など）を入力して、宝物の場所を推測します。正しい座標を入力すると「GET!!」と表示され、すべての宝物を見つけるとゲームが終了します。

このプログラムはC言語の基本的な機能（配列、関数、条件分岐、ループなど）を使用しており、プログラミング初心者向けの学習教材としても最適です。

特徴：
- 10×10のグリッドによるシンプルな宝探しゲーム
- 8個の宝物がランダムに配置される
- 座標入力による直感的な操作
- ゲームの進行状況をリアルタイムに表示

<!-- プロジェクトの概要を記載 -->

<p align="left">
  <br />
  <br />
  <br />

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・ツール | バージョン |
| ------------ | ---------- |
| C言語        | C99/C11    |
| GCC          | 9.0以上    |
| MinGW        | 8.0以上（Windows用）|

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

<!-- Treeコマンドを使ってディレクトリ構成を記載 -->

```
--takara_game.c
--README.md
```

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

<!-- コンテナの作成方法、パッケージのインストール方法など、開発環境構築に必要な情報を記載 -->

### 必要条件
- C言語コンパイラ（GCC、MinGW、Clang、Visual Studioのコンパイラなど）

### Windows での環境構築と実行方法

1. **MinGWのインストール**
   - [MinGW](https://sourceforge.net/projects/mingw/)をダウンロードしてインストール
   - インストール時に「gcc」と「g++」コンパイラを選択
   - システム環境変数のPATHにMinGWのbinディレクトリを追加

2. **コンパイルと実行**
   - コマンドプロンプトを開く（Windowsキー+Rを押して「cmd」と入力）
   - プロジェクトディレクトリに移動:
     ```
     cd プロジェクトのパス
     ```
   - コンパイル:
     ```
     gcc takara_game.c -o takara_game
     ```
   - 実行:
     ```
     takara_game
     ```

### Mac/Linux での環境構築と実行方法

1. **GCCのインストール**
   - Mac: 
     ```
     xcode-select --install
     ```
   - Ubuntu/Debian:
     ```
     sudo apt update
     sudo apt install build-essential
     ```
   - Fedora/RHEL/CentOS:
     ```
     sudo dnf install gcc
     ```

2. **コンパイルと実行**
   - ターミナルを開く
   - プロジェクトディレクトリに移動:
     ```
     cd プロジェクトのパス
     ```
   - コンパイル:
     ```
     gcc takara_game.c -o takara_game
     ```
   - 実行:
     ```
     ./takara_game
     ```

### オンラインコンパイラを使用する方法

コンパイラをインストールしたくない場合は、以下のオンラインコンパイラを使用できます:

1. [Replit](https://replit.com/) - 無料でアカウントを作成し、C言語プロジェクトを開始
2. [OnlineGDB](https://www.onlinegdb.com/) - コードを直接ペーストして実行
3. [Programiz](https://www.programiz.com/c-programming/online-compiler/) - シンプルなオンラインCコンパイラ

## ゲームの遊び方

1. プログラムを実行すると、10×10のグリッドが表示されます
2. 「Input : 」というプロンプトが表示されたら、座標を入力します
   - 座標は「列(a-j)」+「行(0-9)」の形式で入力します（例：c3, f7など）
3. 宝物を見つけると「GET!!」と表示され、残りの宝物の数が減ります
4. すべての宝物（8個）を見つけるとゲームが終了します

## トラブルシューティング

### 一般的な問題と解決策

1. **コンパイルエラー: `stdio.h`が見つからない**
   - 開発環境に適切なCコンパイラがインストールされていることを確認してください

2. **プログラムが即座に終了する**
   - コマンドプロンプトやターミナルから直接実行していることを確認してください
   - IDEを使用している場合は、プログラム終了時に一時停止するオプションを確認してください

3. **ランダム性がない（宝物が毎回同じ場所に現れる）**
   - `srand((unsigned int)t);`の行が正しく動作していることを確認してください

4. **入力が正しく処理されない**
   - 座標は「列(a-j)」+「行(0-9)」の形式で入力してください（例：c3, f7など）
   - 大文字や余分なスペースを入れないようにしてください

<p align="right">(<a href="#top">トップへ</a>)</p>

## 問い合わせ先

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝<br>
株式会社アニメツーリズム<br>
取締役CTO　担当：川上<br>
sota@jam-info.com<br>

株式会社アニメツーリズム・JapanAnimeMaps運営<br>
お問い合わせ<br>
contact@animetourism.co.jp<br>

公式サイト<br>
https://animetourism.co.jp<br>

お問い合わせフォーム<br>
https://animetourism.co.jp/contact.html<br>

アプリはこちら<br>
https://apps.apple.com/jp/app/japananimemaps/id6608967051<br>

〒150-0043<br>
東京都 渋谷区道玄坂1丁目10番8号渋谷道玄坂東急ビル2F-C<br>
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝<br>
※本文に掲載された記事を許可なく転載することを禁じます。<br>
(c)2024 JapanAnimeMaps.All Rights Reserved.<br>

<p align="right">(<a href="#top">トップへ</a>)</p><div id="top"></div>