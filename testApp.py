# TikTokApi uses a verify_fp parameter to authenticate requests. 
# You can try using a different value for verify_fp to bypass the captcha. 
# You can generate a new verify_fp value by going to tiktok.com and inspecting 
# the headers of any network request. You can copy the value of the s_v_web_id 
# cookie and use it as the verify_fp parameter in your code. Replace your_verify_fp with 
# the s_v_web_id cookie value

from TikTokApi import TikTokApi

api = TikTokApi.get_instance(custom_verify_fp="your_verify_fp")

with api:
    user = api.user(username='Cherrius_')
    user.as_dict
    for video in user.videos():
        print(video.stats())

#function to web scrape tik tok @Cherrius_ for total video view count