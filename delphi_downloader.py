# -*- encoding: utf-8 -*-
__author__ = 'changchang'

import bs4
import requests

def saveFile(fileName, data):
    import os
    if 'downloads' not in os.listdir('.'):
        os.mkdir('downloads');
    with open('downloads/' + fileName,mode='wb') as f:
        f.write(data.content);

def postDownloadFile(fileName):
    downLoadURL = 'https://www.delmadang.com/community/download.asp'
    payloads = {'index':'defaultcategory', 'bbsNo':'18', 'downfile':fileName}
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Referer': 'https://www.delmadang.com/community/bbs_view.asp?bbsNo=18&bbsCat=0&indx=435165&page=1',
                'Accept-Encoding': 'gzip,deflate',
                'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
                 }
    return requests.post(downLoadURL, data = payloads, headers=headers)

def main():
    #1)BoardItem URL 435165
    for index in xrange(435215,435216,1) :
        bbsNo = 18
        boardURL = 'https://www.delmadang.com/community/bbs_view.asp?bbsNo=%d&bbsCat=0&page=1&indx=%d'%(bbsNo,index)
        #2)Get fileName From HTML
        response = requests.get(boardURL)
    #    print type(response.text)
    #    print response.encoding    #BeautifulSoup has auto detection #ISO-8859-1 서유럽 방식 (8비트 인코딩)
                                    #response.text는 ISO-8859-1로 잘못 디코딩되었다. (잘못된 유니코드)
                                    #1)따라서 다시 인코딩한 후 bs4의 auto detect를 사용하거나
                                    #2)또는 원래 문서의 인코딩을 찾아서 디코딩 한다.(euc-kr)
        tags = bs4.BeautifulSoup(response.text.encode(response.encoding)).find_all('a',class_='9g cg2');
        fileName = tags[0].text if tags != [] else None
        if None == fileName :
            continue
        #3)Download File
        print '[download] %s'%(fileName)
        data = postDownloadFile(fileName)
        saveFile(fileName,data)

if __name__ == '__main__':
    main();
