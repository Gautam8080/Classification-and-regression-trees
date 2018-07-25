# Classification-and-regression-trees with K-means
This program compares results of "Decision trees on dataset" vs "Decision trees on clusters of dataset formed by kmeans"

## Explaination behind Classification and Regression Trees (CART)
"Recursive partioning of training set to obtain subsets as pure as possible"
In a Decision tree, each node is related to a particular set of data

                                          Tree
                                         /    \
                                     T(left)  T(Right)
                           {t=T : t(A) <= x} {t=T : t(A) > x}
                           
Root node receives entire training set. Root node asks a question about one of features and (true or false) seperates the node into 2 branches. 
The question being asked at a nide can vary with features. In case of numbers, the seperation can be based on a threshold, otherwise, it can be a simple if-else statement. 
Let's take an example-

Given we have a dataset:

                                 Color   Diameter  Label
                                 Green      3      Apple
                                 Yellow     3      Apple
                                 Red        1      Grape
                                 Red        1      Grape
                                 Yellow     3      Lemon
                                 
The most important task of this algorithm is to decide which question to ask at which node based on its imporatance. 
Example of a decision tree in this case can be:

                                           Root Node --- Is Diameter >= 3
                                      (false)/     \(true)
                                            /       \
                                         Grape     Node (Green or Yellow?)
                                         (Leaf)    Asking if color yellow?
                                                  (false)/      \(true)
                                                        /        \
                                                     Apple    Apple/Lemon(50%)
                                                     (Leaf)       (Leaf)
                                                     
Impurity is our chance of being incorrect if we randomly assign a label to an example. Therefore if we have 5 kinds of labels(colors) that can be assigned to a fruit of specific color, then our impurity will be 0.8 or 80%. The best question is which reduces our uncertainity the most. 
Gini Impurity gives the amount of uncertainity at a node. Information gain notifies how much a question can reduce the Gini Impurity.

We represent a question by storing colomn number and value. Ex- Q(1,3) represents if D>=3. The question function returns true or false. In response to the question function, Partition(rows, question) devides the data into 2 subsets: 

1. rows for which question was true
2. rows for which question was false

