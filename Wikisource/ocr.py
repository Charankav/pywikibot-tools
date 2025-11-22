import pywikibot

# Set up the site
site = pywikibot.Site('ml', 'wikisource')
site.login()  # Ensure you're logged in

# Specify the page to access
page = pywikibot.Page(site, "താൾ:തിരുവിതാംകൂർചരിത്രം.pdf/23")

# Print page content
print(page.text)

# Optional: Edit page content
page.text = page.text + "\nAdding new content here"
page.save("Automated edit with Pywikibot")
