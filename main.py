import feedparser
from setup_clients import setup_clients

openAI_client, twilio_client, twilio_phone_number, my_phone_number = setup_clients() #setup global variables for tests. Ew.

def is_affirmative(answer):
    affirmative_responses = {"yes", "yes."}
    return answer in affirmative_responses

def format_response(response):
    return response.choices[0].message.content.strip().lower()

def get_GPT_determination(openAI_client, text):
    try:
        response = openAI_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant who returns 'yes' or 'no' as a boolean response."},
                {"role": "user", "content": f"Is this tweet about SpaceX? '{text}'"}
            ],
            model="gpt-3.5-turbo",
        )
        return response
    except Exception as e:
        print("Well that did not go as planned: {e}")
        return None


def get_most_recent_tweet(feed):
    if not feed.entries:
        print("No entries found in the feed.")
        return None
    return feed.entries[0]

def send_sms(twilio_client, twilio_phone_number, my_phone_number, message):
    twilio_client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=my_phone_number
    )
def is_about_spacex(text):
    response = get_GPT_determination(openAI_client, text)
    answer = format_response(response)
    return is_affirmative(answer)

def get_elon_musk_tweets():
    url = "https://rss.app/feeds/hBAXFi4R57sF7S3y.xml"
    feed = feedparser.parse(url)
    return get_most_recent_tweet(feed)
    

if __name__ == "__main__":
    most_recent_tweet = get_elon_musk_tweets()
    if most_recent_tweet:
        if is_about_spacex(most_recent_tweet.title):
            send_sms(twilio_client, twilio_phone_number, my_phone_number, most_recent_tweet.link)
        else:
            print('nope')
