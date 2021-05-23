#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from yttools import *
from xbmctools import Item
item=Item()
addDir=item.addDir_tube
endDir=item.endDir

def infolist():
  list1=[]
 
  list1.append(('Search','RoyaTV',1009,"img/search.png"))##user channel id
  list1.append(('Live','O0-JGo-9BDE',1007,"img/live.png", '',1))
  list1.append(('All','RoyaTV',1005,"img/royatv.png", '',1))##user channel name
  list1.append(('Comedy','UC5G85jJLODwu50JYfE3x1BA','1001',"img/comedy.jpg", '',1))##user channel id
  list1.append(('Drama','UCBVvowMVFC6Ij6Fc2u1L9MA','1001',"img/drama.jpg", '',1))##user channel id
  list1.append(('News','UCsDQbVxQjBuFOa98vxRlbVQ','1001',"img/news.jpg", '',1))##user channel id
  list1.append(('Sport','UCkmc2z6Ot8Qgw0RpsxtxzkQ','1001',"img/sport.jpg", '',1))##user channel id
  list1.append(('Donya Ya Donya','UCFCf55NNK0iG_Q_5HzGhGpA','1001',"img/donya.jpg", '',1))##user channel id
  list1.append(('Kids','UCCASfGJ7ktemgGgFW84giDA','1001',"img/kids.jpg", '',1))##user channel id
  list1.append(('Kitchen','UCR5RnJywFDicUFcPlsQ0jFw','1001',"img/kitchen.jpg", '',1))##user channel id
  list1.append(('Music','UC3xAt_zTCoPL3EDp-swKu8Q','1001',"img/music.jpg", '',1))##user channel id
  list1.append(('StreetJKS','UCNuAN4U8nNmRp87HhH4dNgQ','1001',"img/street.jpg", '',1))##user channel id
  list1.append(('Fenjal Al-Balad','UCqsH6wReyw6vQedecHRjlBg','1001',"img/Fenjalalbald.jpg", '',1))##user channel id
  return list1

################################################################333
def start():
   list1=infolist()
   process_mode(list1,addDir)
   return endDir()


















