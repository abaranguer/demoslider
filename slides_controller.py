#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from slides_model import Model

class Controller:
    model = None
    frames = None
    slide = 0

    def __init__(self):
        self.model = Model()
	print "AppController constructor"

