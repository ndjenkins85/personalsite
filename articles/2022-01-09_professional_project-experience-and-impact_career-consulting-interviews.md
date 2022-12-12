I have put together a list of data science projects I have worked on and their business impacts. This helps to highlight the depth and breath of my consulting experience. It may also be a useful supplement to my resume and for discussions.

List of projects with synopsis and key topics.

### Boston Consulting Group

- **Lighthouse: BCG feature store**
    - Development of a scalable, high frequency data and feature store for BCG case teams
    - XFN teaming, leadership, workstream development
- **Payroll contract pricing**
    - Assess contract pricing for new and existing customers to determine churn impact and reduce pricing cycles
    - XFN teaming, pricing, data management, infra, ML, client training, pilot
- **Wholesaler pricing**
    - Promo effect attribution and optimization for over $1 billion annual spend
    - promotions, pricing, big data, ML, pilot
- **BCG risk and best practice ring-fence**
    - Stakeholder engagement to assess project risk and ensure high quality deliverables
    - infra, workstream development
- **Survey data predictive value**
    - Demonstrate survey data value as an employment rate leading indicator
    - ML, data management
- COVID employment recovery research (3 weeks)
    - Estimate employment rate recovery at COVID onset in April 2020
- Consumer goods - Order replenishment (3 weeks)
    - Analyze historical purchase behavior to provide customer recommendations for item replenishment
- **High end fashion retailer**
    - $52 million personalization pilot to experiment on many products and sales offers.
    - personalization, product analytics, big data, client training, pilot

### Evolve Research

- **Chatbot for survey engagement**
    - Development of survey chatbot to improve respondent engagement and research insight to support new business development
    - ML, NLP, infra, leadership, workstream development
- **Text analytics capability**
    - Development of text classification and sentiment scoring capability to support new business development
    - ML, NLP, infra, workstream development
- **Government infrastructure end-user research**
    - Measuring end-user satisfaction with large scale infrastructure project affecting all Australians
    - ML, infra

### Lighthouse: BCG feature store

Development of a scalable, high frequency data and feature store for BCG case teams.

Lighthouse empowers BCG case teams to access curated, third-party data sources. We have had several case teams use the data to high effect. I have contributed to the goals of the project by:

- Doubling the number of available assets from 20 to 40
- Established a team of 'integration' specialists to increase dataset availability and quality
- Led and mentored seven data scientists to perform integration duties
- Proved value of Lighthouse data to support several BCG proposals and case teams. Including a multivariate model to bring together many datasets to estimate client revenue.

- XFN teaming
    - Worked with nine XFN partners. These included external providers such as vendors, contractors and clients. It included 'internal clients' such as leadership, case teams, partners. We also worked with legal, procurement, other Lighthouse squads and analytics support.
    - I established respect and trust in these working relationships. We would work to understand each other's objectives, and set our expectations. I worked with teams to seek input, setup dedicated meetings and drive progress.
- Leadership
    - First dedicated leadership role at BCG
    - I led four junior data scientists at any one time, and seven total. Created onboarding, checklists and process documents to set expectations with the team. Setup weekly feedback and content sessions. Provide support to unblock, and enable the team to take ownership of tasks.
- Workstream development
    - Scope and processes for integrations not well defined
    - I collated existing knowledge and resources. This led to draft 'best practices' guidelines for new data integrations. I requested feedback and input from XFN partners. We executed early integrations with attention to our guidelines and opportunities to improve.
- PMO
    - Many new integration projects in backlog (up to 40 projects)
    - We tracked all project details in Jira using a Kanban style project lifecycle. I established clear expectations for team to report project status and inputs required. I requested feedback from leadership and XFN partners on integration readiness and priorities. Discussed with team members project allocations and priorities.

### Payroll contract pricing

Analysis of customer contract pricing to determine churn impact and reduce pricing cycles.

