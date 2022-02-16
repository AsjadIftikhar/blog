import openai

from gpt import Example, GPT
import re


def trainedModel(prompt):
    print(openai.Completion.create(
        model="curie:ft-tcma-2022-02-16-11-49-17",
        max_tokens=200,
        prompt=prompt
    )["choices"][0]["text"])


def ideaGenerator(category, keyword):
    import environ

    env = environ.Env()
    environ.Env.read_env()

    openai.api_key = env('API_KEY')

    gpt = GPT(
        engine="text-davinci-001",
        max_tokens=150,
    )
    gpt.add_example(Example('5 blog ideas for water: facts,drink,reuse', """
        1: Wastewater treatment: A critical component of a circular economy.
        2: A low-priced water reuse process that also delivers renewable energy in rural areas.
        3: Time to adapt to changing climate: what does it mean for water?
        4: 16 Astonishing Facts About Water.
        5: Here's how much water you should drink in a day."""))

    gpt.add_example(Example('5 blog ideas for machine learning: Artificial intelligence,future', """
        1: Deep Learning Without Labels.
        2: Can AI Generate Programs to Help Automate Busy Work?
        3: AI-Based Virtual Tutors – The Future of Education?
        4: Transfer Learning for Text using Deep Learning Virtual Machine.
        5: A Guide to Natural Language Processing for Text and Speech."""))

    gpt.add_example(Example('5 blog ideas for sports: news', """
        1: NFL mock draft: Post-Super Bowl look includes surprises in top 10 of first round.
        2: U.S. Speedskater Erin Jackson’s Medal Ceremony Blunder Goes Viral With Outpouring Of Love.
        3: Premier League: How can Tottenham to beat Manchester City?
        4: England thrashed in first T20 international against West Indies.
        5: 2021/2022 snooker season guide, tournament dates, latest news, betting previews and odds."""))

    gpt.add_example(Example('5 blog ideas for entertainment: celebrities', """
        1: CELEBRITY BRIDE GUIDE.
        2: The Best Singers of All Time.
        3: The Most Beautiful Women In Hollywood.
        4: Celebrities Hollywood Forced on Us.
        5: Fun Old Cameos In Movies And TV Shows That Make You Cringe Now."""))

    gpt.add_example(Example('5 blog ideas for entertainment: comedy', """
        1: The Best Current Dark Comedy TV Shows.
        2: The Best Sitcoms Of The '70s.
        3: The Funniest British and Irish Comedians of all Time.
        4: The Best Celebrity Impersonators Ever.
        5: The Funniest Female Comedians of All Time."""))

    gpt.add_example(Example('5 blog ideas for food: kitchen,eats,food science', """
        1: 5 Design Professionals on What Makes a Timeless Kitchen.
        2: 19 Savory Drinking Snacks from Around the World.
        3: How the Science of Salt can Improve your Tomatoes?
        4: The History of Hibiscus Drinks in the African Diaspora.
        5: Top 10 Instant Noodles from Around the World."""))

    gpt.add_example(Example('5 blog ideas for Photography: Photography,Videography,Camera', """
        1: 3 Bags for your Mirrorless Camera You’ll Love.
        2: Why Photography Without Photoshop Is Brilliant, Exciting, and Important?
        3: Photo Editing: Why It’s Important Not to Do It Too Soon.
        4: 5 of the Best Highlights From Inside the Photographer’s Mind.
        5: 5 Fun Things You’ll Enjoy Trying with Your New Camera!"""))

    prompt = """5 blog ideas for {category} include: {keywords}\n\n###\n\n""".format(category=category,
                                                                                     keywords=keyword)

    rawOutput = gpt.get_top_reply(prompt)
    cleanText = "\n".join([ll.rstrip() for ll in rawOutput.splitlines() if ll.strip()])
    blogIdea = cleanText.splitlines()

    return blogIdea


# idea = ideaGenerator("health care", "mental health")
# print(idea)
