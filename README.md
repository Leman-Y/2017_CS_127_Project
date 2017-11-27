# Project - Jason Chen and Leman Yan
# Project Description:
# 
# Choice 1:
# 
*** Have a web app that can display a table of any csv file uplaoded and then have a search box for certain words, names, phrases, or numbers from within parts of the sections of the tables/csv and replace the exisiting table into the new sorted/shortened table.
# 
# Choice 2:
# 
*** Have a text be broken down into n-gramed phrases, and sort them into catagories/genres based on the phrases. ie - religous, romance, etc.

*** Extended requirements
Here are some ways you should extend the project. You don't have to do
all of them and if you have other ideas, speak to the instructor about them.
- Look at most common words after removing words in a stop word list
  (http://www.lextek.com/manuals/onix/stopwords1.html).
- Add a stemming library and use that in your word searches.
- Look up a simple stemming algorithm and implement it.
- Put it up as a web app (Flask) - for example use a form to input a
  query to the data set.
- Use a graph library to visualize some of your explorations
- Store (and use) additional info in the inverted index such as:
  - how many times each word occurs (use a tuple)
  - The position of the word (where it starts)
  - Storing the stemmed word instead of all the words
- Experiment with n-grams for the inverted index

*** Alternate project 
You may propose an alternate project to the one specified here but
make sure that you have the instructors approval prior to
starting. Any proposed alternate project must make use of the same set
of tools and techniques as the inverted index project does.
