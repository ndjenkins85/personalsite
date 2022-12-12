Before moving into data science consulting, I started my career in marketing. After university I was in advertising for a year, then moving into the market research industry for a further eight years. Looking back on the experience, I learnt a lot about consulting, marketing and market research techniques. I had the opportunity to leverage my data science and market research experience for a client while at Boston Consulting Group, and I hope to leverage these skills again in the future. As I progress in my career into new and exciting areas, I decided to write up a review of my experience. This could be a useful reference when working with clients in the future, or to go into further detail alongside my resume.

This will focus primarily on my quantitative market research experience. It will not cover the consulting experience or qualitative skills during this period.

Topics:

- End-to-end market research
- Survey questionnaire design
- Analysis types
- Data cleaning
- Innovations

# End-to-end market research

Over eight years I worked as an ‘end-to-end’ market research consultant.

- I directly worked with clients to design and recommend survey questionnaire design to help answer their business questions
- I would conduct statistical analysis to determine sample size needs, respondent quotas
- I worked with either client email lists, or worked with survey panel vendors to prepare survey mail-out
- I was a capable survey programmer, I used in-house software, Qualtrics, and survey-monkey to program surveys including advanced experiments
- I conducted survey pilots to validate the survey and data collection process before full-launching
- I set up survey data analysis, including weighting, data cleaning, and experimental models
- I conducted thorough exploratory data analysis to find key insights
- I prepared reporting decks to bring the survey results to life, with a focus on answering business questions
- I presented results to clients and recommended possible next steps and business impact

# Survey questionnaire design

Reflecting on my experience designing survey questionnaire for clients, I found the following useful to keep in mind.

- It is always tempting to ask more questions, but longer surveys come at the cost of respondent attention and can lead to poorer quality data.
- Randomize whenever possible. This can include within-questions, within question blocks, or even sections of the survey. There were a few specific occasions not to randomize, i.e. when answers (brands) are alphabetical, logical scales.
- Consider when it is appropriate to add a ‘not applicable’ to questions. These will often result in missing data, which can be a problem. Another problem can be forcing a choice.
- Add a ‘none of these’ where appropriate (i.e. for multiple choice). This ensures an answer is punched, which is useful for data validation (question was correctly asked).
- Be mindful of the survey question wording - ask one thing at a time, avoid ‘double barrelled’ questions otherwise you can’t interpret the answers.
- Consider when it is appropriate to use two sided rating scales (disagree vs agree), or single sided (none at all, highly likely)
- Consider converting answers into ‘top 2 box’ (i.e. % agree). This will ‘flatten’ the data, simplify interpretation, make it easier to cross tabulate, and improve statistical power.
- Add demographic questions to surveys, always useful as a gut check or for weighting back to populations and geographies.
- For panel based surveys, use screening questions. Panel respondents are incentivised to respond to surveys, so to be sure that you are speaking only to your relevant audience, you may want to add ‘implausible’ conditions. For example, someone who goes skiing 3 times a year, travels to Africa 3 times a year, xxxxyyy 3 times a year, and works full time. Occassion based responses are excellent to screen for very high activity in too many areas.
- When programming surveys, be mindful of usability. This can include keeping language simple and concise, increasing font and graphic sizes for older or visually impaired respondents, adding ALT text to improve usability for alternative computer interface users.

# Analysis types

While in market research, my interest in quantitative analysis grew and grew. I enjoyed the data management, preparation and analysis steps of the process most of all - and this is no surprise given my career trajectory into data science! I had experience with the following techniques.

- Conducting basic statistical tests of proportions (chi-squared) and numeric rating scale (t-test) data, being mindful of null hypothesis and multiple comparisons.
- Analysis of customer satisfaction, net promoter score, key drivers and improvement strategies
- Using marketing funnel frameworks to understand the customer journey. This included using: Top of mind awareness, total awareness (prompted), consideration, trial, regular usage, recommendation (NPS).
- Creating data splits (a.k.a banners) to readily analyse results by key groups
- Advanced survey design including maxdiff (best worse), and choice analysis
- Customer segmentation, using attitudinal, behavioural and demographic features, allocation of segments
- Principle components analysis, useful to simplify large question batteries into simple themes, multiple correspondence analysis for visualisation, or for use in segmentation and regression
- Regression and random forest, for understanding feature importance and variance capture.
- Multivariate (rim) weighting to maximise effective sample size when augmenting data to be representative of a population

# Data cleaning

When preparing survey data for analysis, I found the following steps useful to improve the overall quality of the data. These methods were used to remove respondents with poor quality survey results. In general, I used a ‘demerit points’ system, to attribute scores to specific behaviours. We could then apply a threshold to the total points per respondent.

- As mentioned earlier, screening questions for ‘implausible’ responses
- Flatline responses to question batteries
- Speeders, in terms of total survey time, or an estimated minimum read speed per question wording.
- Open ended responses which are nonsense as if someone has ‘face rolled’ over the keyboard. We also kept an eye out for bot style text

In addition to these, we would watch for outliers for regression analysis, and extreme values for weighting where quotas were not adequately reached. If needed we would remove an entire weighting cell if the values were too low.

# Innovations

As I developed my python and analytic skills in market research, I started to contribute new innovations to the business. These were either pain points, business opportunities, or quality of life improvements.

- Created a tool to attempt to automatically fill in surveys with random data. This used python selenium library. This was useful to exhaustively test survey pathways, and detect problems with the expected branch flow vs number of filled surveys. This also allowed us a head start in the analysis setup, as we had dummy data to begin project setup.
- Created in-house capability to classify open-ended text responses into categories. This took a slow, expensive, manual process and allowed us to speed up and scale the categorisation of text into pre-formed categories. We developed tooling to allow clients to understand and accept different levels of predictive accuracy, which allowed us to trade off automatic categorisation of simple/straightforward text and to manually review more complex responses. We sold several projects based on this cutting edge functionality.
- Creation of sentiment and engagement text analysis models for open-ended text. Similar to the above, I added new tooling to the business to perform response level or keyword level sentiment and engagement scoring. We scaled this functionality across all surveys and provided a value add to our client servicing. We did this by creating our own ‘gold standard’ sentiment scoring as a hold out test set, and utilised our in-house overall satisfaction matched to open ended feedback to develop models.
- Also in the text analytics space, I created the businesses first production ready chatbot. The aim was to increase respondent engagement, obtain highly granular and quality feedback, while ensuring a short and quality survey experience. This was a significant innovation for our business, which has since seen much success from this product offering.
- Several of our clients conducted a high volume of ongoing surveys. We developed automated reporting scripts to pull together several data sources, data cleaning steps, weighting, analysis and regressions. This allowed us to get a head start on the week and report with confidence in time for our client’s C-level briefings.

To summarise, I am very thankful for my career experience in market research. It set me up to pursue a career in data science consulting. I still use many of the same techniques and skills in current day. The world is moving more towards the use of in-house behavioural and sales data, and to product analytics and experimentation. This is particularly the case with tech companies, and is an exciting space to be a data scientist. That being said, market research will continue to be an important part of the marketing landscape. Behavioural data can tell you when what and how, but market research can help marketers understand the why.
