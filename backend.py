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

    with open("examples.txt") as fp:
        Lines = fp.readlines()
        for line in Lines:
            a, b = line.split(';', 1)
            gpt.add_example(Example(a, b))

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
