While performing some github repository cleaning in May 2020, I found a collection of blogs from my first blog site which I didn't stick with. This article explores ML classification of text data.

## Automatic coding, prototype planning

‘Thor’ (a collegue) really took to my presentation at ‘show and tell’ and before long he pulled me over to help him with a proposal.

Thor manages several customer satisfaction surveys for a large client. There is one particular question that is asked in all surveys which is liklihood to recommend. This is used as an NPS score. Further to this, respondents are asked why they rated the way they did.

Enter automatic coding of respondent feedback.

Thor pointed out that with over 120,000 verbatim comments currently, and an additional 5k per month (which are currently coded at random), there could be a lot more usefulness come out of the data.

The verbatim responses are complicated however, and there is not the opportunity to do a completely unsupervised approach, as the code frames have been decided.

The client and Thor have decided on 30 code frames, with a positive and negative spin; so 60 seperate code frames.

In the previous text analytics task, up to 5,000 responses were already coded, which were used to create a predictive model of a verbatim belonging to a class. In this instance there are less than 300 already coded.

Adding to the difficulties is the requirement for multiclass coding. Three difficult challenges.

So this project differs to the one i presented in the following ways;

* Multiple class coding needed
* Positive/Negative comments (Sentiment analysis)
* Predefined code frames

There are many areas I need to learn about to better tackle the problem, but the method I have proposed is as follows;

Firstly I need to create a baseline case. In order to fit a number of segments into the preexisting groupings, I am proposing to create n=100 segments, and attempt to code into only 30 (non-sentimental) segments.

I will do this by reading 10 or so codes randomly to judge what the segment is about and code accordingly.

I believe the approach will really start to shine when two further improvements are made; first off, introducing multiple class coding, secondly, by creating some tools to aid the manual coding process.

To create multiple class coding, we will split the sentences by punctuation, ‘and’, etc. At this point I will need to research a suggested list or method of splitting the sentences. My hope is that many part-sentences will be segmented into very uninteresting (but homogenous) segments. I have ideas how to piece the information back together which I will express shortly.

The process of identifying a cluster is currently onerous. We need metrics that help to express what the cluster is about. Ideas include;

* Segment size
* Inertia
* Set of most central sentences
* Set of random sentences
* Most numerous words used in cluster
* Neighbouring clusters
* Markov chain sentence generator (Not for this project, but eventually!)

The metrics will be very useful in quickly adding qualitative labels against predicted clusters. Moreover, it will mean we can radically increase the number of clusters to n=300, and, clusters with poor inertia we can attempt to recluster.

With a high number of clusters, I anticipate many sentences and part sentences will fall into clusters that are unrelated to the end goal 30 code frames. This is just as useful as codes which we know are closely related.

When we break sentences into partials, we can allow a single sentence to belong to many clusters. If many of those sentences are just noise, that’s OK, as long as we end up with at least one related codeframe per verbatim. Sometimes that will mean a verbatim will fall into an ‘other category’ if there are no other suitable codes.

Another method to try here would be some kind of skip-gram style breaking of sentences. This would mean a sentence with a natural break, like this one, would be analysed six ways total. Firstly as a whole, secondly as individual sentence parts, thirdly as two-sentence parts.

Sentiment analysis will have to come later into the piece. It will be very useful to utilise the advocacy score itself to help drive ‘positive vs negative’, or in some combination with text. There is some difficulty however, because a respondent might have rated a 7, and when answering why they rated they way, are say ‘because of value for money’. Is that a positive or a negative sentence? There could be merit to having a negative/neutral/positive sentiment attached. This would be an area to explore after the benchmark, tools, and multiple coding analysis.

The clustering algorithm used could be improved greatly as well, but this will likely not be explored this side of the proposal.

Kmeans appears to break down on my laptop and the office ‘beast’ as of 25k cases. MinibatchKmeans could be the way to go, or could potentially use amazon services and Apache Spark to create a distributed clustering. The problem isnt so much with the raw data size (100-200mb) but the memory requirements to cluster.

![Machine learning map](http://1.bp.blogspot.com/-ME24ePzpzIM/UQLWTwurfXI/AAAAAAAAANw/W3EETIroA80/s1600/drop_shadows_background.png "Machine learning map")

If we went down the distributed pathway, we may one day look into hierachical clustering. It is not currently implemented in spark, http://spark.apache.org/docs/latest/mllib-clustering.html but the following paper seems to suggest some promise. http://users.eecs.northwestern.edu/~cji970/pub/cjinBigDataService2015.pdf

Cosine similarity for vector space (useful for neighbour clusters perhaps) http://blog.christianperone.com/?p=2497

Evaluation; https://en.wikipedia.org/wiki/Cluster_analysis#External_evaluation

Also, a distracting and engaging piece on real world data science: https://www.linkedin.com/pulse/data-science-taught-universities-here-why-maciej-wasiak?trk=hp-feed-article-title-share
