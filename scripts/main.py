from frontMatter import FrontMatter
from walk import Walk
from datetime import TimeStampToTime 
from file import getFileTime 
import os

if __name__=="__main__":
    f_path = "C:/Users/李枫/Desktop/hugoHome/content/posts/生活记录/一些网站密码.md"
    w = Walk('content')
    
    for f_path in w.getFiles():
        if "_index.md" in f_path:
            continue
        fm = FrontMatter(f_path)
        ctime = getFileTime(f_path,'Create')
        ctime = TimeStampToTime(ctime)
        mtime = getFileTime(f_path,'Modify')
        mtime = TimeStampToTime(mtime)
        fm.setMdFMValue('PublishDate',ctime)
        # fm.setMdFMValue('Lastmod',mtime)
        # fm.delMdFMValue('PublishDate')
        fm.delMdFMValue('Lastmod')