from TikTokApi import TikTokApi

with TikTokApi() as api:
    user = api.user(username='Cherrius_')
    user.as_dict
    for video in user.videos():
        print(video.stats())
        

    #for video in user.videos():
     #   print(video.views)
      #  count += video.views
        # print(video.id)

    #print(count)
