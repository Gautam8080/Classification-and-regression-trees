# Interative Decision Tree
## Classification-and-regression-trees
Classification and Regression Trees are ideally suited for analysis into complex ecological data (De'ath, 2000). Classification and Regression Trees are fairly traditional in data analysis, yet they remain to be one of the most effective ones in giving insights into the data. While neural networks have surpassed most machine learning techniques in performance, their decision process is complex and visualizing how they reach the predictions in entirety remains a challenge. Decision Trees, on the other hand, work on recursive partitioning of training set to obtain subsets as pure as possible. Each node in the tree represents a particular set of data that shrinks as the data trickles into the lower branches. That makes Decision Trees easy to peek into and understand why the classifier made a choice at certain nodes to reach the output. 

## Conceptual Understanding of Classification and Regression Trees (CART)
"Recursive partioning of training set to obtain subsets as pure as possible"
In a Decision tree, each node is related to a particular set of data

                                          Tree
                                         /    \
                                     T(left)  T(Right)
                           {t=T : t(A) <= x} {t=T : t(A) > x}
                           
Root node receives entire training set. Root node asks a question about one of features and (true or false) seperates the node into 2 branches. 
The question being asked at a node can vary with features. In case of numbers, the seperation can be based on a threshold, otherwise, it can be a simple if-else statement. 
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

We represent a question by storing colomn number and value. Ex- Q(1,3) represents if D>=3. The question function returns true or false. In response to the question function, Partition(rows, question) devides the data into 2 subsets by checking each row in that node: 

1. rows for which question was true
2. rows for which question was false

While building the tree, we recursively partition the data on every node based on right question unless our information gain turns to be zero in that case, we do not have further questions and the node becomes a leaf.

In simple language, we begin by calculating uncertainity of our starting set. Then for each possible question we can ask at that node, we try partitioning the data and calculate the uncertainityat true and false node (child nodes). We take weighed average of their uncertainity which can be passed to info gain function. This process is repeated for every possible question and best question is stored with highest info gain. We follow recursion on true and false branches and repeat until no more partition is possible. This node is called Leaf.

### Explaination of K-means is attached as a .docx file. 

### K-Fold Cross Validation
Also we are performing 10-Fold Cross Validation on the data in the program. It is basically breaking the data into 10 folds and using 1 fold as test data while remaining 9 folds as training data. We perform this with every fold.That is why we are getting 10 different accuracies in the result after we execute the program. Average of all accuracies will be net accuracy of model.

## Proposed Research I
The concept of CART is simple to understand and arguably should be ideal for optimum performance. However, in realistic scenarios the unsupervised approach sometimes reduces the functionalities in terms of what user expects. For instance, to access the performance of players in different combined sports, a user may want to first split the data based on the sport or team.
This study proposes a supervised controlled approach to CART algorithm that would let the user decide or alter the question at certain nodes. The proposed research intends to achieve its designated functions through an Interactive GUI that will dictate a live feature selection at each node. The user will be given choices of features in order of most to least information gain, something the user can overrule the algorithm. Once the appropriate questions have been introduced to the model at intended nodes, user can let the model proceed in its original form to complete the tree.

## Proposed Research II
In the Program, the data is first stored in a variable. Also the data is fed to K-means module that returns 3 clusters of data. Now we apply the decision tree on (whole dataset) vs (3 clusters indivisually) to yeild the result. 
