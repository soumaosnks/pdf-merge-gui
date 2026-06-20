# 🧠 PDF Merge GUI Tool  
選択した PDF を 1 つのテキストファイルに統合できる GUI アプリ

---

## 📌 概要

**PDF Merge GUI Tool** は、フォルダ内の PDF を GUI 上でチェックボックス選択し、  
選んだ PDF のテキストを 1 つの `.txt` ファイルに統合する Python アプリです。

- 完全ローカルで動作  
- ネット接続不要  
- 画像PDFはスキップ（テキストPDFのみ対応）  
- 区切り線つきで読みやすい統合ファイルを生成  

Python 初心者でも扱いやすく、実務でも使えるツールです。

---

## ✨ 主な機能

### ✔ GUI で PDF を選択  
フォルダ内の PDF が一覧表示され、チェックボックスで選択できます。

### ✔ 統合ファイル名を自由に設定  
`merged.txt` など、任意の名前で保存できます。

### ✔ PDFごとに区切り線を挿入  
統合後のテキストは PDF ごとに見やすく区切られます。

### ✔ テキストPDFのみ対応  
画像PDFは自動でスキップし、処理が止まりません。

### ✔ 完全ローカル動作  
セキュリティ面でも安心。

---

## 🖥️ 使用方法

### 1. リポジトリをクローン

git clone https://github.com/soumaosnks/pdf-merge-gui.git (github.com in Bing)
cd pdf-merge-gui


### 2. 必要ライブラリをインストール

pip install -r requirements.txt


### 3. アプリを起動

python pdf-text-extractor.py


### 4. GUI の操作手順

1. 「フォルダを選択」ボタンで PDF が入ったフォルダを指定  
2. チェックボックスで統合したい PDF を選択  
3. 統合ファイル名を入力（例：`merged.txt`）  
4. 「統合する」ボタンを押す  
5. 結果が同じフォルダに保存されます

---

## 📂 フォルダ構成

pdf-merge-gui/<br>
├ pdf-text-extractor.py<br>
├ requirements.txt<br>
└ sample_pdfs/


---

## 🧩 コード概要

### ● GUI（tkinter）
- フォルダ選択ダイアログ  
- PDF一覧のチェックボックス生成  
- 統合ファイル名の入力欄  
- 実行ボタン  

### ● PDF処理（pdfplumber）
- テキストPDFから文字を抽出  
- 画像PDFは抽出結果が空 → スキップ  

### ● 統合処理
- 選択したPDFを順番に読み込み  
- 区切り線を挿入して1つのテキストにまとめる  

---

## 📘 requirements.txt

pdfplumber
tk


---

## 🧠 技術ポイント

- Python 標準 GUI ライブラリ **tkinter** を使用  
- PDF テキスト抽出に **pdfplumber**  
- ファイル操作に **os**  
- UTF-8 対応で日本語PDFも扱える  
- GUI × PDF × ファイル操作の基礎が詰まった構成  

---

## 💡 応用アイデア

- OCR（画像PDF対応）を追加  
- PDF の順番をドラッグで並び替え  
- 統合後に自動でファイルを開く  
- `.exe` 化して配布可能にする（PyInstaller）  
- ダークモード対応 GUI  

---

## 👤 作者

**岡本颯真（Souma Okamoto）**  
- Python / ABAP / GitHub  
- 業務自動化ツールの開発に挑戦中  
- ERP事業で全体最適を意識して働く新入社員  

---

## 🪪 ライセンス

このプロジェクトは **MIT License** のもとで公開されています。

