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
]


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


get_titles_in_csv()
