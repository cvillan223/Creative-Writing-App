import webScrape as ws
import csv
import pandas as pd
import random

if __name__ == '__main__':
    nouns = ws.getNouns()
    verbs = ws.getVerbs()
    povs = ws.getPOV()
    genres = ws.getGenres()
    themes = ws.getTheme()


    wordcount = []

    # Word count for each activity, constrained by verb list
    for i in range(0, len(verbs)):
        wordcount.append(ws.getWordCount())

    # Should write a short story 2 times a week at most, allow for every 3rd week to be a revision of
    # 2 random stories

    # 52 weeks per year, 104 stories in total, every 3rd week is a revision week

    # Csv file should be filled as noun, verb, genre, wordcount
    headers = ['Subject1', 'Action', 'Subject2', 'Genre(s)', 'Theme/Literary Device', 'POV', 'Time Period', 'Wordcount']
    with open('CreativeWriting.csv', 'w') as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        i = 0
        while i < 104:
            noun = "A/At/An " + nouns[random.randint(0, len(nouns.columns) - 1)][random.randint(0, len(nouns) - 1)]
            verb = verbs[random.randint(0, len(verbs) - 1)] + '(s)'
            noun2 = "A/At/An " + nouns[random.randint(0, len(nouns.columns) - 1)][random.randint(0, len(nouns) - 1)]
            count = wordcount[random.randint(0, len(wordcount) - 1)]
            pov = povs[random.randint(0, len(povs) - 1)]
            theme = themes[random.randint(0, len(themes) - 1)]
            timePeriod = ws.getTimePeriod()

            flip = random.randint(0, 1)
            genre = genres[flip][random.randint(0, 28)]

            # Randomly decide if a different genre should be included
            extraGenre = random.randint(0, 1)
            if extraGenre == 1:
                flip = random.randint(0, 1)
                xtreGenre = genres[flip][random.randint(0, 28)]
                genre = genre + " / " + xtreGenre

            data = [noun, verb, noun2, genre, theme, pov, timePeriod, count]
            if i % 3 == 0 and i != 0 and i != 3 or i == 2:
                writer.writerow(["REVISION WEEK"])
            else:
                writer.writerow(data)
            i += 1

