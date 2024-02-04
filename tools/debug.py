import sys
sys.path.append('/home/speedy/Development/Phase3/articles-without-sqlalchemy-Emmanuel-Oite')

from lib.Author import Author
from lib.Magazine import Magazine


# Create instances of authors and magazines
author1 = Author("John Doe")
author2 = Author("Jane Smith")
magazine1 = Magazine("Science Weekly", "Science")
magazine2 = Magazine("Tech Review", "Technology")

# Add articles to authors and magazines
article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author2.add_article(magazine1, "Space Exploration")
article3 = author2.add_article(magazine2, "The Latest Gadgets")

# Test various methods
print(f"Author 1: {author1.get_name()}")
print("Articles written by Author 1:")
for article in author1.articles:
    print(f"- {article.title} in {article.magazine.name}")

print("\nMagazines contributed to by Author 2:")
for magazine in author2.magazines:
    print(f"- {magazine.name} ({magazine.category})")

print("\nMagazine contributors for 'Science Weekly':")
for contributor in magazine1.contributing_authors():
    print(f"- {contributor.get_name()}")

# Test Magazine class methods
print("\nTesting Magazine class methods:")
print("Magazine.find_by_name('Tech Review').name:", Magazine.find_by_name("Tech Review").name)
print("Magazine article titles for 'Science Weekly':", magazine1.article_titles())

# Test contributing_authors method
print("\nContributing authors for 'Science Weekly':")
for author in magazine1.contributing_authors():
    print(f"- {author.get_name()}")
