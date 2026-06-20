import os
import pdfplumber
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_text_from_pdf(pdf_path):
    """PDF からテキストを抽出する関数"""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)
        load_pdf_list(folder)

def load_pdf_list(folder):
    for widget in pdf_frame.winfo_children():
        widget.destroy()

    pdf_files = [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        messagebox.showinfo("情報", "PDFファイルが見つかりませんでした")
        return

    for pdf in pdf_files:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(pdf_frame, text=pdf, variable=var)
        chk.var = var
        chk.pdf = pdf
        chk.pack(anchor="w")

def merge_selected_pdfs():
    folder = folder_path.get()
    if not folder:
        messagebox.showerror("エラー", "フォルダを選択してください")
        return

    selected_pdfs = []
    for widget in pdf_frame.winfo_children():
        if widget.var.get():
            selected_pdfs.append(widget.pdf)

    if not selected_pdfs:
        messagebox.showerror("エラー", "統合するPDFを選択してください")
        return

    output_name = output_filename.get().strip()
    if not output_name:
        messagebox.showerror("エラー", "統合ファイル名を入力してください")
        return

    if not output_name.endswith(".txt"):
        output_name += ".txt"

    merged_text = ""

    for pdf_file in selected_pdfs:
        pdf_path = os.path.join(folder, pdf_file)
        text = extract_text_from_pdf(pdf_path)

        if not text.strip():
            merged_text += f"\n\n===== {pdf_file}（テキスト抽出不可） =====\n\n"
            continue

        merged_text += "\n" + "=" * 50 + "\n"
        merged_text += f"【 {pdf_file} 】\n"
        merged_text += "=" * 50 + "\n\n"
        merged_text += text

    output_path = os.path.join(folder, output_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(merged_text)

    messagebox.showinfo("完了", f"統合ファイルを保存しました：\n{output_path}")

# GUI構築
root = tk.Tk()
root.title("PDF 選択式テキスト統合ツール")

folder_path = tk.StringVar()
output_filename = tk.StringVar()

tk.Label(root, text="① PDFフォルダを選択").pack()
tk.Button(root, text="フォルダを選択", command=select_folder).pack()

tk.Label(root, text="② PDFを選択（チェック）").pack()
pdf_frame = tk.Frame(root)
pdf_frame.pack()

tk.Label(root, text="③ 統合ファイル名（例：merged.txt）").pack()
tk.Entry(root, textvariable=output_filename, width=40).pack()

tk.Button(root, text="統合する", command=merge_selected_pdfs).pack(pady=10)

root.mainloop()
