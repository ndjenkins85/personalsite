While performing some github repository cleaning in May 2020, I found a collection of blogs from my first blog site which I didn't stick with. This article further explores ML classification of text data.

## Automatic coding of respondent feedback

It has been at least a month since 'the project' that had occupied many late nights. It appears that my subconscious has been secretly working on the answer to the last lingering question I had when the project was finished.

"Can we teach a computer to code respondent feedback automatically?"

So on the way to picking up a morning coffee, I started to think through the logical steps needed. It worked! It can be done!

So what was the project and what was the method?

A large global client runs an employee satisfaction survey across many countries and languages. They wanted to know what their staff are saying and what areas to improve in. The primary method used was an NPS style question and open verbatim feedback. Typically the main way to quantify the issues staff have, are to manually review verbatim responses and allocate to a theme (aka code frame). The specific challenge for this project was that of the 50,000 open responses, a subset of only n=4,000 were manually coded. If the n=4,000 were selected randomly and coded, usually that is perfectly sufficient to make assumptions about the total population. For this project however, the client wanted basically ALL responses coded! Enter Machine Learning.

The problem boiled down to n=4,000 verbatims were coded into ~80 different code frames. We needed to take the learnings from the manual process and train the computer to apply the rules to the uncoded responses.

Simple exploratory analysis was conducted, using bag-of-words and simple CHAID/Tree and random forest. Main reason was to get a quick 'benchmark' and get an idea of how we would implement the solution.

First step was to compact the number of code frames into 27 code frames. This was done manually but in retrospect could have been better handled or complemented by an analytical solution (which would aim to group code frames by similarity).

Next step was to convert all verbatim feedback into a 300 dimension vector object using some of Googles latest technology; word2vec. This method has many advantages over typical bag-of-words methods in that it can group words that have similar meaning. The results are at times, fantastic. We saw the method assign similar values for 'good', 'great', 'gud*', 'awesome' (*yes that IS a misspelling!).

Sample was prepared into typical training, validation and test samples, and 27 models were created (using random forest) that learnt how the vectors related to each of the coded responses. The coded responses were multiple select which required the use of several models. On reflection and later learning there are better modelling techniques to more gracefully handle multiple response type models.

We then spent considerable time looking at the outputs, which were 27 columns of probabilities, indicating how likely a response was to belong to a given code frame.

The team met to discuss what the eventual output would look like to the client. I provided reports on accuracy of the model, as well as precision. The decision was made that if we were to show 'automatic coding' to the client, we would not be comfortable showing more than 1 incorrectly coded response for every 4 correctly coded responses.

This became a usability mandate of 80% precision, with as high an accuracy as possible.

It turned out that by combining the results of the 27 different models led to MUCH better results. Simple rules were used to determine, from the 0-1 probability, if a response belonged in a given code frame. Certain codes needed to be treated a special way, either because their models were not as strong or they were an 'other' category.

Rules were something like, 
if x>0.6, True
else if x>0.3 AND max(all_other_x)<0.3, True

This helped the final model to determine final codings based not just on it's own confidence, but on other model's LACK of confidence.

I am sure there is a better way to manage the combining process as well, and if we had more time on the project it would have been the next priority.

The final way the probabilities were used was in two ways;
*To show the % of respondents who said a given code frame, take the AVERAGE of all responses. The 0-1 probabilities effectively become a weight, and were very similar to the training %'s.
*Show a verbatim response to the client if the rules were met for any given code frame.

The above was all received well, and I learnt some very valuable lessons in creating such an analytical solution.

The last remaining question I had for myself after leaving the project was, what if we could have done away with the n=4,000 coded responses and trained a computer to create the code frames?

So here I am this morning creating tests and writing up results. It seems to work!

So far I have tried the following steps;

* Create 300 dimension vector space for all verbatim feedback
* Run the array through a k-means clustering solution with k=15 clusters
* Attach the k-label back to the verbatim response
* Analyse the size of the clusters
* Review a random selection of 10 verbatim responses

Appears to work quite well. 

There is more improvement that can be done, specifically I would want to try finding 5 of the most 'stereotypical' verbatim responses for a given cluster. 

This might include 2 of the 'most central', and 3 from some distance away from the center (to get a slightly broader sense of the space). 

If we stuck with the pure center we might end up with results such as 'Good service', 'Good Service', 'Good service'; which isn't bad but not very descriptive of the space either.

The application of such as tool in Market Research would be simply incredible. For companies with long-term relationships and lots of client 'universe' data, this is potentially a gold mine.

Sources of information for my reference:

* http://stackoverflow.com/questions/20976722/k-means-initial-centers-determine-the-result
* http://www.slideshare.net/SarahGuido/kmeans-clustering-with-scikitlearn
* http://stackoverflow.com/questions/29799053/how-to-print-result-of-clustering-in-sklearn