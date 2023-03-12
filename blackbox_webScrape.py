from tiktokscraper import scrape

Tiktok = scrape.create()

Tiktok.get_follwer_count('@example_user')

total_followers = Tiktok.get_follwer_count('@example_user')

print(total_followers)