We helped a payroll provider assess pricing to maximise profit and reduce churn. We analyzed which factors are important to determining contract pricing. This insight resulted in fewer pricing cycles, speeding up the contract process. Our results also indicated that customers were not very price sensitive. This gave the client confidence in approaching customer pricing negotiations and improved profitability. I contributed impact to this project by:

- Providing a robust analytical pricing recommendation, using ML and explainable AI principles. This included searching over 2000 possible features to determine the most important 15.
- Worked with team to integrate pricing and churn models to show impact of price changes on churn rate.
- Lead the data management, coding and infrastructure solution for the project. This enabled us to deliver quality codebase with version control, configurability, and documentation.

- XFN teaming
    - Worked with several XFN partners. This included strategy focused client, BCG consultants and partners. Also included technical DS clients, DS team and DS lead.
    - Looked to understand XFN perspectives and motivations. We needed to prove the data science process to non-technical stakeholders. We did this by being transparent about the setup process, and when initial results are ready. We supported their use-cases by designing a configurable codebase for fast analytics turnaround.
- Pricing
    - It was difficult to get a true picture of customer pricing and profitability. This is due to variability in charge rates, bonus payments, pay periods.
    - We created a robust data engineering pipeline to ingest, clean and analyse pricing over time.
- Data management
    - We received over 50 different data sources in a variety of formats from the client. These included features such as payroll, insurance, and customer information.
    - I implemented a data manifest process to standardize knowledge capture. This helped the team to dig into different areas, and provide useful summaries. The standards informed ownership, ingest method, data dictionary, and use in models.
- Infra
    - We needed to work on client VM due to sensitive data, without ability to transfer any code or data.
    - I set up a standard workflow to support best practice software development. This included codebase version control, environment management, and python packaging. This afforded us repeatability in our analysis and ease of deployment to client.
- ML
    - We needed to analyze all available client data, while providing an explainable model.
    - I proposed a three-step approach. A random forest model to find the predictive ceiling and most relevant features. Then, use the top features in an interpretable linear regression model. We worked on feature tweaks to reduce the predictive gap, such as log transformations.
- Client training
    - The client was not used to working with python applications. There was also knowledge transfer needed for data preparation and modelling approach.
    - We held weekly update and collaboration sessions with the client to discuss results. Towards project delivery, we held daily training sessions with client data science team. We prepared jupyter notebook tutorials to guide client DS through a familiar interface.
- Pilot
    - We prepared project analysis outputs to support an upcoming pilot. We needed to prepare the client strategy and DS team to launch the pilot.
    - We prepared an excel simulator with configurable controls. This gave the strategy team insightful tools to guide pricing decisions. As mentioned in client training, we provided deep knowledge transfer to the team.

### Wholesaler pricing

Promo effect attribution and optimization for over $1 billion annual spend.

We helped a B2B distribution company to increase sales volume. We created models to attribute promotion performance and expected secondary effects. This allowed us to identify best and worse performing promotions. This guided decision making towards effective promotions and maximizing sales volume. I contributed to this project by:

- Analysis of ideal SRP - the recommended retail price issued by the B2B distribution company. Created robust, SKU and multi-level model to estimate ideal SRP and price elasticity. This enabled maximization estimates and profit share simulation
- Helped standardize the data engineering and codebase workflow. This included version controlled code, repeatable workflows, and pyspark optimizations
- Providing support to junior DS team members, particularly on codebase design

- Promotions
    - The promotional calendar and method was complex. Promotions had several modalities, with involvement by retailers, wholesaler and producers.
    - Considerable work was undertaken to understand promotions. This included how they related to each other and how to define
attribution. Beyond this, we analyized for secondary effects such as cannibalization and pull forward.
- Pricing
    - This project included wholesaler SRP recommendations to retailers. Increasing order volume was a primary motivation of the wholesaler.
    - I helped show that SRP was a significant factor in order volume using GLMs. This allowed estimations of SRP elasticity per SKU and enable further volume optimizations. I created compelling reporting to highlight discussion points around guardrails and win-win outcomes.
