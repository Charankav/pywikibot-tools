import pywikibot

# Connect to the Malayalam Wikisource
site = pywikibot.Site('ml', 'wikisource')

# Loop through the page numbers
for i in range(1, 2):  # From test1 to test10
    page_title = f"ഉപയോക്താവ്:Akbarali/test{i}"
    page = pywikibot.Page(site, page_title)
    
    # Text to add
    new_content = f"{{{{center|{i + 1}}}}}\n"  # Adds 7 to align with the sequence starting at 8
    
    # Check if the page exists
    if page.exists():
        original_text = page.text
        
        # Prepend the new content only if it is not already there
        if not original_text.startswith(new_content.strip()):
            updated_text = new_content + original_text
            page.text = updated_text
            page.save(summary=f"Added centered page number {i + 1}")
            print(f"Successfully updated the page: {page_title}")
        else:
            print(f"The page {page_title} already contains the correct centered page number.")
    else:
        print(f"The page {page_title} does not exist.")
