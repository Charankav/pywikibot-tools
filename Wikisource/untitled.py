import pywikibot

# Define the site
site = pywikibot.Site('ar', 'wikisource')

# Loop to create pages and add page numbers
for i in range(1, 13):
    # Set the correct page title
    page_title = f'فهرس:Qaseedath Burda.pdf/{i}'
    page = pywikibot.Page(site, page_title)

    # Add page number at the top center
    page_number = i
    page.text = f"<center>Page {page_number}</center>\n"

    # Save the page with a summary
    page.save(summary=f"Created page and added page number {page_number} at the top center")
    print(f"Page '{page_title}' was created.")
