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
    - promotions, pricing, big data, infra, ML, pilot
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

The goal of the project was to enable BCG case teams to quickly access curated third-party data sources. I contributed to this goal by:

- Increasing available datasets from 20 to 40 during tenure
- Established the 'integration' squad to accelerate dataset availability and quality
- Led and mentored seven data scientists to implement integrations
- Proved value of Lighthouse to support BCG proposals, such as using footfall data as a proxy for store revenue

- XFN teaming
    - Eight XFN partners; leadership, legal, procurement, vendors, infrastructure, BCG partners, case teams, within-squad.
    - Quickly established respect and trust in working relationships, set expectations clearly, was clear about asks for input, setup of dedicated weekly progress and content meetings. Looked to understand XFN perspectives and motivations, and find win-win solutions.
- Leadership
    - First dedicated leadership role at BCG
    - I led four junior data scientists at any one time, and seven overall. Created onboarding, checklists and process documents to set expectations with the team. Setup weekly feedback and content sessions. Provide support to unblock, and enable the team to take ownership of tasks.
- Workstream development
    - Scope and processes for integrations not well defined
    - Pulled together all resources and knowledge to draft 'best practices' guidelines for new data integrations. I seeked feedback and input from XFN partners. Executed first few integrations which care to meet standards and make adjustments.
- PMO
    - Many new integration projects in backlog (up to 40 projects)
    - Utilized Jira to set up kanban style project tracking, established clear guidelines for project status and work items required. I seeked feedback from leadership and XFN partners on integration readiness and priorities. Discussed with team members project allocations and prioritization.

### Payroll contract pricing

Assess contract pricing for new and existing customers to determine churn impact and reduce pricing cycles.

The goal of the project was to help a B2B payroll service provider assess ideal contract pricing to maximise profit and reduce churn. I contributed impact to this project by:

- Providing a robust analytical pricing recommendation, using ML and explainable AI principles. This empowered the sales team to drive towards ideal contract pricing with a minimum of iterations; the increased speed resulted in reduced internal costs due to iterations, and faster contract turn around time with customers
- Combined pricing research with churn analysis to show impact of price changes on churn rate. This lead to increased willingness to engage in customer pricing negotiations.
- Demonstrating technical project leadership and finding alignment with fellow data scientists. This enabled us to provide a high quality python codebase with version control, configurability, and documentation.

- XFN teaming
    - Several XFN partners; Non-technical PMs and lead, technical collegues and lead, BCG partners, client DS team, client strategy team.
    - Looked to understand XFN perspectives and motivations. Needed to convince non-technical stakeholders to trust in data science process, and that results are not immediate. Supported their requirements by designing codebase to support configuration in relevant areas. I regularly contributed to daily check-in and check-outs to drive work to completion, align with team, and collaborate on next steps. There were additional challenges by working fully remote and not meeting, this was partly overcome by allowing additional team time for social meetings.
- Pricing
    - Difficult to assess client pricing and profitability due to variability in charge rates, bonus payments, pay periods.
    - We created a robust data engineering pipeline to ingest, clean and analyse pricing over time.
- Data management
    - As the client had taken over several companies, there were over 50 different data sources provided for payroll, insurance, client information etc. Some of which was structured database tables, others as excel or reports.
    - I implemented a data manifest process which standardized how to document information, the ingestion process, and how data was prepared for modeling.
- Infra
    - Due to data sensitivities, we needed to work on client infrastructure, which included a VM and no local data transfer.
    - I set up a standard process on the client infrastructure to ensure that we had a version control codebase, and python packaging so that we could deploy process to client infrastructure.
- ML
    - We needed to make the most use of available data, while providing an explainable model.
    - I recommended a two-step approach: use a 'kitchen sink' random forest based model to find predictive ceiling and most relevant features, then utilize best features in an interpretable linear regression model. We found methods to reduce the predictive gap between models such as log variables.
- Client training
    - The client was not very familiar with using pure python codebases, and the specific data preparation and modeling strategies.
    - We held weekly update and collaboration sessions with the client to discuss results. Towards project delivery, we held daily training sessions with client data science team, including preparing the codebase into jupyter notebooks at the request of client team.
- Pilot
    - The project produced deliverables needed to prepare a segment of customers for a pilot of the updated process.
    - We prepared analysis results as an excel simulator and recommended price change to support the process change pilot.

### Wholesaler pricing

Promo effect attribution and optimization for over $1 billion annual spend.

*promotions, pricing, big data, infra, ML, pilot*

- Goal
    - Worked with a B2B food distribution company to improve the effectiveness of their promotions with the goal of increasing purchase volume.
- Impact
    - $1b of promo spend optimized
    - We created an analytics pipeline to attribute historic promotion impact, and used this to recommend fund reallocation towards high performing promos
    - We provided analysis and recommendations to client for ideal recommended retail price, to optimise for multiple metrics (volume, revenue, profit), and guardrail conditions (minimum profit, competitive pricing), as well as highlighting elastic vs inelastic product sets.
- Challenges
    - Many categories, subcategories and SKUs, hard to generalise results
    - Complex promotion systems, i.e. vendor, client and customer contribution,
    - Required complex allocation system for overlapping timing windows, fill forward, cannibalisation
- Skills and learnings
    - Deeper insight into B2B wholesaler space and complex business rules
    - Further opportunity to mentor two junior data scientists
    - Started developing own frameworks around data engineering and pyspark comfort

### BCG risk and best practice ring-fence

Stakeholder engagement to assess project risk and ensure high quality deliverables.

*infra, workstream development, PMO*

- Goal
    - Ensuring high quality projects and deliverables for our clients is BCG’s highest priority. I joined a ring-fence team which focused on providing project support to assess project risk and best practices, to ensure high quality outputs.
- Impact
    - Audited around 20 live cases across several attributes including legal, data use, teaming, infrastructure, modelling
    - Provided first hand coaching and review of codebases with junior team members, to support busy case leadership teams
    - Improved the auditing and onboarding process to help the ring-fence team scale and rotate new team members
- Challenges
    - Worked directly with busy BCG partners to explain audit process, provide guidance, and expert input on best practice
    - Quickly absorbing current best practice standards so I could provide expertise to teams
- Skills and learnings
    - Developed relationships with BCG leadership
    - Rapidly improved my python skills to provide expertise to case teams on successful python project delivery

### Survey data predictive value

Demonstrate survey data value as an employment rate leading indicator.

The aim of this project was to work with a political polling data vendor to assess and recommend additional revenue streams for their data. I contributed to the project in the following ways:

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
