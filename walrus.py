tweet_limit = 280
tweet_string = "coś" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("Dobry tweet")
else:
    print("Tweet za długi o", abs(diff), "znaków")

tweet_limit = 280
tweet_string = "coś" * 50
if diff := tweet_limit - len(tweet_string) >= 0:
    print("Dobry tweet")
else:
    print("Tweet za długi o", abs(diff), "znaków")