- Big data
    - We were working with several hundred gigabytes of promotional and order data.
    - We used the dataiku platform for data storage and engineering pipeline. Alongside this we used pyspark and version controlled codebase. This helped us keep the codebase modular and documentation centralized.
- ML
    - The SRP data had few records per SKU, and little variation over price ranges. It appeared to be challenging to pull together coherent analysis.
    - We were able to address data problems and produce a successful model. We used SKU hierarchy to fill information from similar products (i.e. flavour variants). We created linear models with a monotonic increasing constraint for SRP. We were able to use this for elasticity estimates at SKU, sub-category, and category level.
- Pilot
    - We prepared project analysis outputs to support an upcoming pilot. We needed to prepare the client strategy and DS team to launch the pilot.
    - We prepared pipelines to populate SRP and secondary effects for the upcoming pilot. The pipeline was replicatable, which would help the client team in future cycles.

### BCG risk and best practice ring-fence

Stakeholder engagement to assess project risk and ensure high quality deliverables.

The team goal was to ensure that all active projects had completed a risk assessment. This was to ensure all projects were being delivered with quality standards, with no risk to BCG. During my time in this team, I helped course correct a few projects. My impact included:

- Audited 20 projects across legal, data use, teaming, infrastructure, modelling domains
- Worked with teams to find solutions to quality issues. This included finding alternative sources for incorrect sourcing of third-party data.
- Coaching junior project team members and codebase review
- Improved ring-fence onboarding process to help the team scale

- Infra
    - I needed to dive into various codebases to understand them and propose improvements
    - I spent time to learn python packaging and libraries process. This allowed me to provide guidance to case teams on best practice.
- Workstream development
    - The ring-fence team was self-directed
    - I found many areas to contribute, including best-practice documentation and onboarding process.
- PMO
    - Much of the work included scheduling, meetings, and task tracking among team members.
    - We utilized Jira to track projects, with custom fields to note upcoming appointments. We standardized our workflow so that it became easy to track status of many projects.

### Survey data predictive value

Demonstrate survey data value as an employment rate leading indicator.

The aim of this project was to work with a political polling data vendor to assess and recommend additional revenue streams for their data. We were successful in demonstrating a valuable use case (unemployment forecasting), culminating in ongoing use of the data for BCG clients. I contributed to the project in the following ways:

- We proved the value of the survery data as a weak, leading indicator of regional unemployment.
- I contributed to the project by advocating for strong statistical controls including time based train/test and strong baseline models for comparison.
- I used my market research survey experience to work quickly and comfortably with the data to prepare it for a ML pipeline.
- I provided recommendations to the client on improvements to survey data collection methods

- ML
    - Difficult to produce statistically significant findings with relatively few data points
    - Convinced team to employ a robust baseline to test for effects from the market research data. We used gradient boosted regression to produce robust estimates, and quantile regressions for confidence intervals. We also used time based train/test splits for unbiased estimates of future performance.
- Data management
    - Data size was relatively small, needed to consider trade off between granularity, aggregation and base validity. Needed to align data to available unemployment figures.
    - We designed a data setup to support different levels of aggregation; i.e. geographical to county, state, region, and time-based to week, month, quarter. We aligned on state level, monthly data, to trade off between having suitable sample within each cell for aggregation, and enough data points for a ML solution.

### High end fashion retailer

$52 million personalization pilot to experiment on many products and sales offers.

The overall goal of the project was prove the effectiveness of personalized sales offers to increase revenue via sales lift %. Overall the project as a great success and we showed significant lift above client BAU (about 25%). I had the following impacts on the project.

- I created several sales offers, including the sizing and experimental design.
- Model creation for a triggered cross-shopping offer based on basket analysis and recommender systems of previous shops.
- I translated several existing offers from SAS to our pyspark codebase, and used these as training examples for the client.
- I helped train the non-technical team members in SQL to help them self-serve analysis requests.

