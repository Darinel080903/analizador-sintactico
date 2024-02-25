import tkinter as tk

import sintaxis
from lexer import lexer
import re

from sintaxis import parser


class IDESimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple IDE Simulator")
        self.text_widget = tk.Text(root, height=15, width=50)
        self.text_widget.pack()
        self.validate_button = tk.Button(root, text="Validate", command=self.validate_code)
        self.validate_button.pack()
        self.result_text = tk.Text(root, height=15, width=50)
        self.result_text.pack()

    def validate_code(self):
        self.result_text.delete("1.0", tk.END)
        code = self.text_widget.get("1.0", tk.END)
        code = code.replace("\n", "")
        tokens_info = self.analyze_code(code)
        parser.parse(code)
        if sintaxis.error_message is not None:
            parser_result = sintaxis.error_message
            self.result_text.insert(tk.END, f"Parser result: {parser_result}\n")
            sintaxis.error_message = None
        else:
            parser_result = "No se encontraron errores de sintaxis."
            self.result_text.insert(tk.END, f"Parser result: {parser_result}\n")
            self.result_text.insert(tk.END, "Lexer result:\n")
            for token_info in tokens_info:
                self.result_text.insert(tk.END, f"{token_info}\n")


    def analyze_code(self, code):
        lexer.input(code)
        tokens_info = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_info.append(f"Token: {tok.type}, Value: {tok.value}")
        return tokens_info

if __name__ == "__main__":
    root = tk.Tk()
    ide = IDESimulator(root)
    root.mainloop()
