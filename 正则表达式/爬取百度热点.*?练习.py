import requests
import re

url = 'https://www.baidu.com/'

#response = requests.get(url)

#response.encoding = 'utf-8'

headers = {
     'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}
cookies = {
    'cookies':'BIDUPSID=D5D4E3D5626993852C78D1B960C3AC64; PSTM=1726056791; BAIDUID=D5D4E3D562699385D4529553FC644A57:FG=1; H_WISE_SIDS_BFESS=60728_60360_60748; BD_UPN=123253; ispeed_lsm=2; BAIDUID_BFESS=D5D4E3D562699385D4529553FC644A57:FG=1; ZFY=jzZBJ0HAsYfssrqeDuwgAmj:AgxKthdCKSXYx2ZM2P5k:C; H_WISE_SIDS=62325_62968_63030_63056_63194_63242_63247; baikeVisitId=10236c5a-8133-482e-a706-ab9f9d12f273; BD_HOME=1; BA_HECTOR=a50g800g25ag00a08g2k21a4812l261k36ir124; BD_CK_SAM=1; PSINO=5; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=1185435_0_9_8_5_58_1_0_7_8_1_6_1207617_0_0_0_1746150870_0_1748192103%7C9%231671688_10_1744115686%7C4; RT="z=1&dm=baidu.com&si=0af4761d-89a7-4d9e-89fd-c69d0ca69def&ss=mb49uk3v&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=biu"; H_PS_PSSID=62325_62968_63144_63194_63211_63242_63247_63254_63325_63353_63369'
}
response = requests.get(url=url, cookies=cookies, headers=headers)

#print(response.text)

#数据解析
ret = re.findall('<span class="title-content-title">.*?</span>', response.text, re.S)

print(f"总共有{len(ret)}条热点")
print("它们是：")
for title in ret:
    print(title)

