import os
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

os.makedirs(r'D:/ZhuoMian/爬虫视频', exist_ok=True)  # 自动创建目录，已存在也不报错

# useragent=str(input('请输入user-agent'))
视频url=str(input('请输入视频的url:'))
视频Referer=str(input('请输入视频的Referer:'))
音频url=str(input('请输入音频的url:'))
音频Referer=str(input('请输入音频的Referer:'))


url=视频url
headers={
    'referer':视频Referer,
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
}
res=requests.get(url,headers=headers)
print('-'*50)
# print(res.headers)
open(r'D:/ZhuoMian/爬虫视频/视频.mp4','wb').write(res.content)
print ('视频访问',res.status_code)
print('视频提取完成')
print('-'*50)


url2=音频url
headers2={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'referer':音频Referer}
print('-'*50)
res2=requests.get(url2,headers=headers2)
open(r'D:/ZhuoMian/爬虫视频/音频.mp3','wb').write(res2.content)
print ('音频访问',res2.status_code)
print('音频提取完成')
print('-'*50)


video = VideoFileClip(r"D:/ZhuoMian/爬虫视频/视频.mp4")
audio = AudioFileClip(r"D:/ZhuoMian/爬虫视频/音频.mp3")
video = video.with_audio(audio)  # 把音频贴到视频上
video.write_videofile(r"D:/ZhuoMian/爬虫视频/最终视频.mp4")
print("合并完成 ✅")
