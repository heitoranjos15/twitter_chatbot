from datetime import datetime
import twitter
import requests
import json

bot_twitter = twitter.Api(consumer_key="NZTVPmJ7u32rUNppF6dHNWWJW",
                  consumer_secret="qp7fCiQQdQIdAldCQlXuXR4hRUoMeoQsba2wDdYDuLBPZxy3OI",
                  access_token_key="1198666284562563073-iXYTrYNICWoX7Cu7qWEqNJhmVVdYvN",
                  access_token_secret="kIQSpHmgMNe60wHjAYXHguRBkLV44wx4hJUkZAESgjPq7")

# bot_twitter.PostUpdate('Hello world')
since =  datetime.now().strftime('%Y-%m-%d')
twitts = bot_twitter.GetSearch(term="fizzbuzz", since=since, result_type="recent")
for twitt in twitts:
    print(twitt)
    data_twitt = {
      'quote': twitt.text,
      'user':{
        'name': twitt.user.name,
        'plataform': 'twitter'
      }
    }
    response = requests.post('http://127.0.0.1:5000/answer', data=json.dumps(data_twitt))
    if response.status_code == 200:
      message = json.loads(response.text).get('message')
      bot_twitter.PostUpdate(status=message, in_reply_to_status_id=twitt.id)
    else:
      bot_twitter.PostUpdate(status='Mensagem invalida!', in_reply_to_status_id=twitt.id)
