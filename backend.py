# Add methods to use GPT
from happytransformer import HappyGeneration, GENSettings
import re


def ideaGenerator(keyword):
    # prompt = """blog ideas for {key} include:
    # 1: Why Billionaires Will Never Invest In {key}.
    # 2: An Expert Interview About {key}.
    # 3: What Everyone Is Saying About {key}.
    # 4: 5 Reasons You Should be Talking About {key}.
    # 5: Who Really Uses {key}.
    # 6: 20 Facts About {key} That Will Impress You.
    # 7: A Foolproof Guide to {key}.
    # 8: How Much Do You Know about {key}?
    # 9: What You Should Wear To {key} events.
    # 10: Attending {key} Can Be A Disaster If You Forget These Five Rules.
    # 11: Is {key} Healthy For You?
    # 12: Why Are Children Getting Addicted To {key} Nowadays?
    # 13: 7 Things Your Boss Needs To Know About {key}.
    # 14: The Millionaire Guide On {key} To Help You Get Rich.
    # 15: I Will Tell You The Truth About {key} In The Next 60 Seconds.
    # 16: In What Ways Can {key} Be Dangerous To Our Health.
    # 17: Pros And Cons of {key}.
    # 16: 12 Secrets About {key}
    # 17: """.format(key=keyword)

    prompt = """blog ideas for pets include:
    1: Why Billionaires Will Never Invest In Pets.
    2: 6 Ways Pets Can Find You the Love of Your Life.
    3: 12 Secrets About Pets.
    4: Create a wish list for your dog or cat.
    5: Do you want another pet? Share why or why not.
    6: Review a pet product that you’re not a fan of."

    blog ideas for cars include:
    1: A Foolproof Guide to buying Cars.
    2: An Expert Interview About Cars.
    3: 13 Insane (But True) Things About Cars.
    4: The Truth About Cars."

    blog ideas for water include:
    1: Wastewater treatment: A critical component of a circular economy.
    2: A low-priced water reuse process that also delivers renewable energy in rural areas.
    3: Time to adapt to changing climate: what does it mean for water?
    4: 16 Astonishing Facts About Water.
    5: Here's how much water you should drink in a day.
    6: Benefits of Drinking a lot of Water."

    blog ideas for fashion include:
    1: The wardrobe tour.
    2: The biggest fashion fails.
    3: Memorable outfits to wear on special occasions.
    4: DIY Fashion tutorials.
    5: Your top fashion hacks.
    6: Things You Should Know About The Fashion Industry."

    blog ideas for health care include:
    1: foods that will boost your immunity.
    2: number of exercises you can do at home with no equipment.
    3: ways to mentally refresh after a stressful day.
    4: Sleep quality and mental health: What the data says.
    5: Why time with friends is essential for your mental health.
    6: From Salt to Turmeric: Common kitchen foods that soothe an itchy throat."

    blog ideas for machine learning include:
    1: Deep Learning Without Labels.
    2: Can AI Generate Programs to Help Automate Busy Work?
    3: AI-Based Virtual Tutors – The Future of Education?
    4: Transfer Learning for Text using Deep Learning Virtual Machine.
    5: A Guide to Natural Language Processing for Text and Speech.
    6: Advancements in Machine Learning and Artificial Intelligence.
    7: When and How Machine Learning can Change the World.
    8: Do You Think You Know Everything About Machine Learning?"

    blog ideas for travel include:
    1: Cheapest Travel Destinations.
    2: The least-visited countries in Europe.
    3: The year to plan a trip with friends.
    4: The future of solo female travel.
    5: The world’s most interesting journeys.
    6: Things to Keep in Mind When travelling alone."

    blog ideas for food include:
    1: The Best Bagels Are in California.
    2: What Our Food Reporters and Editors Make When They’re Too Tired to Cook.
    3: 20 Simple Sauces That Will Transform Any Meal.
    4: 24 Days of Cookies.
    5: This Is How You Get the Best Scrambled Eggs.
    6: Here's why you should have spiced tea in winters."

    blog ideas for {key} include:""".format(key=keyword)

    gpt_neo = HappyGeneration(model_type="GPT-NEO", model_name="EleutherAI/gpt-neo-125M")
    top_k_sampling_settings = GENSettings(do_sample=True, top_k=30, max_length=30, min_length=15)
    output_top_k_sampling = gpt_neo.generate_text(prompt, args=top_k_sampling_settings)

    rawOutput = output_top_k_sampling.text

    # Cleaning
    text = "".join([s for s in rawOutput.splitlines(True) if s.strip("\r\n")])

    output = text.partition('\n')[0]

    # remove number from start
    blogIdea = re.sub(r'\d+', '', output)
    blogIdea = blogIdea.replace(":", "").strip()
    blogIdea = blogIdea.split(".")[0]
    return blogIdea


idea = ideaGenerator("Testing")
print(idea)
