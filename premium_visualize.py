import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def visualize(read_file, write_img):

    read_file = csv.reader(open(read_file, "r"))
    read_file = list(read_file)

    pos = read_file[2][1]
    neu = read_file[2][3]
    neg = read_file[2][2]
    
    # need to fix y-values range problem and ordering of x-values
    data = {'Negative': neg, 'Positive': pos, 'Neutral': neu}
    names = list(data.keys())
    y_pos = np.arange(len(names))
    values = list(data.values())

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, names)
    plt.ylabel('Quantity')
    plt.title('Sentiments Visualization')
    plt.savefig('image/' + write_img)

    plt.show()

if __name__ == '__main__':
    print('Visualize full archive search tweets: ')
    visualize('search-data/computedResults.csv', 'full_archive.png')

    print('Visualize 30 day search tweets: ')
    visualize('search-data/computedResults30days.csv', '30_day.png')