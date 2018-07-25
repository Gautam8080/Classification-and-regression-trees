
#k means
import numpy as np
import matplotlib.pyplot as plt
import copy
import pandas as pd


def dataset(filename):
    data = (pd.read_csv(filename, delimiter=",", na_values=[" "], usecols = (1,4,10,11)))
    #feature scaling of categorizical data to numeric for k means
    data.loc[(data.Sex.isin(['male'])), 'Sex'] = int(1)
    data.loc[(data.Sex.isin(['female'])), 'Sex'] = int(0)

    data.loc[(data.Embarked.isin(['S'])), 'Embarked'] = 0
    data.loc[(data.Embarked.isin(['C'])), 'Embarked'] = 1
    data.loc[(data.Embarked.isin(['Q'])), 'Embarked'] = 2

    
    data_points = np.array(data.dropna())  

    header = pd.read_csv(filename, delimiter=",", header = None, usecols = (1,4,10,11))
    header = np.array(header)[0].tolist()
    return [data_points, header]

def compute_euclidean_distance(point, centroid):
    return pd.to_numeric(np.sqrt(np.sum((point - centroid)**2)))


def assign_label_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)
    return [index_of_minimum, data_point]


def compute_new_centroids(cluster_label, centroid):
    return np.array(cluster_label + centroid)/2

def iterate_k_means(data_points, centroids, total_iteration):
    label = []
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)
    
    for iteration in range(0, total_iteration):
        for index_point in range(0, total_points):
            distance = {}
            for index_centroid in range(0, k):
                distance[index_centroid] = compute_euclidean_distance(data_points[index_point], centroids[index_centroid])
            label = assign_label_cluster(distance, data_points[index_point], centroids)
            #here label has [index of centroid which is minimum distant, datapoint]
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])
            
            if iteration == (total_iteration - 1):
                cluster_label.append(label)
    return [cluster_label, centroids]


def print_label_data(result):
    #result is [cluster label [(centroid label, that data point)], new_centroids]
    print("Result of k-Means Clustering: \n")
    for data in result[0]: #data means cluster label
        print("data point: {}".format(data[1])) 
        print("cluster number: {} \n".format(data[0])) #cluster number mean the centroid number
    print("Last centroids position: \n {}".format(result[1]))


def create_centroids(dataset):
    k = 3
    rows, colomns = dataset.shape
    centroids = dataset[np.random.randint(0, rows, k)]
    return np.array(centroids)

def working(filename):
    data_points, header = dataset(filename)
    centroids = create_centroids(data_points)
    store_initial = copy.deepcopy(centroids)
    total_iteration = 100

    [cluster_label, new_centroids] = iterate_k_means(data_points, centroids, total_iteration)
   #cluster_label is 2 dimensional list with (centroid_label, data point associated) at each index
    #iterate_k_means(data_points, centroids, total_iteration)
    #print_label_data([cluster_label, new_centroids])
    print()

    datasetzero = []
    datasetone = []
    datasettwo = []
    for i, g in cluster_label:
        if (i == 0):
            datasetzero.append(g)
        elif (i == 2):
            datasettwo.append(g)
        else:
            datasetone.append(g)
    #print(len(datasetzero), len(datasetone), len(datasettwo))

    #plt.scatter(np.array(datasetzero)[:, 0], np.array(datasetzero)[:, 1], c='g', marker = 'x')
    #plt.scatter(np.array(datasetone)[:, 0], np.array(datasetone)[:, 1], c='c', marker = 'x')
    #plt.scatter(np.array(datasettwo)[:, 0], np.array(datasettwo)[:, 1], c='r', marker = 'x')

    #plt.scatter(new_centroids[:, 0], new_centroids[:, 1], c=(1,1,1))
    #plt.scatter(store_initial[:, 0], store_initial[:, 1], c=(4,4,4))
    #plt.show()
    #Since we are using multiple features, graph wouldn't give visual results due to multidimensional space
    i = 0
    for i in range(len(datasetzero)):
        datasetzero[i] = datasetzero[i].tolist()
    i = 0
    for i in range(len(datasetone)):
        datasetone[i] = datasetone[i].tolist()
    i = 0
    for i in range(len(datasettwo)):
        datasettwo[i] = datasettwo[i].tolist()

    datasetzero = np.array(datasetzero)    
    datasetone = np.array(datasetone)
    datasettwo = np.array(datasettwo)    

    return [datasetzero, datasetone, datasettwo]

#cl1, cl2, cl3=working("titanic dataset.csv")
#working("titanic dataset.csv")


