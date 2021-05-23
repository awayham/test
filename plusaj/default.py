# -*- coding: utf-8 -*-

import sys
from yttools import *
from xbmctools import Item
item=Item()
addDir=item.addDir_tube
endDir=item.endDir

def infolist():
  list1=[]

  list1.append(('+AJ كبريت','UC-4KnPMmZzwAzW7SbVATUZQ','1001',"img/channel.png", '',1))## channel id
  
 
  
  return list1

################################################################333
def start():
   list1=infolist()
   process_mode(list1,addDir)
   return endDir()


















