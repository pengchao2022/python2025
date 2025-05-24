import requests
import re
import json
import pprint

def get_response(html_url):
    """发送请求"""
    
    headers = {
        #加防盗链
        'referer':'https://www.bilibili.com',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

    response = requests.get(url=html_url, headers=headers)
    return response



def get_video_info(html_url):
    response = get_response(html_url)
    #title = re.findall('</script> <title data-vue-meta=(.*?)>', response.text)[0]
    html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    json_data = json.loads(html_data)
    #pprint.pprint(json_data)
    #数据解析,键值对取值
    #音频地址
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    #视频地址
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    video_info =[audio_url, video_url]
    return video_info

    #print(title)
    #print(audio_url)
    #print(video_url)
def save(audio_url, video_url):
    audio_content = get_response(audio_url).content
    video_content = get_response(video_url).content
    with open('.mp3', mode='wb') as f:
        f.write(audio_content)
        
    with open('.mp4', mode='wb') as f:
        f.write(video_content)
    print("保存结束")

        

url = 'https://www.bilibili.com/video/BV1aY4y1R7Gw'
video_info = get_video_info(url)
save(video_info[0],video_info[1])