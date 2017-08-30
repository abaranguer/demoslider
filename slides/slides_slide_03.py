#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import Tkinter as tk

class Slide03(tk.Frame):

    control = None
        
    def __init__(self, root, controller):
        tk.Frame.__init__(self, root)
        self.control = controller
        self.config(bg="green")

    def show(self):
        for i in range(0, 6):
            self.control.frames[i].pack_forget()

        self.header = tk.Label(self, \
              text="Slide 3", \
              font="Helvetica 24  bold").pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.body = tk.Label(self, \
              text="This is the body", \
              font="Helvetica 24  bold").pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.footer = tk.Label(self, \
              text="This is the footer", \
              font="Helvetica 24  bold").pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
