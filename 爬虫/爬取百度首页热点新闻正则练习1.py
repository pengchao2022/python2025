import requests
import re

url = 'https://www.baidu.com/'

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

cookies = {
    'cookie':'BIDUPSID=D5D4E3D5626993852C78D1B960C3AC64; PSTM=1726056791; BAIDUID=D5D4E3D562699385D4529553FC644A57:FG=1; H_WISE_SIDS_BFESS=60728_60360_60748; BD_UPN=123253; ispeed_lsm=2; BAIDUID_BFESS=D5D4E3D562699385D4529553FC644A57:FG=1; ZFY=jzZBJ0HAsYfssrqeDuwgAmj:AgxKthdCKSXYx2ZM2P5k:C; H_WISE_SIDS=62325_62968_63030_63056_63194_63242_63247; baikeVisitId=10236c5a-8133-482e-a706-ab9f9d12f273; BD_HOME=1; BD_CK_SAM=1; PSINO=5; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=1185435_0_9_8_5_58_1_0_7_8_1_6_1207617_0_0_0_1746150870_0_1748192103%7C9%231671688_10_1744115686%7C4; RT="z=1&dm=baidu.com&si=0af4761d-89a7-4d9e-89fd-c69d0ca69def&ss=mb49uk3v&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=biu"; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; BA_HECTOR=2g0h8h2k0k04ak2485ah2l8h85240m1k39sq624; H_PS_PSSID=62325_62968_63144_63194_63211_63242_63247_63254_63325_63353_63369_63389_63186; BDSVRTM=3'
}

response = requests.get(url=url, headers=headers, cookies=cookies)
print(f"HTTP 请求返回记录：{response.status_code}")

#print(response.text)
#编写正则过滤新闻热点
ret = re.findall('<span class="title-content-title">.*?</span>', response.text)
print(f"总共有{len(ret)}条热点")
print()

#print(ret)
#for news in ret:
    #print(news)

# 提取中文核心内容（保留标点）
chinese_titles = [re.search(r'>([^<]+)</', item).group(1) for item in ret]

# 打印结果
for title in chinese_titles:
    print(title)
    print()
print("显示完毕！")
