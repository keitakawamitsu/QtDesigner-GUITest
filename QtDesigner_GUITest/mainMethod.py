# -*- coding: utf-8 -*-
import cv2
import os

class MainClass():
    def showImg(self):
        img = cv2.imread('TestImg.png',cv2.IMREAD_COLOR)
        cv2.imshow("image", img)
