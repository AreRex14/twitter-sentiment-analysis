import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def visualize(read_file, write_img):

    read_file = csv.reader(open(read_file, "r"))
    read_file = list(read_file)

    pos = read_file[2][1]
    neu = read_file[2][3]
    neg = read_file[2][2]
    
    # need to fix y-tick value range problem
    #pos = 20
    #neu = 15
    #neg = 5
    data = {'Negative': neg, 'Neutral': neu, 'Positive': pos, }
    names = list(data.keys())
    values = list(data.values())
    x_pos = np.arange(len(names))
    width = 0.8
    plt.bar(names, values, align='center', alpha=1, color='b')
    plt.xticks(x_pos, names)
    plt.xlabel('Type', fontsize=10, fontweight='bold')
    plt.ylabel('Quantity', fontsize=10, fontweight='bold')
    plt.title('Sentiments Visualization', fontsize=10, fontweight='bold')
    plt.savefig('static/' + write_img)
    plt.show()

if __name__ == '__main__':

    print("This python script will visualize tweets based on sentiment type.")
    # need to handle other user io operations(file not existed, or not extensions and else...)
    confirmation = input("Executing this script will overwrite existing data in file if the operation has been done before, proceed with caution. y/n: ")
    if confirmation == 'y':
        read_file = input("Please input a csv file to read tweets from: ")

        visualize('search-data/'+read_file, read_file+'.png')
    else:
        print("You said no. Thank you")
