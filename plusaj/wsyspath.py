import sys

print "we are here",sys.argv
import os

######################################

dpath=__file__.split("addons")[0]
nparam=sys.argv[2].replace( "AxNxD","&")
if "?"in nparam:
       nparam=nparam.split("?")[1]
sys.argv[2] =nparam 
print "nparam",nparam
######################################



log_file=dpath+"/tmp/Kodi_log"
log_file1=dpath+"/tmp/Kodi_log1"
xbmclog_file=dpath+"/tmp/TSmedia_log"

#############################################


from os import listdir as os_listdir
import sys
import os


scripts =dpath+"/scripts"
print "beofre  scripts",scripts
if "Kodi" in scripts:
       scripts=open(__file__.replace("wsyspath.py","appPath")).read()+"\scripts"
       print "new  scripts",scripts
      
for name in os_listdir(scripts):
       if "script." in name:
               fold = scripts + "/" + name + "/lib"
               sys.path.append(fold)
#############################################
def trace_error():
                  import sys,traceback
                  traceback.print_exc(file = sys.stdout)
                  traceback.print_exc(file=open(xbmclog_file,"w"))
                 

try:
    sys.argv[0]=sys.argv[0].replace("wsyspath.py","default.py")
    sys.modules["__main__"].__file__=sys.argv[0]

    print "wsyspath",sys.argv[2]
    sys.argv[2]=sys.argv[2].replace('"','')
    print "wsyspath",sys.argv[2]
    
    from default import start
    start()
    
except:
    trace_error()



