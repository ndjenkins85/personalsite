While performing some github repository cleaning in May 2020, I found a collection of blogs from my first blog site which I didn't stick with. This article is a reflection on taking a big data with apache spark course.

# First post - A for Apache Spark.

10 minutes ago I opened a bottle of wine to celebrate finishing the edX course "BerkeleyX: CS100.1x Introduction to Big Data with Apache Spark".

I wanted to write up my reflections on the course; why I took it, and what I learnt from it.

On the path to improving my data analysis abilities, I undertook the task of learning Python. While my abilities have improved a great deal in the past few months, I was hesitant in enrolling in a course where an 'intermediate' knowledge was required. I would say the python requirements were not too onerous. They were just challenging enough.

#### If you have an understanding of the following, then you are well prepared to take the course.

* Making and using functions
* List comprehension (lots of x[0][1] usage!)
* Lambda functions
* ipython

### An example which uses many elements of Spark using Python

``` python

    myValuesRDD = sc.parallelize(listOfMyNewValues)

    # Merge RDDs. Can also use join in some instances.
    allRDD = existingRDD.union(myValuesRDD)

    # Change the way tuples are displayed in the data
    mappedRDD = allRDD.map(lambda x: (x,1))
    >[(oi,1),(tudo,1),(sim,1),(oi,1),(oi,1),(tudo,1).....]

    # The above have effectively created a key/value partnership. This is great for 'reduceByKey'.
    reducedRDD = mappedRDD.reduceByKey(lambda a,b: a+b)
    >[(oi,3),(tudo,2),(sim,1).....]

    # Actions will cause calculations to happen
    reducedRDD.count()
    >3....

    reducedRDD.collect()
    >[(oi,3),(tudo,2),(sim,1).....]

    reducedRDD.take(2)
    >[(oi,3),(tudo,2)]

    # Sometimes you have to sort in strange ways due to the key/value relationship. While there may be better ways (and better examples), using two map commands can do the job.
    reducedRDD.map(lambda x: (x[1],x[0]).sortByKey(True).map(lambda x: (x[1],x[0]).collect()
    >[(sim,1),(tudo,2),(oi,3).....]

    # filters are also widely used
    .filter(lambda x: True if x[1]>2 else False).collect()
    >[(oi,3).....]

```

### The course was great for exposure to

* Analysis of distributed data sets.
* regex in text analysis
* groupByKey and reduceByKey, functions often used in SQL and Pandas dataframes.
* Machine learning using Spark, specifically collaborative filtering.

### Hints and tips for the course:

* ipython is a fantastic environment for testing your variables, make liberal use of .take(5) to always assess what your coding is producing before introducing it to the final piece.
* Although the lessons indicate reduceByKey() is superior to groupByKey(), the latter DOES come in handy at times during the course, so do not ignore it.
* Understanding the action functions outside of (lambda a,b: a+b) was essential. As my tutor Brendan put it, 'a' is the total, 'b' is what we want to add or times it by as all the elements are actioned. This makes statements like (lambda a,b: a+(1/b)) possible.

### Where to from here?
I finished the course with an A and what I feel that translates to is exposure and basic understanding of the concepts.
To really become expert in this area, I would need to work with distributed data sets professionally alongside other experts.
The introduction to regex and groupByKey will be invaluable and something I will build on in the next year as I get more exposure to SQL and NLP.

Top 10 movies I would apparently watch!

* (4.789309907107899, u'Inherit the Wind (1960)', 133)
* (4.723802072380128, u"Schindler's List (1993)", 1171)
* (4.688131459723218, u'Wizard of Oz, The (1939)', 817)
* (4.684335819305319, u"It's a Wonderful Life (1946)", 343)
* (4.671417508626954, u'Raiders of the Lost Ark (1981)', 1195)
* (4.62317400088355, u'My Fair Lady (1964)', 314)
* (4.61502880874494, u'To Kill a Mockingbird (1962)', 451)
* (4.598726124937215, u'12 Angry Men (1957)', 314)
* (4.593908346057006, u'Star Wars: Episode IV - A New Hope (1977)', 1447)
* (4.578087346384571, u'Sting, The (1973)', 496)

### Other related resources
Paper on collaborative filtering using regression based approach.
http://www.dabi.temple.edu/~zoran/papers/vucetic_kais05.pdf

So for now - vagrant halt
