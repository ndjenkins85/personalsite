As I work through development upgrades for the wow_auctions repository, I thought it would be a good idea to quickly reflect on the development status. This will discuss the shape of the project after the first sprint of development, the initial upgrade stage, and plans for the future.

## The first version

Ultimately the first version was a success - the program was completed and it helped me to make more gold from my auctions. The following graph shows gains over time. The blue line is gold on my auction characters, orange line represents inventory on auction characters and the black line is gold + inventory on all characters.

There are a few distinct phases of the project which are reflected in the graph

![Holdings](https://www.nickjenkins.com.au/static/assets/wow_auctions/holdings.jpg "holdings.jpg")

##### Mid-April MVP

Mid-April was when the first MVP version of the program came online. One of the first challenges was to maintain a record of gold, inventory, inventory value, across characters, over time. The mere ability to record and plot this was a major milestone for the project, as it became a way to objectively measure gold making improvements over time. 

##### Mid-April - Mid-May execution

Overall, this is the phase where the program really showed itself to be valuable. Early in the period is where I created the concept of an alternative 'market price' which could tell me if current prices were over/under valued versus a longer trend. I also created the basic sell policy rules.

Further into the month I also created the first version of the buying policy, which allowed for a steady stream of herb buying and potion sales. I also started some optimization work; analyzing and reducing the program runtime.

This period represents an increase in holdings of 2,500g - not bad!

##### Mid-May to Mid-June

During this phase I was more focused on a work project, and did not continue to execute. This is why we see a long tracked line; there was virtually no usage of the program during this time.

What we do see is that I moved a lot of gold into inventory. The thinking was that inflation may eat up the value of the gold, so it was better put into items.

##### Mid-June to Late-June

As work projects began to finish up, and noticing that my in-game gold reserves were getting desperately low, I resumed executing on the project. The early periods here I spend a lot of gold on characters for other things, and shuffled holdings more towards gold, herbs and potions.

## Recent developments

The past two weeks are more reflective of the initial Mid-April to Mid-May period, where the engine is doing a lot of work. This is also where I've began to think about performance improvements and software development practices. 

On the performance improvement side, I was not satisfied with the herb buying policy as I found it too conservative which limited supply. I realized that by basing market price on my auction history, I was unintentionally biasing the market price towards my own actions as opposed to a more real price. 

I considered changing the program to define market price as auctions that existed in one snapshot, but not the next (if they were not due to expire). Alternatively, I decided it was easier and robust to use more general data from ['Booty Bay Gazette'](https://www.bootybaygazette.com/) on auction values. To absorb the information in an API-like form, I needed to experiment with creating WoW addons with lua, so that I could scrape the BBG information in-game, and save it to my own addon file so that the auction program could read this market price information. I created a ['wow_addon github'](https://github.com/bluemania/wow_addon) specifically for this sub-project.  

## On to improving software development expertise

Now within the past few days, with a working project, I'm turning my attention more to improving the software architecture, documentation and thought process (this!), and best practices.

While I am waiting to be onboarded onto my next work project, I'm looking to improve the project with a couple of quick wins:

- [X] Move from jupyter notebook to CLI using argparse
- [X] Clean up git repo to remove data saves
- [X] Basic dependency management using virtualenv
- [X] Documentation updates

In my other post I discussed some tools and methods to increase my software development expertise -  https://www.nickjenkins.com.au/articles/professional/2020/07/07/increasing-software-development-expertise

I spent some time over past few days looking to implement CLI + Packaging + Dependency management; ideally this would use Click + setuptools + Poetry, but I am not quite understanding how these will fit together at this stage. I thought it would be best to implement CLI and dependency management that I am familiar with, and move on to other topics.

Today I'm looking to (finally) learn good logging habits, then I might work on cleaning up the script configurations.

