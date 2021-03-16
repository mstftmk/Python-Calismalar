#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mustafa
"""

"""
Buradaki kütüphaneleri indirmeniz gerekiyor.
"""

from pytube import Playlist, YouTube
from pyfiglet import Figlet
import time

yazi_format = Figlet(font="slant")

link = input("Link Girin: ")
try:
  video = YouTube(link)
except:
  print("Unavailable link..")
else:
  print("İndiriliyor..", end="")
  for i in range(6):
    time.sleep(.3)
    print(".", end="")
  print("")
  indirme = video.streams.get_highest_resolution()
  indirme.download()
  print(yazi_format.renderText("Completed"))
