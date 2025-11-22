import pywikibot

def add_category_to_article(page_title, category):
    site = pywikibot.Site('ar', 'wikipedia')  # Arabic Wikipedia
    page = pywikibot.Page(site, page_title)

    # Check if the page exists
    if not page.exists():
        print(f"Page '{page_title}' does not exist.")
        return

    # Check if the page already has the category
    if category in page.categories():
        print(f"Page '{page_title}' already has the category '{category}'.")
        return

    # Add the category to the page
    page.text += f"\n[[تصنيف:{category}]]"
    page.save(f"Adding category '{category}' ")

def main():
    articles = [
" بريانكا غاندي "

    ]

    category = "البانديت الكشميريين"

    for article in articles:
        add_category_to_article(article, category)

if __name__ == "__main__":
    main()