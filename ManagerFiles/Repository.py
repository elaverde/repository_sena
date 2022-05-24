import os
import time
class Repository:

    def get_last_update_repository(self,path):
        ti_m = os.path.getmtime(path) 
        m_ti = time.ctime(ti_m) 
        t_obj = time.strptime(m_ti) 
        T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj) 
        return T_stamp

    def format_size(size,format='bytes'):
        if (size == 0):
            return "0"
        if(format=='bytes'):
            return str(size)+ " Bytes"
        if (format=='auto'):
            if (size >= 1073741824):
                size = size / 1073741824
                return str(round(size,2)) + " GB"
            if (size >= 1048576 ):
                return str(round(size/1048576,2))+ " MB"
            if (size>=1024):
                return str(round(size/1024,2))+ " KB"
            
            
    def size(self,path,format='auto'):
        size=0
        if (os.path.isdir(path)):
            try:
                for path, dirs, files in os.walk(path):
                    for f in files:
                        fp = os.path.join(path, f)
                        size += os.path.getsize(fp)
                return self.format_size(size,format)
            except:
                return "fallo"
        else:
            size = os.path.getsize(path)
            return self.format_size(size,format)

            