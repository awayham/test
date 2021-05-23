# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TSmedia/lib/syspath.py
import sys
import os 
scripts = '/usr/lib/enigma2/python/Plugins/Extensions/TSmedia/scripts'
def trace_error():
    import sys
    import traceback
    traceback.print_exc(file=sys.stdout)
    logfile = '/tmp/TSmedia/TSmedia_log'
    if os.path.exists(logfile):
        pass
    else:
        logfile = '/tmp/TSmedia_log'
    traceback.print_exc(file=open(logfile, 'a'))

try:
       for name in os.listdir(scripts):
              if "script." in name:
                      fold = scripts + "/" + name + "/lib"
                      print "fold",fold
                      sys.path.append(fold)

      
except:
       trace_error()
sys.argv[0]=sys.argv[0]


try:
       
    sys.argv[0]=sys.argv[0].replace("psyspath","default")
    try:sys.argv[2]=sys.argv[2].strip()
    except:pass
    import default
    
except:
    trace_error()
