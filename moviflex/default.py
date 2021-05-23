# -*- coding: utf8 -*-

import sys
import urllib,urllib2,re,os,json
from xbmctools import Item,readnet,get_params,getDomain,resolvehost,playlink,trace_error,cleanhtml,getsearchtext
extra={}
item=Item()
addDir=item.addDir
endDir=item.endDir

##########################################main menu
baseurl = 'https://www.moviflex.net'
      
##########################################main menu

def showmenu():       
        
        addDir('Search','https://www.moviflex.net/?s=prison',103,'img/search.png','',1)
	addDir('الافلام','https://www.moviflex.net/movies/',100,'img/1.png','',1)

        addDir('المسلسلات','https://www.moviflex.net/tvshows/',200,'img/2.png','',1)	


def search(name,sterm,page):
                url='https://www.moviflex.net/?s='+sterm ##sterm presents the name of movies to search for
      
                data=readnet(url)##get source code
                blocks=data.split('class="result-item"')#split data to blocks

                #print number of blocks,same as number of movies in first page in the link above
                print "blocks count",len(blocks)

                i=0  #counter
                for block in blocks:#for loop to iterate all blocks to get movie information
                    i=i+1 #counter
                    if i==1:## if block number continue to next block,because first block does not have movie information
                        continue


                    regx='''alt="(.*?)"'''###title of the movie
                    title=re.findall(regx,block, re.M|re.I)[0]
                    regx='''href="(.*?)"'''##link for movie
                    href=re.findall(regx,block, re.M|re.I)[0]
                    regx='''src="(.*?)"'''###image of the movie
                    image=re.findall(regx,block, re.M|re.I)[0]


                    print "***********************************"
                    print "title:" +title
                    print "href:" +href
                    print "image:" +image
                    if 'tvshows' in href:## if link includes tvshows word then it is series
                            mode=202
                    else:##else should be movie
                             mode=1
                    addDir(title,href,mode,image,name,1)


        
def getmovies(name,url,page):##movies
                if page>1:
                       url=url+'page/'+str(page)+'/' ## this line create link for next page



        
                data=readnet(url)
                blocks=data.split('class="poster">')

                #print number of blocks,same as number of movies in first page in the link above
                print "blocks count",len(blocks)

                i=0  #counter
                for block in blocks:#for loop to iterate all blocks to get movie information
                    i=i+1 #counter
                    if i==1:## if block number continue to next block,because first block does not have movie information
                        continue


                    regx='''alt="(.*?)"'''###title of the movie
                    title=re.findall(regx,block, re.M|re.I)[0]
                    regx='''href="(.*?)"'''##link for movie
                    href=re.findall(regx,block, re.M|re.I)[0]
                    regx='''src="(.*?)"'''###image of the movie
                    image=re.findall(regx,block, re.M|re.I)[0]


                    print "***********************************"
                    print "title:" +title
                    print "href:" +href
                    print "image:" +image
                    addDir(title,href,1,image,name,1)
                if len(blocks)>25: #25number  of movies in one page
                       addDir("next page",url,100,"img/next.png",name,str(page+1))####add this line to store code for next page
              
def getseries(name,url,page):##TVshows
                if page>1:
                       url=url+'page/'+str(page)+'/' ## this line create link for next page



        
                data=readnet(url)##get source code
                blocks=data.split('''class="poster">''')##split to series to blocks

                #print number of blocks,same as number of series in first page in the link above
                print "blocks count",len(blocks)

                i=0  #counter
                for block in blocks:#for loop to iterate all blocks to get movie information
                    i=i+1 #counter
                    if i==1:## if block number continue to next block,because first block does not have msries information
                        continue


                    regx='''alt="(.*?)"'''###title of the movie
                    title=re.findall(regx,block, re.M|re.I)[0]
                    regx='''href="(.*?)"'''##link for movie
                    href=re.findall(regx,block, re.M|re.I)[0]
                    regx='''src="(.*?)"'''###image of the movie
                    image=re.findall(regx,block, re.M|re.I)[0]


                    print "***********************************"
                    print "title:" +title
                    print "href:" +href
                    print "image:" +image
                    addDir(title,href,202,image,name,1)
                if len(blocks)>25: #25number  of movies in one page
                       addDir("next page",url,200,"img/next.png",name,str(page+1))####add this line to store code for next page
              
def getepisodes(name,url,img,page):##TVshows
                
                data=readnet(url)##to get source code of moviflex series page
                blocks=data.split('class="imagen"')##split episodes info to blocks

                #print number of blocks,same as number of movies in first page in the link above
                print "blocks count",len(blocks)

                i=0  #counter
                for block in blocks:#for loop to iterate all blocks to get series information
                    i=i+1 #counter
                    if i==1:## if block number continue to next block,because first block does not have movie information
                        continue


                    regx='''<div class="numerando">(.*?)</div>'''###to get season number and episode number
                    title=re.findall(regx,block, re.M|re.I)[0]
                    title="episode-"+title# add word episode to extracted title
                    regx='''href="(.*?)"'''##link for episode
                    href=re.findall(regx,block, re.M|re.I)[0]
                    regx='''src="(.*?)"'''###to get poster of the episode
                    image=re.findall(regx,block, re.M|re.I)[0]


                    print "***********************************"
                    print "title:" +title
                    print "href:" +href
                    print "image:" +image
                    addDir(title,href,1,image,name,1)#mode 1 to go getservers funtion
                
def getservers(name,url,image):##get servers
               
         data=readnet(url)###get source code of the movie website
         
         regx='''<iframe id="iframe_" class="metaframe rptss" src="(.*?)" frameborder="0" scrolling="no" allowfullscreen="true"></iframe>'''
         hrefs=re.findall(regx,data, re.M|re.I)
         for href in hrefs:
                 print "href",href
                 server,img,issupported=getDomain(href) ###function to get name,image if server and if supported by TSmedia
                 #store information about server to read by TSmedia
                 addDir(server,href,2,image,name,1) 
         return
                 


def start():  
        params=get_params()
        url=None
        name=None
        mode=None
        page=1
        name=params.get("name",None)
        url=params.get("url",None)
        try:mode=int(params.get("mode",None))
        except:mode=None
        image=params.get("image",None)
        section=params.get("section",None)
        page=int(params.get("page",1))
        extra=params.get("extra",{})
        try:extra=ast.literal_eval(extra)
        except:extra={}
        show=params.get("show",None)       
        ##menu and tools
       
        if mode==None:
                print ""
                showmenu()
        ##parsing tools
        elif mode==1:
                print ""+url
                getservers(name,url,image)
        elif mode==2:
                print ""+url
                resolvehost(Item,name,url)

                
        elif mode==100:
                print ""+url
                getmovies(name,url,page)
        elif mode==200:
                print ""+url
                getseries(name,url,page)
        elif mode==202:
                print ""+url
                getepisodes(name,url,image,page)                
        elif mode==103:
                print ""+url
                sterm=getsearchtext()
                search(name,sterm,page)        
        return endDir()
      	
        
