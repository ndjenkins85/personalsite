Understanding of product analytics, metrics and A/B tests is a critical skill for data science consultants. While I have had some experience with these through [former projects](http://www.ndjenkins.com/articles/professional/2022/01/09/project-experience-and-impact), it is a skill I am actively researching and studying to prepare for future engagements.
The following article provides an overview of these three areas.

#### This article is summarized by a one-page reference document which can be [found here](/static/assets/product/20220111_NDJ_product_analytics_reference.pdf "20220111_NDJ_product_analytics_reference.pdf").

For Metrics, we will discuss - what are google metrics, commonly encountered technical and product metrics, understanding different audiences in a marketplace, and metric frameworks.

In the product analytics section, we will discuss the product lifecycle, including initial product ideas, opportunity sizing, experimental design, and measurement and launch decisions. We will highlight some common questions used to understand and assess product health, such as diagnosing problems, setting goals for a product, measuring success, launch or not.

For A/B tests, we will discuss experimentation broadly as it relates to statistical practices and design. We will discuss challenges to A/B tests and dealing with those challenges.

The aim of this guide is to reinforce my own learning in these areas, and prepare for discussions with companies and clients.
I found many useful resources when collating this information, most notably; [Trustworthy online controlled experiments by Kohavi, Tang, Xu](https://www.amazon.com/Trustworthy-Online-Controlled-Experiments-Practical/dp/1108724264), and [Data interview pro](https://www.youtube.com/c/DataInterviewPro) on Youtube.

# Metrics

When creating metrics, good metrics tend to have these three characteristics;

- Simple - Easy to discuss and calculate
- Clear - Unambiguous with simple english
- Actionable - Can be effected

When discussing metrics, it is important to have a good understanding of who the audience or end-user is.
This is particularly important for businesses which may have multiple pillars, some examples of which are…

- Ride-share services with riders and drivers
- Food shopping companies which have consumers, shoppers, supermarkets and advertisers
- Digital media with consumers, creators and advertisers

Technical metrics are more related to website or app performance, often these are ‘hygiene factors’, that we expect a minimum acceptable behaviour.
These can also form good ‘guardrail metrics’, in that we want our experiments to have no major impact on load times. Some Common technical metrics include:

- Load time
- Website uptime
- num. crashes
- num. issues
- Storage performance
- Buffering time

Delving into product specific metrics, we will often have an organizational ‘North Star’, or ‘overall evaluation criteria’ (OEC) metric.
For companies like Meta this is ‘Daily active users (DAU)’.

When discussing products and experiments, we usually want to dig deeper to find more tactical metrics to measure experiment impact. Some examples of common product metrics (by audience types) include:

- Content consumers
    - Daily / monthly active users
        - Logging in
        - Watching for 5 seconds
        - (Consider cases which make sense for user activity)
    - Retention
        - Unsubscribes
    - Engagement
        - Watch time
        - Complete streams
        - Skips
- Creators
    - Paid vs free
    - Origin region
    - Analytics
    - Retention
    - Engagement activity
- Advertisers
    - Ads reach
    - Personalization
    - Click through rate (CTR)
    - Paying customers / views
    - Spend / view

Often, metrics frameworks can be a useful way to understand many parts of a product and process.

For example, when I worked in market research, we often used the ‘marketing funnel’. This allowed us to measure and understand how consumers perceived our client’s brands across many steps of engagement. Question wording would often include either more attitudinal (would you consider) vs behavioural style (did you shop within three months) questions.

Marketing funnel:

- Top of mind awareness (open ended)
- Prompted awareness
- Consideration
- Ever purchase / trial
- Recent purchase
- Ever recommend

This is similar to the ‘Growth metrics’ funnel framework (AARRR)

Growth metrics AARRR:

- Acquisition - awareness and sign up
- Activation - engagement and use of product
- Retention - re-use of product
- Referral - shares with others
- Revenue - increased customer LTV

Other frameworks include more of an ‘input and output’ setup, such as click through rate, and fraud detection.

# Product analytics

Product analytics helps us drive improvement in products by experimentation.
The book mentioned above ([Trustworthy online controlled experiments by Kohavi, Tang, Xu](https://www.amazon.com/Trustworthy-Online-Controlled-Experiments-Practical/dp/1108724264)) goes into detailed discussion of why organisations should consider a product analytics strategy and implementation steps.
For this section we will primarily focus on the role of a data science consultant interacting with the product analytics process.

The product analytics lifecycle includes four key stages:

- Initial product ideas
- Opportunity sizing
- Experiment design
- Measurement and launch decisions

Often data scientists will be required to make assessments of a product. These may include diagnosing a problem, measuring success, setting goals for a product, and launching or not.
The following section will discuss some strategies for framing, exploring and executing on these tasks.

Diagnosing a problem. I have had first hand experience with diagnosing problems on a [government infrastructure end-user research](http://www.ndjenkins.com/articles/professional/2022/01/09/project-experience-and-impact) project. The following is a recommended framework and discussion items.

- Clarify the expected function and goal of the product
    - Discuss and confirm high level goals of product i.e. Help people connect, find communities, grow their business
    - Confirm own understanding of product, discuss with team
    - Understand the audience(s) and how they use the product
- Diagnose the metric
    - Clarify how metric is measured. i.e. is the ‘start time’ when order is submitted or payment processes?
    - Changes to the metric usually involve a timing component, has the change been sudden or stable?
    - Is there internal business issues that have affected the product?
        - Own team or other teams
        - Technical: Bugs, data source, data collection, missing values
    - Have there been external pressures that have affected the product?
        - Political, special events, natural disasters,
        - Industry trends, competitors, partners changes (iOS releases, TVs)
        - Customer backlash and boycott
- Other product / feature by same company?
    - Is it possible another test is not guardrailed against our metric?
    - Are other products seeing similar change?
    - Is there evidence of cannibalization
- Segment by user demographics, behavioural features, (and attitudes)
    - Age groups, mosaic,
    - Geography, language
    - Frequent or high CLTV customers
    - Premium service customers
    - Platform (mobile vs web)
- Decompose the metric
    - Sometimes it can be helpful to break down the metric into components to open up further analysis.
        - i.e. Daily active users = existing users + new users + resurrected users - churned users
- Summarise overall approach
    - Weight towards the most reasonable causes
    - Propose how to fix

Measuring success and setting goals for a project can usually reuse much of the above framework and thinking.
Questions may take the form of How to measure success of a product? How would you measure the health of Mentions? How would you set the goals for (whatsapp, instagram, messenger).
A framework to help with these sorts of questions includes:

- Confirm understanding
    - Discuss and confirm high level goals of product i.e. Help people connect, find communities, grow their business
    - Understand the audience(s) and how they use the product
- High level metric buckets
    - Consider high level metrics, and which you’ll focus on for discussion
        - i.e. Engagement, Retention, Monetization
- User actions that support metric
    - How often and long using product
    - Interaction as follows, likes, shares
    - Consider multi-sided (i.e creator uploads)
- Success metrics, guardrails
    - Average watch time per user
    - Average # videos watched per session
    - Likes comments subscribe, consider as a funnel
- Guardrails
    - Churn
    - Reports
    - Diversity of content
- Evaluate trade offs

Often data scientists will help product teams assess if we will launch a product or not.
While at Boston Consulting Group, many projects involved launch / no launch decisions, through an initial pilot, or through a series of shorter experiments such as in [personalization](http://www.ndjenkins.com/articles/professional/2022/01/09/project-experience-and-impact).
We may be asked to assess how to test a product idea or launch feature? Or how would you set up an experiment to understand the change in instagram stories. How would you decide to launch or not if engagement within a specific cohort decreased?

- Clarify function and goal
    - Discuss and confirm high level goals of product i.e. Help people connect, find communities, grow their business
    - Understand the audience(s) and how they use the product
- Define metrics
    - 2 success metrics, i.e daily active users, number of bookings
    - 1 guardrail metrics, should not degrade
- Experiments
    - How to design
    - How to split users
    - How long to run
        - Statistical power and expected sample size
- Recommendation based on experiment results
    - Link results to the goal and business metrics
    - Conflicting results
    - Short term vs long term
- Restate and ensure recommendation is clear

# A/B Tests

While not a full guide to A/B tests and experimentation, the following are some important considerations to design.

- What units (customers, businesses, groups)
    - 50/50 control, test. Paired?
    - By days of week, by geography, at random? Stratified?
- How long to run the test
- Determine sample size through statistical power
    - Type II error and correctly rejecting null hypothesis
    - Significance level i.e. 95%
    - Minimum detectable effect - Smallest difference that matters in practice

Some challenges may come up depending on the business context, some examples of which include:

- Multiple testing problem
    - Using multiple test correction to avoid spurious p-value significance
- Novelty and primacy effect
    - Change aversion (primacy effect)
    - i.e. after a week it goes back to normal.
    - An option is to run only with first time users, or compare first time users
- Interference between groups
    - i.e. when its not possible to do split randomly (network effects, two sided market)
    - Network effects > experiment > two sided market
- Options to deal with challenges
    - Geobased randomisation
    - Time based randomisation

In summary, metrics, product analytics frameworks and A/B tests are great discussions to have to be an effective data scientist and provide impact to companies and clients. It is an area I am keen to continue growing in expertise.
