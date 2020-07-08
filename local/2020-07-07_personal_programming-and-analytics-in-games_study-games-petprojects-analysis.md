I have always been a keen video game player. Since moving to a new country, and especially during COVID times, video games have become a choice way to spend free time. I enjoy complex games with a lot of opportunity to analyse and optimise - no great surprise that I made a career of these skills! 

https://github.com/bluemania/wow_auctions

Recently I started playing World of Warcraft: Classic (WoW) upon it's release late 2019. It is a highly social game where players group to fight monsters and loot gold and items.

##### I wondered - could I ethically use my programming skills to get more gold?

In WoW, gold is like money. It can be used to purchase skills, mounts and even items from other players. To facilitate exchange, there is a centralised Auction House (AH). From there players can list their items for bid/buy, and use the AH to purchase items they need. In many ways, the AH is comparable with a 'stock market', with the lowest priced items (usually) being preferred which sets the 'market price'.

##### Identifying a market

At any time there could be tens of thousands of auctions underway. I figured I would need to focus on a smaller, hopefully more profitable area of the economy.

I narrowed this down to the Potions and Elixirs market. This can be considered a 'secondary' market, because potions need to be brewed by players from raw materials (herbs). So rather than buying and selling the same items, I would aim to buy raw ingredients and sell brewed potions. Because potions almost always come into existance from player creating them, there could be natural supply bottlenecks which I could take advantage.

Buy herbs when there is high supply and sell potions when there is high demand.

##### A simple policy

There are some simple buying and selling policies which can help players make money. The basic concept of 'buy low sell high' tends to work well, but requires players to identify when prices are non-average. Cost plus pricing is not bad either, take the raw costs of materials add some profit, and sell only if a profit is achivable.

##### An automated policy

What would be more ideal is to have a system which could make policy decisions for us. It could determine:

* How many herbs are available?
* How many herbs I need?
* How much do the herbs cost?

And use this information to set a herb buying policy.

On the flipside we would want a potion selling policy. This would make some similar determinations such as:

* How many competing potions are available?
* How much do competitor potions cost?
* How many potions do I have for sale?
* What is the minimum I would be prepared to sell a potion for?

### Staying within the games rules and limits

We are bound by the game's terms of service for what we can and cannot do as part of this system. For instance, we can not automate any mouse or keystrokes. 

WoW has an addons system for allowing users to customise their game experience. These include in-game auction tools that can collect data and allow users to set prices. These addons can only load information into the game at character login, and write information at character logout (or reload).

Our aim is to modify the addon files after character logout, so we can read information about
* Character inventory - Number of potions, herbs, gold and other items
* Auctions available - Items, prices, quantities, time remaining, and owner
* Auction history - Successful and unsuccessful auctions, previous purchases

### Approach

The overall aim is to increase profits given constraints of:
* potion actual sale price
* herb actual buy price
* sale volume
* herb market
* time taken
* current inventory
* personal demand
* fail rate
* actions per day
* available capital
* inventory space

We use the following approach for buying and selling

For each potion:

* Calculate the minimum_sell_price based on
    * Ingredient market price
    * Auction fail rate / deposit amount
    * Minimum profit buffer (the plus in cost plus pricing)
    * The AH cut
* Check how many potions are available in our inventory, for splitting into sales of stacks of 5 or stacks of 1.
* If market_price is less than minimum_sell_price, then do not sell
* Else if market_price is higher than minimum_sell_price, and the lowest priced item is not one of my existing auctions, then undercut the current market price

This gives us a mapping of potions: price. We use the auctioneer addon to fill in the prices (with an invalid price for no-sale) and use batch-post. This is much faster than having to manually review the current prices, judging if they will make profit, and entering quantities and prices.

For each herb:

* Determine inventory of potions and herbs
* Given a user specified maximum number per potion - calculate herbs required to reach maximum
* Scan AH for available herbs and prices
* Set a maximum price to pay per herb, based on historic market price
* Rank order the herbs by lowest price, setting the maximum buying price to the quantity of herbs that fill the order

This gives us a mapping of herbs: prices. From there we can use the 'Snatch' addon to lookup items at that price and less, and simply buy all auctions. This saves considerable time over having to manually think about how many items, costs etc.

### Market price and profit

To make a profit, we need to have an understanding if current market prices are over or undervalued versus a longer term trend.

To calculate market prices, we originally used auction history, as well as buying and selling. We have recently moved to using an external source of auction prices, as it collects far more data and provides an unbiased source of prices.

### Next steps

Next aims with the project link in with my other professional article. I'm looking to increase my expertise with software development practices using this project as a sandbox.