- Personalization
    - I did not have deep knowledge of personalization before starting the project.
    - Throughout the project I learnt about the core tenants of personalization (right offer, right person, right channel, right time), and regularly asked questions to deepen understanding. I was exposed to several new technologies and frameworks and learnt; software engineering skills, SQL for data ingest, github, pyspark, AWS, airflow, SAS.
- Product analytics
    - The personalization project also included the standard product analytics requirements of identifying metrics, experimental design, and measurement.
    - I learnt about these elements of product analytics, and additional things to watch out for, such as control/test contamination, triggering, and cannibalization.
- Big data
    - We were working with several GB of daily data for transactions, inventory, and customer information
    - This required me to quickly become comfortable working in SQL and pyspark in order to effectively contribute to the project analysis.
- Client training
    - Client data science team very busy with BAU, and not familiar with python / pyspark codebases
    - I pitched in to help take on maintenance of some existing BAU offers, and converted them to work with our new infrastructure. This became a focal point for training and upskilling with the client data science team.
- Pilot
    - We ran several experiments on new offers each week, and needed to track overall project performance regularly.
    - The team needed regular communication to understand the status of experiments and how they contributed to the overall project. Where appropriate, I provided input, insight, and recommendations to help explain experiment results.

### Chatbot for survey engagement

Development of survey chatbot to improve respondent engagement and research insight to support new business development.

*ML, NLP, infra, leadership, workstream development*

- Goal
    - Build a market research survey chatbot to increase respondent engagement and quality of feedback while retaining guardrail metrics, and highlight the company as a key market research innovator and competitive advantage.
- Impact
    - We created a full chatbot solution along with metrics and guardrail metrics, including increased ‘quality’ of information as tested against explainability of overall satisfaction, quantity of text information, while maintaining survey completion rate and unsubscribe rate.
    - The chatbot solution used NLP based models (keywords, sentiment, classification), state machines, and a docker based API to serve chatbot requests to users
- Challenges
    - Hard to identify metrics and quantify improvement
    - Technology challenges early in career
- Skills and learnings
    - Learnt API, state machine frameworks
    - Worked with junior analysts to create effective keyword based hierarchies

### Text analytics capability

Development of text classification and sentiment scoring capability to support new business development.

*ML, NLP, infra, workstream development*

- Goal
    - Open ended text responses in market research surveys a quality source of insights, however these require slow, expensive and manual review. I designed a text classification and sentiment scoring process to quickly and accurately compile insights, in a highly scalable way.
- Impact
    - We successfully piloted the text classification process with a client, enabling them to save $30k per year on text analytics costs
    - We sold several projects based on this capability to other clients, with new revenues of $120k in first year, and $300k in second.
    - We provided scalable sentiment scoring analysis to all projects as client value add.
- Challenges
    - Technical modelling challenges with small categories, complexity of feedback, working with unstructured data
    - Developing a process which was transparent to accuracy, trade-offs, and value
- Skills and learnings
    - Learnt strong python and machine learning fundamentals, advanced text analytics techniques
    - Worked with business owner to productise and sell the innovation to clients

### Government infrastructure end-user research

Measuring end-user satisfaction with large scale infrastructure project affecting all Australians,

*ML, infra, PMO*

- Goal
    - Assist the client in understanding customer satisfaction with their service and root cause issues across segments
- Impact
    - We surveyed millions of Australian consumers on their infrastructure satisfaction and several points in lifecycle including installation, 3 months, and 6 months into usage.
    - Used robust data science approach to estimate root cause of customer satisfaction, across several segments
- Challenges
    - Large amount of data and weighting requirements
    - Creating automated data ingestion and analysis processes to support early week reporting
    - Creating infrastructure to handle hundreds of linear regressions and random forest based feature importance
- Skills and learnings
    - Python and pandas
    - Ability to break down data and analytical problems into executable code
    - Project mangagement
