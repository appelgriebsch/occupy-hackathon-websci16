from os import path
import numpy as np
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt


def aggregatebyweek(data):
    data_good_resp = data.loc[data['resp'] == 200]
    #aggr = data_good_resp.groupby(['year', 'week', 'ip'])
    # print pd=.DataFrame(aggr).reset_index()
    # data_good_resp[['year', 'week', 'ip']].groupby(['year', 'week']).count()
    # data.loc[(data['resp'] == 200) & (data['week'] == 51) & (data['year'] == '(2011')]['ip'].count()


    data_good_resp['year'] = data_good_resp['year'].map(lambda x: x[1:])

    groups = data_good_resp[['year', 'week', 'title']].groupby(['year', 'week'])

    aggr_data = data_good_resp[['year', 'week', 'title', 'ip']].groupby(['year', 'week']).agg(
        {'title': concattitles, 'ip': np.size}).reset_index()

    print pd.DataFrame(aggr_data)
    for row in aggr_data[['year', 'week', 'title']].itertuples():
#        print(str(int(row[1])) + '_' + str(int(row[2])) + '.png')
        createwc(row[3], str(int(row[1])) + "_" + str(int(row[2])) + ".png")

def concattitles(titles):
       fulltitle = " ".join(titles)
       return fulltitle

def createwc(text, filename):
    wordcloud = WordCloud().generate(text)

    # take relative word frequencies into account, lower max_font_size
    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    #plt.show()
    plt.savefig(filename)

def main(filename):
    data = pd.read_csv(filename, error_bad_lines=False)

    data.columns = ['year', 'week', 'ts', 'resp', 'url', 'ip', 'title']

    aggregatebyweek(data)

if __name__ == '__main__':
    filename = "5percentsample.txt"
    main(filename)