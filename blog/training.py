Categories = [
    "Food blogs",
    "Travel blogs",
    "Health and fitness blogs",
    "Lifestyle blogs",
    "Fashion and beauty blogs",
    "Photography blogs",
    "Personal blogs",
    "DIY craft blogs",
    "Parenting blogs",
    "Music blogs",
    "Business blogs",
    "Art and design blogs",
    "Book and writing blogs",
    "Personal finance blogs",
    "Interior design blogs",
    "Sports blogs",
    'News blogs',
    "Movie blogs",
    "Religion blogs",
    "Political blogs",
    'Tutorials and How-to Guides', 'Latest IndustryNews', 'Current Events', 'Controversial Subjects',
    'Checklists:Do you have all that you need to ____?', 'Listicles', 'Infographics', 'Case Studies', 'Profiles',
    'Interviews', 'dvice from the Experts', 'Reviews', 'Comparisons', 'Video Blogs', 'MP3s', 'Resources',
    'Problem and Solutions', 'Share What Others are Saying', 'A Glance “Behind the Curtain”', 'Inspirational Stories',
    'Parody Posts', 'Funny Posts', 'Quizzes', 'Surveys andPolls', 'Local News (Non-Business)',
    'Presentations and SlideShare', 'Frequently Asked Questions (FAQs)', 'Questions You Should be Asking',
    'Twitter Posts', 'Contests', 'Screencasts', 'Time-Saving Posts (how to)', 'indFunny Videos for Blog Posts',
    'Conference Posts', 'Event Summaries', 'Top Take-Aways From Whatever', 'Think Out Loud Posts', 'Rants',
    'Pop-Culture Commentary', 'Beginner’s Guides', '“Metrics to Measure” Guides', 'Recent Tools You Use',
    'Free Giveaways', 'Guest Bloggers', 'Debates', 'Transcript Posts', 'Myth vs. Fact', 'Monthly Updates and Stats',
    'Preview Posts', 'Answer “Why?”', 'Search Twitter for Inspiration', 'Cheatsheets', 'Criticisms and Open Letters',
    'Share Recent Travel Experiences', 'Gallery/Album Posts', 'Talk About Your Successes and Your Failures',
    'Auto-Biographical Post', 'Share Recipes', 'Curate or Summarize Someone Else’s Work.', 'Holidays',
    'Thankful Posts', 'Show Your Response to an Interesting Customer Question', 'Create a Glossary',
    'Share Who is Important to Follow', 'Best Sources of Inspiration', 'Recount the History of Your Blog or Business',
    'Aspirations for Your Blog/Business', 'Best Mobile Apps for your Industry', 'Roundups', 'Get thoughts fromNewbies',
    'Memes', 'Charity/Awareness posts', 'RecycleOld Posts']


def write_to_csv(stories):
    import csv

    fields = ['Category', 'Title']
    filename = "titles.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(stories)


def get_titles(search):
    from pygooglenews import GoogleNews
    stories = []
    google_news = GoogleNews(country="CN")
    searched = google_news.search(search)
    articles = searched['entries']
    for article in articles:
        story = {
            "Category": search,
            "Title": article.title,
        }
        stories.append(story)
    return stories


def get_titles_in_csv():
    stories = []
    for each_category in Categories:
        stories += get_titles(each_category)

    write_to_csv(stories)


def get_keywords(text):
    from rake_nltk import Rake
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()[:4]
    print(keyword_extracted)

    return keyword_extracted


def get_dict_from_csv():
    import csv

    filename = "titles.csv"

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            category = row[0]
            title = row[1].split("-")[0].strip()
            rows.append({
                "prompt": category + ": " + "".join([kw + "," for kw in get_keywords(title)])[:-1] + "\n\n###\n\n",
                "completion": " " + title + "###",

            })

        return rows


# get_titles_in_csv()

def get_training_set():
    import json
    dataset = get_dict_from_csv()
    path = "training.jsonl"
    with open(path, 'w') as file:
        for entry in dataset:
            jsonl = json.dumps(entry)
            print(jsonl)
            file.write(jsonl + "\n")


get_training_set()
