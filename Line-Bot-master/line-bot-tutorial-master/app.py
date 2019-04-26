from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import random
import json
import requests
import urllib
import certifi
import urllib3
import configparser
import re
from bs4 import BeautifulSoup
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Q6866YeoxQ+WOfZI9eHkYA7728MuaGkpG+uw7JYuqGYkq6F68ldB1kyLWLAElbFklbwjScquMtsezL5FwMZ/o7deHMH1pYa0NCOOAZPx/CmjghEkLB8lrSPmgCwdYIrUjDWG9smhLTs7DP2CNGh++QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f4a2d0051a61763478220fc300ac8882')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, message)
	if event.message.text == '關於我':
		message = TemplateSendMessage(
			alt_text='Buttons template',
			template=ButtonsTemplate(
				thumbnail_image_url='https://cthr.ctgoodjobs.hk/article_images/self-intro-14626_2.jpg',
				title='關於我',
				text='請選擇想知道關於我的資訊~',
				actions=[
					MessageTemplateAction(
						label='自我簡介',
						text='自我簡介'
					),
					MessageTemplateAction(
						label='程式語言',
						text='程式語言'
					),
					MessageTemplateAction(
						label='作品',
						text='作品'
					),
					MessageTemplateAction(
						label='來一則笑話',
						text='來一則笑話'
					)
				]
			)
		)
	elif event.message.text == '自我簡介':
		message = [TextSendMessage(text='您好~我是目前就讀政治大學資管所碩一的林郁豪\n高中曾擔任優良學生、英語研究社副社長，大學參加過系壘、系排系學會幹部，也擔任各大活動負責人\n從大學就開始學習各種程式語言，喜歡探索各種新奇的事物，因此也對開發各種程式很有興趣\n很高興有機會可以來LINE實習'), ImageSendMessage(original_content_url='https://github.com/ho4849123/Line_ChatBot/blob/master/Line-Bot-master/line-bot-tutorial-master/%E7%85%A7%E7%89%87.jpg?raw=true',preview_image_url='https://github.com/ho4849123/Line_ChatBot/blob/master/Line-Bot-master/line-bot-tutorial-master/%E7%85%A7%E7%89%87.jpg?raw=true')]
	elif event.message.text == '程式語言':
		message = [TemplateSendMessage(
			alt_text='ImageCarousel template',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://upload.wikimedia.org/wikipedia/zh/8/88/Java_logo.png',
						action=PostbackTemplateAction(
							label='JAVA',
							text=' ',
							data='action=buy&itemid=1'
						)
					),
					ImageCarouselColumn(
						image_url='https://png.icons8.com/color/1600/c-programming',
						action=PostbackTemplateAction(
							label='C',
							text=' ',
							data='action=buy&itemid=2'
						)
					),
					ImageCarouselColumn(
						image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png',
						action=PostbackTemplateAction(
							label='PYTHON',
							text=' ',
							data='action=buy&itemid=3'
						)
					),
					ImageCarouselColumn(
						image_url='https://pngimage.net/wp-content/uploads/2018/06/php-mysql-png.png',
						action=PostbackTemplateAction(
							label='MYSQL',
							text=' ',
							data='action=buy&itemid=4'
						)
					),
					ImageCarouselColumn(
						image_url='https://www.pngarts.com/files/4/Android-PNG-Image.png',
						action=PostbackTemplateAction(
							label='ANDROID',
							text=' ',
							data='action=buy&itemid=5'
						)
					)
				]
			)
		),TextSendMessage(text='可以左右滑動查看喔!')]
	elif event.message.text == '作品':
		message = TemplateSendMessage(
			alt_text='Carousel template',
			template=CarouselTemplate(
				columns=[
					CarouselColumn(
						thumbnail_image_url='https://img.ltn.com.tw/Upload/3c/page/2015/06/18/150618-18766-1.jpg',
						title='GomourmandGo',
						text='大學專題',
						actions=[
							MessageTemplateAction(
								label='詳細介紹',
								text='作品1介紹'
							),
							MessageTemplateAction(
								label=' ',
								text=' '
							),
							MessageTemplateAction(
								label=' ',
								text=' '
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://www.ctimes.com.tw/news/2016/03/02/1144202490.jpg',
						title='新契約登打系統規則引擎',
						text='實習作品',
						actions=[
							MessageTemplateAction(
								label='詳細介紹',
								text='作品2介紹'
							),
							MessageTemplateAction(
								label=' ',
								text=' '
							),
							MessageTemplateAction(
								label=' ',
								text=' '
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://media.istockphoto.com/vectors/artificial-intelligence-electronic-brain-icon-vector-vector-id1051563164?b=1&k=6&m=1051563164&s=170667a&h=2nhilaTaBTuhXDo6VEYvQFqU8-Iepws2uJK85P0H9vM=',
						title='Python Profiler',
						text='研究所作品',
						actions=[
							MessageTemplateAction(
								label='詳細介紹',
								text='作品3介紹'
							),
							MessageTemplateAction(
								label=' ',
								text=' '
							),
							MessageTemplateAction(
								label=' ',
								text=' '
							)
						]
					)
				]
			)
		)
	elif event.message.text == '作品1介紹':
		message = TextSendMessage(text='這是我在大四做的畢業專題，是一款在ANDROID上的APP，主要的內容是結合餐廳搜尋和娛樂性的APP，功能有在地圖上搜尋附近餐廳、依種類搜尋餐廳、任務功能、成就、好友等等，最主要的特色就是使用者可以接取任務，並到任務指定的餐廳完成任務內容，就可以獲得獎勵，例如:折價券，我們希望借此可以讓使用者探索周圍沒嘗試過的餐廳，餐廳可以獲得新的客流量，而使用者可以獲得折價券，以此達到一個良性的循環。\n這個專題也有參加資訊應用服務創新競賽GCIS-OPENDATA-01商工行政創新雲端-應用組，並進入了決賽')
	elif event.message.text == '作品2介紹':
		message = TextSendMessage(text='這是我在大四下到新光人壽-壽險資訊部實習時的作品，由於保險業的壽險規則會因為各項因素有所改變，例如:修法、科技、新規章...等，但是如果要修改時，一條一條保險的去修改規則，會非常的麻煩，所以公司打算利用規則引擎把各項規則單獨拉成一個系統，而保險的組成包括BOM、詞條、規則，而我們需要讓一個保險的每個元素可以任意新增修改刪除，以適應保險的變更。')
	elif event.message.text == '作品3介紹':
		message = TextSendMessage(text='這是我目前在研究所的研究主題之一，主要是實做一個Python的Function call Profiler，做法是修改Python的source code，compile出一個屬於我客製化的Intepreter，這樣只要用這個Intepreter去執行Python程式，便會自動側錄出各項Function的資訊，例如:名稱、開始結束時間、參數、參數型態、執行時間...等，並且可以依時間序列性的把所有用過的Funtion側錄出來，日後可用於Malware的分析，並且嵌入在IoT的板子上，預測出當前是否有Malware的惡意行為。')
	elif event.message.text == '來一則笑話':
		a=random.randint(1,10)
		if a == 1:
			message = [TextSendMessage(text='為什麼模範生容易被綁架?\n因為他一副好綁樣....') , StickerSendMessage(package_id='1',sticker_id='10')]
		elif a == 2:
			message = [TextSendMessage(text='有個人對著山洞大喊 : 嗚郎滴欸某??\n山洞裡有聲音回答: 嗚 ～\n然後他就被火車撞死了') , StickerSendMessage(package_id='1',sticker_id='100')]
		elif a == 3:
			message = [TextSendMessage(text='為什麼放連假的時候不能去工作？\n因為會變成連假勞工') , StickerSendMessage(package_id='1',sticker_id='14')]
		elif a == 4:
			message = [TextSendMessage(text='小明對小美說你美爆了\n小美就爆了') , StickerSendMessage(package_id='1',sticker_id='10')]
		elif a == 5:
			message = [TextSendMessage(text='大樹跟小樹差在哪裡?\n插在土裡') , StickerSendMessage(package_id='1',sticker_id='100')]
		elif a == 6:
			message = [TextSendMessage(text='小狗跟貓咪誰先上台背課文?\n小狗\n旺旺仙貝') , StickerSendMessage(package_id='1',sticker_id='14')]
		elif a == 7:
			message = [TextSendMessage(text='哪個性別的鯊魚比較大隻？\n母鯊魚比較大 因為公鯊小') , StickerSendMessage(package_id='1',sticker_id='10')]
		elif a == 8:
			message = [TextSendMessage(text='有一天小明去圖書館\n小明：我要一碗牛肉麵\n櫃檯：先生 這裡是圖書館\n小明：喔喔好 （氣音）我要一碗牛肉麵') , StickerSendMessage(package_id='1',sticker_id='100')]		
		elif a == 9:
			message = [TextSendMessage(text='A：你今天有賴床嗎？\nB：有\nA：那他有回你嗎') , StickerSendMessage(package_id='1',sticker_id='14')]
		elif a == 10:
			message = [TextSendMessage(text='有一個人印假鈔被抓到了~\n警察問他為什麼印假鈔?\n因為我不會印真鈔啊') , StickerSendMessage(package_id='1',sticker_id='10')]
	elif '天氣' in event.message.text:
		try:
			http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
			address_replace=event.message.text.replace('台','臺')
			origin = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-33DD2FD4-092A-49D3-8C9F-81691FB530B0&format=JSON&locationName='+ address_replace[:3], verify=False)
			bbbb = json.loads(origin.content)
			timeIntervalPredict = bbbb['records']['location'][0]['weatherElement'][0]['time'][0]
			timeIntervalPredict2 = bbbb['records']['location'][0]['weatherElement'][1]['time'][0]
			timeIntervalPredict3 = bbbb['records']['location'][0]['weatherElement'][2]['time'][0]
			discription_weather = timeIntervalPredict['parameter']['parameterName']
			discription_rain = timeIntervalPredict2['parameter']['parameterName']
			discription_temperature = timeIntervalPredict3['parameter']['parameterName']
			reply = '天氣 : '+str(discription_weather)+'\n降雨機率 : '+str(discription_rain)+'%\n溫度 : ' + str(discription_temperature) +'度'
		except:
			reply='請輸入XX(縣/市)天氣\n例如:臺北市天氣'
		try:
			if '雨' in discription_weather:
				message = [TextSendMessage(text=reply) , StickerSendMessage(package_id='4',sticker_id='266')]
			elif '雲' in discription_weather:
				message = [TextSendMessage(text=reply) , StickerSendMessage(package_id='4',sticker_id='264')]
			else:
				message = [TextSendMessage(text=reply) , StickerSendMessage(package_id='4',sticker_id='263')]
		except:
			message = TextSendMessage(text=reply)
	elif event.message.text == '餐廳查詢' :
		message = TemplateSendMessage(
			alt_text='Buttons template',
			template=ButtonsTemplate(
				thumbnail_image_url='https://icrvb3jy.xinmedia.com/solomo/article/152650/4EE253DB-F14C-30EB-F2B2-663FA3A25AC7.jpeg',
				title='來找間餐廳吧',
				text='不知道吃甚麼的話就隨便來一家吧!',
				actions=[
					MessageTemplateAction(
						label='隨便來一家',
						text='隨便來一家'
					),
					MessageTemplateAction(
						label='依種類餐廳查詢',
						text='餐廳查詢種類'
					),
					MessageTemplateAction(
						label=' ',
						text=' '
					)
				]
			)
		)
	elif '隨便來一家' in event.message.text :
		try:
			address=event.message.text.replace('隨便來一家', '')
			# 預設地址
			#address = event.message.text.split(',')
			# 你的API_KEY
			GOOGLE_API_KEY = 'AIzaSyAlYOHz_WzG7v3Sn6AIVJOqvmwUOA2kmCQ'
			addurl = 'https://maps.googleapis.com/maps/api/geocode/json?key={}&address={}&sensor=false'.format(GOOGLE_API_KEY,address)
			# 經緯度轉換
			addressReq = requests.get(addurl)
			addressDoc = addressReq.json()
			lat = addressDoc['results'][0]['geometry']['location']['lat']
			lng = addressDoc['results'][0]['geometry']['location']['lng']
			# 取得店家資訊
			foodStoreSearch = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}&location={},{}&rankby=distance&type=restaurant&language=zh-TW".format(GOOGLE_API_KEY, lat, lng)
			foodReq = requests.get(foodStoreSearch)
			nearbyRestaurants_dict = foodReq.json()
			top20Restaurants = nearbyRestaurants_dict["results"]
			res_num = (len(top20Restaurants)) 
			# 取評分高於3.9的店家
			bravo=[]
			for i in range(res_num):
				try:
					if top20Restaurants[i]['rating']>3.9:
					# print('rate: ', top20Restaurants[i]['rating'])
						bravo.append(i)
				except:
					KeyError
			if len(bravo) < 0:
				print("沒東西可以吃")
				# restaurant = random.choice(top20Restaurants) 沒有的話隨便選一間
			# 從高於3.9的店家隨機選一間
			restaurant = top20Restaurants[random.choice(bravo)]
			# 檢查餐廳有沒有照片
			if restaurant.get("photos") is None:
				thumbnailImageUrl = None
			else:
				# 取得照片
				photoReference = restaurant["photos"][0]["photo_reference"]
				photoWidth = restaurant["photos"][0]["width"]
				thumbnailImageUrl = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY, photoReference,photoWidth)
			# 餐廳詳細資訊
			rating = "無" if restaurant.get("rating") is None else restaurant["rating"]
			address = "沒有資料" if restaurant.get("vicinity") is None else restaurant["vicinity"]
			details = "評分：{}\n地址：{}".format(rating, address)
			print(restaurant.get("name"))
			print(details)
			# 取得餐廳的 Google map 網址
			mapUrl = "https://www.google.com/maps/search/?api=1&query={lat},{long}&query_place_id={place_id}".format(lat=restaurant["geometry"]["location"]["lat"],long=restaurant["geometry"]["location"]["lng"],place_id=restaurant["place_id"])
			message = TemplateSendMessage(
				alt_text='Buttons template',
				template=ButtonsTemplate(
					thumbnail_image_url=thumbnailImageUrl,
					title=restaurant.get("name"),
					text=details,
					actions=[
						URITemplateAction(
							label='查看地圖',
							uri=mapUrl
						)
					]
				)
			)
		except:
			message = TextSendMessage(text='請輸入隨便來一家+地址\n例如:隨便來一家臺北市信義區')
	elif '餐廳查詢' in event.message.text :	
		try:
			input=event.message.text.replace('餐廳查詢', '')
			x = input.split('，')
			address = x[1]
			category = x[0]
			# 預設地址
			#address = event.message.text.split(',')
			# 你的API_KEY
			GOOGLE_API_KEY = 'AIzaSyAlYOHz_WzG7v3Sn6AIVJOqvmwUOA2kmCQ'
			addurl = 'https://maps.googleapis.com/maps/api/geocode/json?key={}&address={}&sensor=false'.format(GOOGLE_API_KEY,address)
			# 經緯度轉換
			addressReq = requests.get(addurl)
			addressDoc = addressReq.json()
			lat = addressDoc['results'][0]['geometry']['location']['lat']
			lng = addressDoc['results'][0]['geometry']['location']['lng']
			# 取得店家資訊
			foodStoreSearch = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}&location={},{}&rankby=distance&type=restaurant&keyword={}&language=zh-TW".format(GOOGLE_API_KEY, lat, lng, category)
			foodReq = requests.get(foodStoreSearch)
			nearbyRestaurants_dict = foodReq.json()
			top20Restaurants = nearbyRestaurants_dict["results"]
			res_num = (len(top20Restaurants)) 
			# 取評分高於3.9的店家
			bravo=[]
			for i in range(res_num):
				try:
					if top20Restaurants[i]['rating']>3.9:
					# print('rate: ', top20Restaurants[i]['rating'])
						bravo.append(i)
				except:
					KeyError
			if len(bravo) < 0:
				print("沒東西可以吃")
				# restaurant = random.choice(top20Restaurants) 沒有的話隨便選一間
			# 從高於3.9的店家隨機選一間
			restaurant = top20Restaurants[random.choice(bravo)]
			# 檢查餐廳有沒有照片
			if restaurant.get("photos") is None:
				thumbnailImageUrl = None
			else:
				# 取得照片
				photoReference = restaurant["photos"][0]["photo_reference"]
				photoWidth = restaurant["photos"][0]["width"]
				thumbnailImageUrl = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY, photoReference,photoWidth)
			# 餐廳詳細資訊
			rating = "無" if restaurant.get("rating") is None else restaurant["rating"]
			address = "沒有資料" if restaurant.get("vicinity") is None else restaurant["vicinity"]
			details = "評分：{}\n地址：{}".format(rating, address)
			print(restaurant.get("name"))
			print(details)
			# 取得餐廳的 Google map 網址
			mapUrl = "https://www.google.com/maps/search/?api=1&query={lat},{long}&query_place_id={place_id}".format(lat=restaurant["geometry"]["location"]["lat"],long=restaurant["geometry"]["location"]["lng"],place_id=restaurant["place_id"])
			message = TemplateSendMessage(
				alt_text='Buttons template',
				template=ButtonsTemplate(
					thumbnail_image_url=thumbnailImageUrl,
					title=restaurant.get("name"),
					text=details,
					actions=[
						URITemplateAction(
							label='查看地圖',
							uri=mapUrl
						)
					]
				)
			)
		except:
			message = TextSendMessage(text='請輸入 餐廳查詢+種類，地址\n例如 : 餐廳查詢牛排，台北市信義區')
	elif event.message.text=='來點新聞':
		url = 'https://www.dcard.tw/f'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
		resp = requests.get(url, headers=headers)
		soup = BeautifulSoup(resp.text, 'html.parser')
		dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
		dcard_href = soup.find_all('a',re.compile('PostEntry_root_V6g0rd'))
		title_list=[]
		href_list=[]
		for index, item in enumerate(dcard_title[:10]):
			title_list.append(item.text.strip())
			href_list.append(dcard_href[index].get('href'))
		message = TemplateSendMessage(
			alt_text='Buttons template',
			template=ButtonsTemplate(
				thumbnail_image_url='https://en.pimg.jp/010/956/442/1/10956442.jpg',
				title='來點新聞',
				text='來自DCARD的熱門貼文',
				actions=[
					URITemplateAction(
						label=title_list[0][0:20],
						uri='https://www.dcard.tw'+href_list[0]
					),
					URITemplateAction(
						label=title_list[1][0:20],
						uri='https://www.dcard.tw'+href_list[1]
					),
					URITemplateAction(
						label=title_list[2][0:20],
						uri='https://www.dcard.tw'+href_list[2]
					),
					URITemplateAction(
						label=title_list[3][0:20],
						uri='https://www.dcard.tw'+href_list[3]
					)
				]
			)
		)
	else:
		message = TemplateSendMessage(
			alt_text='Buttons template',
			template=ButtonsTemplate(
				thumbnail_image_url='https://steemitimages.com/DQmdLYh8gdzPbpAtZ8L9QLS9NwsQeP3PYZAyzuizGzUPrhB/image.png',
				title='主選單',
				text='請選擇功能',
				actions=[
					MessageTemplateAction(
						label='關於我',
						text='關於我'
					),
					MessageTemplateAction(
						label='來點新聞',
						text='來點新聞'
					),
					MessageTemplateAction(
						label='天氣查詢',
						text='天氣查詢'
					),
					MessageTemplateAction(
						label='餐廳查詢',
						text='餐廳查詢'
					)
				]
			)
		)
	line_bot_api.reply_message(event.reply_token, message)
	

		
	#message = TextSendMessage(reply_text)
	#line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
