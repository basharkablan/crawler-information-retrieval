# crawler-information-retrieval

This repository will include an IMDB crawler which is made as a homework.

The script crawler.py would start from a specified actor and saves its movies into an xlsx file,
then it crawls to every movie and do the same for its actors.

The output file is an Excel 2010 file, since we use openpyxl library, which includes 3 sheets:
1- Movies of Actors (only ids are shown).
2- List of Movies we've scanned (Name + id + Rating).
3- List of Actors we've scanned (Name + Movies count).