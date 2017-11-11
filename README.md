# Jieli's Machine Learning Reading List
Below is my reading list on a variety of topics of modern machine learning. Different from many reading list you may find available online, I have went through all of the listed materials myself and so am sure that you'll more or less benefit from it.

### General-Purpose Books
As a statistician, I favor machine leanring books from 
* [Elements of Statistical Learning, 2nd](http://web.stanford.edu/~hastie/ElemStatLearn/) **(ESL, Bible book of machine learning in statistics community, My favorite book)** - Book
* [An Introduction To Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) **(A more gentle version of ESL)** - Book

### Probability & Statistics

* [Statistical Inference, 2nd](https://www.amazon.com/Statistical-Inference-George-Casella/dp/0534243126) **(General introduction to prob & stat, Our textbook)** - Book
* [Computer Age Statistical Inference](https://web.stanford.edu/~hastie/CASI_files/PDF/casi.pdf) **(Textbook of statistical inference in modern era written by the two big names)** - Book
* [Bayesian Data Analysis, 3rd](https://www.amazon.com/Bayesian-Analysis-Chapman-Statistical-Science/dp/1439840954) **(Standard reference to Bayesian statistics)** - Book
* [ASA Statement on Statistical Significance and P-Values](http://amstat.tandfonline.com/doi/pdf/10.1080/00031305.2016.1154108?needAccess=true) **(Surprisingly, people outside (and even inside) statistics community are misinterepreting p-values, this is "official" guide on how to use it)** - Article

### Linear Models

* [Linear Model with R](http://www.utstat.toronto.edu/~brunner/books/LinearModelsWithR.pdf) **(Introductory book on linear regression with plenty of R examples)** - Book
* [Linear Statistical Models, 2nd](https://www.amazon.com/Linear-Statistical-Models-James-Stapleton/dp/0470231467) **(For those who want a formal mathematical treatment, Our textbook)** - Book

Below some papers on regularized regression which are thought as the main breakthroughs in stats in the recent 20 years
* [Regression Shrinkage and Selection via the Lasso](https://statweb.stanford.edu/~tibs/lasso/lasso.pdf) **()** - Article
* [Regularization and Variable Selection via the Elastic Net](https://web.stanford.edu/~hastie/Papers/B67.2%20(2005)%20301-320%20Zou%20&%20Hastie.pdf) - Article
* [Model Selection and Estimation in Regression with Grouped Variables](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.366.4278&rep=rep1&type=pdf) - Article
* [Exact Post-Selection Inference, with Application to the Lasso](https://arxiv.org/abs/1311.6238.pdf) - Article

### Bagging & Boosting
If I were asked to perform some prediction task in short time and without caring intepretation of the meaning of my model, boosting is my only choice. 
* [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/pdf/1603.02754.pdf) **()** - Article
* [Welcome to LightGBM’s documentation!](https://lightgbm.readthedocs.io/en/latest/) **(Another industry-level gradient boosting by Microsoft, claimed to )** - Website
* [Fighting Biases with Dynamic Boosting](https://arxiv.org/pdf/1706.09516.pdf) **()** - Article
* [Deep Forest: Towards An Alternative to Deep Neural Networks](https://arxiv.org/pdf/1702.08835.pdf) **()** - Article

### Stacking
The modern approach is to create an ensemble of a well-chosen collection of strong yet diverse models.
* [Stacked Regressions](http://statistics.berkeley.edu/sites/default/files/tech-reports/367.pdf) **(Original paper on stacking models)** - Article
* [Super Learner in Prediction](http://biostats.bepress.com/cgi/viewcontent.cgi?article=1226&context=ucbbiostat) **(Extend to general loss functions)** - Article

### Clustering
* [Survey of Clustering Algorithms](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.318.2219&rep=rep1&type=pdf) - Article
Besides the common clustering algorithms, the following two are pretty interesting 
* [On Spectral Clustering: Analysis and an Algorithm](http://ai.stanford.edu/~ang/papers/nips01-spectral.pdf) **(Spectral clustering)** - Article
* [Clustering by Passing Messages Between Data Points](http://www.psi.toronto.edu/affinitypropagation/FreyDueckScience07.pdf) **(Affinity propagation clustering)** - Article

### Reinforcement Leanring

* [Reinforcement Learning: An Introduction, 2nd](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf) - Book
* [UCL Course on Reinforcement Learning](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) - Website
* [CS 294: Deep Reinforcement Learning](http://rll.berkeley.edu/deeprlcourse/) - Website

### Deep-Learning
* [A Tutorial on Deep Learning Part 1: Nonlinear Classifiers and The Backpropagation Algorithm](http://ai.stanford.edu/~quocle/tutorial1.pdf) - Article
* [A Tutorial on Deep Learning Part 2: Autoencoders, Convolutional Neural Networks and Recurrent Neural Networks](http://ai.stanford.edu/~quocle/tutorial2.pdf) - Article
* [Deep Learning - An MIT Press book](http://www.deeplearningbook.org/) - Book
* [Mastering the game of Go with deep neural networks and tree search](https://gogameguru.com/i/2016/03/deepmind-mastering-go.pdf) - Article
* [Representation Learning: A Review and New Perspectives](https://arxiv.org/pdf/1206.5538.pdf) - Article
* [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shit](https://arxiv.org/pdf/1502.03167v3.pdf) - Article
* [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf) - Article
* [An Overview of Gradient Descent Optimization Algorithms](https://arxiv.org/pdf/1609.04747.pdf) - Article
* [Searching for Activation Functions](https://arxiv.org/pdf/1710.05941.pdf) - Article
* [ImageNet Classification with Deep Convolutional Neural Networks](https://www.nvidia.cn/content/tesla/pdf/machine-learning/imagenet-classification-with-deep-convolutional-nn.pdf) - Article
* [Generative Adversarial Nets](https://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf) - Article
* [Long Short-Term Memory](https://dl.acm.org/citation.cfm?id=1246450) - Article
* [Keras Documentation](https://keras.io/) - Website

### Natural Language Processing

### Python & R
I intentiionally don't include any advanced books, as the best way of learning is by practicing once you get yourself started
* [Python for Data Analysis, 2nd Edition](http://shop.oreilly.com/product/0636920050896.do) **(Written by the author of numpy)** - Book
* [An Introduction to R](https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf) **(Official R documentation, best quick tutorial)** - Article

### Big Data

#### Overview
* [Challenges of Big Data Analysis](https://arxiv.org/pdf/1308.1479.pdf) **(Review article written by Jianqing Fan)** - Article
#### Parallel Strategies
* [A Split-and-Conquer Approach for Analysis of Extraordinarily Large Data](http://www3.stat.sinica.edu.tw/sstest/oldpdf/A24n49.pdf) **(Parellelizing regularized GLM, written by my research group at Rutgers)** - Article
* [A Communication-Efficient Parallel Algorithm for Decision Tree](https://arxiv.org/pdf/1611.01276.pdf) **(Parellelizing tree building)** - Article
#### Hadoop & Spark
* [MapReduce: Simplified Data Processing on Large Clusters](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) **(Original research paper of MapReduce by Jeff Dean)** - Article
* [Spark: Cluster Computing with Working Sets](https://www.usenix.org/legacy/event/hotcloud10/tech/full_papers/Zaharia.pdf) **(Original research paper introducing the concept of Spark)** - Article
* [Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf) **(Original research paper introducing the concept of RDD)** - Article

### Miscellaneous Topics
* [A Few Useful Things to Know about Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) - Article
* [Model Order Selection: A Review of Information Criterion Rules](http://www.sal.ufl.edu/eel6935/2008/01311138_ModelOrderSelection_Stoica.pdf) **(A great review of various information criterions)** - Article
* [Do we Need Hundreds of Classifiers to Solve Real World Classification Problems?](http://jmlr.org/papers/volume15/delgado14a/delgado14a.pdf) **(The authors compared 179 classification models and claimed random forest the best )** - Article
