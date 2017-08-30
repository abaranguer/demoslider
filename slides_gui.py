#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import Tkinter as tk

from slides_controller import Controller
from slides.slides_slide_01 import Slide01
from slides.slides_slide_02 import Slide02
from slides.slides_slide_03 import Slide03
from slides.slides_slide_04 import Slide04
from slides.slides_slide_05 import Slide05
from slides.slides_slide_06 import Slide06

class Gui:
    control = None
    root = None
    frames= []
    slide = 0

    def __init__(self):
        self.control = Controller()
        self.initializeWindow()
        self.initializeFrames()
        self.root.after(0, self.showFrames)
        self.root.mainloop()

    def initializeWindow(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.title("SlideShow")
        #maxY = self.root.winfo_screenheight()
        #maxX = self.root.winfo_screenwidth()
        #self.root.geometry("%dx%d+0+0" % (maxX, maxY))        
        #self.root.resizable(False, False)

    def initializeFrames(self):
        self.frames.append(Slide01(self.root, self.control))
        self.frames.append(Slide02(self.root, self.control))
        self.frames.append(Slide03(self.root, self.control))
        self.frames.append(Slide04(self.root, self.control))
        self.frames.append(Slide05(self.root, self.control))
        self.frames.append(Slide06(self.root, self.control))
        self.control.frames = self.frames

    def showFrames(self):
        if self.slide > 5:
            self.reset()

        self.frames[self.slide].show()

        self.slide = self.slide + 1

        # rearm trigger
        self.root.after(3000, self.showFrames)
        
    def reset(self):
        for i in range(0, 6):
            self.frames[i].pack_forget()
        self.frames = []
        self.slide = 0
        self.initializeFrames()
