#by Changwon 
#email :qwefgh90@naver.com
#taget :https://play.google.com/store/apps/details?id=com.kakao.talk&hl=ko
#review Crawler



import requests as rs

def getReview(pageNum):
	playURL = 'https://play.google.com/store/getreviews'
	header = {
'accept':'*/*',
'accept-encoding':'gzip,deflate',
'accept-language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
'cache-control':'no-cache',
'content-length':120,
'content-type':'application/x-www-form-urlencoded;charset=UTF-8',
'cookie':'NID=67=IK2e12URE2XTPBN2yNaaO79IFmAzthMKNSVYHJYFVNrNYXuGOTvtjf9Qpe1OeuwBkxOFDEF_Ekw-4BupmaJ52O6o6sbxanxKYHa1HFD1nAzinscCnmMBqJMYTRCTbFFvcnB1bb5xtIX-kVX4zcRNEaYK2pxTwqVplOQafJE; PREF=ID=743ae16d10c9dfd5:U=49388268792851f8:FF=0:LD=ko:TM=1412493153:LM=1413728432:S=NrHevrTYdZ6eBb1r; HSID=ALe-6s-RQ_O-8hPj4; SSID=At9bNo3Tjt1rPhAL_; APISID=60V6FfwaijN1fSW2/ApvFKlGwTConaOH78; SAPISID=VzMV3TsGCBMmUApH/AIQTT8mWOa5XURWsZ; SID=DQAAAPcAAAAcT0E6DiOS1UJ333Mp9kTOtL98XkSOI1jqpi34ammt6YAM2r6iECElJMB14Qlyx97-Rpj0pVmchcNfEZpR4CRJNJ_RMXeRY_VL2eM1gkA3vrZszXHjjDmQq9u2iKmhx6dTPCpRwkHWolZDVSu8WjQafWuiAn0aHeambc_itX5Gy0iA_glp65WONS-SHNiTIu5MT9RMQ6kiO_uS5ILVu9n8SDxL0t51YDxtM-1yz-aeL8t_J4Qn64SHZZY70kOGA7qT_i7fuQKoiBwFIbG0AYZD5LNP_857RQXVXsw9cCvDYvSqRZbif3uY0gMDzCk39YeIw9FFiomuw8DPbOrZcNi9; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=qwefgh90@gmail.com; PLAY_PREFS=CgJLUhClktWwnCkiI2NsOmRldGFpbHMuZG91YmxlX2ZldGNoX3NvY2lhbF9kYXRhIidjbDpkZXRhaWxzLmhpZGVfZG93bmxvYWRfY291bnRfaW5fdGl0bGUiD2NvbnRlbnRfcmF0aW5ncyITbmV3X21lcmNoYW50X3NpZ251cCIcbm9jYWNoZTphY3RpdmVfYXBwc19hY3F1aXJlciIVbm9jYWNoZTpib29rc19kb3JtYW50Ih9ub2NhY2hlOmNoYXJ0czptb3ZpZV9wcmVfb3JkZXJzIhtub2NhY2hlOmVuYWJsZV9wbGF5X2NvdW50cnkiM25vY2FjaGU6ZW5hYmxlX3VseXNzZXNfY29tcGF0aWJsZV9zdWJzY3JpcHRpb25fY29kZSIVbm9jYWNoZTplbmNyeXB0ZWRfYXBrIhZub2NhY2hlOmlidF9leHBlcmltZW50IhZub2NhY2hlOm11c2ljX3N1Yl9ub25lIiJub2NhY2hlOm5ld191c2VyX2NsdXN0ZXJfbWFnYXppbmVzIh5ub2NhY2hlOm5ld191c2VyX2NsdXN0ZXJfbXVzaWMiHm5vY2FjaGU6bmV3X3VzZXJfY2x1c3Rlcl9vY2VhbiIgbm9jYWNoZTpuZXdfdXNlcl9jbHVzdGVyX3lvdXR1YmUiHG5vY2FjaGU6bmV3X3VzZXJfZXhwX2RheV9vbGQiGm5vY2FjaGU6bmV3X3VzZXJfbWFnYXppbmVzIhZub2NhY2hlOm5ld191c2VyX211c2ljIhZub2NhY2hlOm5ld191c2VyX29jZWFuIhhub2NhY2hlOm5ld191c2VyX3lvdXR1YmUiDm5vY2FjaGU6bm9fZm9wIipub2NhY2hlOm5vbl9zdWJfbm9uX211c2ljX3VzZXJfd2l0aG91dF9mb3AiIW5vY2FjaGU6bm90X25ld191c2VyX2FuZHJvaWRfYXBwcyIpbm9jYWNoZTpwbGF0b19hYl9hbGxfdXNlcnNfMjVfYWIxX2NvbnRyb2wiKG5vY2FjaGU6cGxhdG9fYWJfYWxsX3VzZXJzXzI1X2FiMl9ub3JtYWwiKW5vY2FjaGU6cGxhdG9fYWJfYWxsX3VzZXJzXzI1X2FiM19jb250cm9sIiFub2NhY2hlOnBsYXRvX2FiX2FsbF91c2Vyc18yNV9hYjQiKG5vY2FjaGU6cGxhdG9fYWJfYWxsX3VzZXJzXzI1X2FiNV9ub3JtYWwiNm5vY2FjaGU6cmVjczpsYXNlcl9yZWxhdGVkX2Zvcl9tb3ZpZXNfMjAxNDExMTJfY29udHJvbCIybm9jYWNoZTp0YXJnZXRlZF9wcm9tbzpub19uZXh1c182X211c2ljX2FsbF9hY2Nlc3MiFm5vY2FjaGU6dXNlcl9jaGFsbGVuZ2UiDG9mZmxpbmVfYXBwcyIPb2ZmbGluZV9hcnRpc3RzIg1vZmZsaW5lX211c2ljKKWS1bCcKQ:S:ANO1ljIW7dSLA4pU; _ga=GA1.3.627220286.1416367298; _gat=1',
'dnt':1,
'origin':'https://play.google.com',
'pragma':'no-cache',
'referer':'https://play.google.com/store/apps/details?id=com.kakao.talk&hl=ko',
'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36',
'x-client-data':'CJC2yQEIo7bJAQiptskBCMG2yQEInobKAQjqiMoBCKOSygEI9pPKAQjelsoB',
}
	playload ={
	'reviewType':0,
'pageNum':pageNum,
'id':'com.kakao.talk',
'reviewSortOrder':4,
'xhr':1,
'token':'rPjTyxlektqwdI9HO-N1gP3u4FE:1416368765094',
'hl':'ko'
	}

	return rs.post(playURL, headers = header, data=playload)

def getBS4Controller(pageNum):
	import json
	resp = getReview(pageNum);
	import bs4
	reviewText = json.loads(resp.text[4:])[0][2].strip();
	#return reviewText
	controller = bs4.BeautifulSoup(reviewText)
	return controller
	
def getTree(pageNum):
	controller = getBS4Controller(pageNum);
	findList = controller.find_all('span',class_="review-title")
	return findList

def saveHTMLToFile():
	for pageNum in xrange(10):
		with open('page%d.html'%(pageNum),'w') as fp:
			text= getBS4Controller(pageNum);
			fp.write(str(text))

def getGoogle():
	return rs.get('http://www.google.com')