import openai
import wikipedia

# pass the api key
# NEVER upload this to Github
openai.api_key = 'api_key_here'

# get user input
title = input('title of the page: ')

# get the wikipedia content
page = wikipedia.page(title = title, auto_suggest = False)


# define the prompt
prompt = 'Write a summary of the following article: ' + page.content[:10000]
messages = []
messages.append({'role': 'user', 'content': prompt})

try:
    # make an api call
    response = openai.completions.create(model = 'gpt-3.5-turbo-instruct', prompt = messages,)

    # print the response
    print(response.choices[0].message.content)
except openai.AuthenticationError:
    print('no valid token / authentication error')
except openai.BadRequestError as e:
    print('invalid request, read the manual!')
    print(e)