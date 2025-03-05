# Job relevance

Your task is make an assessment of a job's relevance to a candidate's resume and career goals.

You will be provided with the following information:

- Output format instructions
- Candidate's stated goals
- Example output
- Candidate resume
- Job description

## Output format instructions

Your output must conform to the following template

<template>

* ML/LLM Depth: <number>
* Prestige: <number>
* Compensation: <number>
* Skill Set Match: <number>
* Research Freedom: <number>
* Business Influence: <number>
* Engineering/Analytics Balance: <number>

## Pros

1. <text>
2. <text>
3. <text>

## Cons

1. <text>
2. <text>
3. <text>

</template>

- Do not add any other introduction, context or justifications, only output the required template data

## Candidate's stated goals

The candidate has the following primary goals, flexiblility in trading off, and hard no's.

#### **Primary Goals (Must-Haves)**
- **Hands-on ML/LLM Work**: At least **one-third of my time** must be spent on ML, LLM applications, or research.
- **IC Role, No People Management**: I want to stay as an **individual contributor (IC)**, leading technical work but **not managing direct reports**.
- **Strategic or Research-Oriented Work**: Either:
  - **Research-Heavy (80%+ ML/LLM R&D, lower prestige/compensation)**, or
  - **Execution-Heavy (Product-oriented, ML-influenced, high prestige/compensation).**
- **Business Value & Influence**: The role must **utilize my unique skill set**, especially my **consulting expertise**, technical leadership, and ability to drive ML adoption.

#### **Trade-Offs (Flexibilities)**
- **Prestige vs. Depth of Work**:
  - At a **high-prestige company** (e.g., Google), I accept that ML/LLM work may be **less exploratory**.
  - At a **less prestigious company**, I expect **deep research and experimentation**.
- **Compensation vs. Intellectual Freedom**:
  - If a **role is highly research-heavy**, I'm willing to trade **some salary** for it.
  - If a **role is highly execution-heavy** but at a strong company, I'm okay with that trade-off.
- **Consultative Work is Fine**: As long as I'm building AI solutions, I don’t mind **engaging with stakeholders**.
- **Some Business Analytics is Acceptable**: But the role should not be **entirely reporting-driven**.

#### **Hard No’s (Things I Absolutely Do Not Want)**
- **Primarily Data Engineering Roles**: Some engineering is fine, but the focus should not be **infra-heavy**.
- **Pure Business Intelligence (BI) Roles**: I don’t want to do **dashboards and metrics without ML impact**.
- **Full-Time People Management**: I do not want to be **a team lead or people manager**.

---

### **2. Potential Career Paths & Strategic Considerations**
The **next career step** should set you up for **one of two long-term paths**:

#### **Path A: Prestige & Compensation**
- **Target**: Google, Meta, OpenAI, DeepMind, Microsoft, etc.
- **Role Type**: Applied ML/LLM Data Scientist, Generative AI Consultant, ML Engineer.
- **Pros**:
  - High salary, strong name on resume.
  - Industry credibility and influence.
- **Cons**:
  - Likely **less research freedom**.
  - More **corporate and process-heavy**.
  - More **product execution, less experimentation**.

#### **Path B: ML/LLM Research & Thought Leadership**
- **Target**: AI-first startups, research labs, mid-tier tech companies.
- **Role Type**: ML Research Scientist, AI Consultant, Internal ML/LLM R&D Lead.
- **Pros**:
  - Freedom to **explore cutting-edge ML applications**.
  - Higher likelihood of **direct AI/LLM work**.
- **Cons**:
  - Likely **lower pay and prestige**.
  - Some companies may **lack strong engineering teams**.
  - May require **self-driven leadership** to create impact.

### **Hybrid Roles (Balanced Approach)**
Some roles, like the **Field Solutions Architect at Google**, blend both **prestige and hands-on AI work**. These are **high-value targets**.

This represents the best type of job, whereby the candidate gets everything they want.

The following is further detail on the **job scoring system** that evaluates job descriptions against your **priorities and trade-offs**.

### **Key Scoring Categories**
Each job should be evaluated on a **0-10 scale** across the following:

1. **ML/LLM Depth** (0-10)
   - How much time is actually spent on **ML research or AI-driven work**?
   - 0 = Pure reporting, 10 = ML research-heavy.

2. **Prestige** (0-10)
   - How much career credibility does this role give?
   - 0 = Small unknown company, 10 = Google/DeepMind/OpenAI.

3. **Compensation** (0-10)
   - How well does the role pay?
   - 0 = Low salary, 10 = FAANG+ level.

4. **Skill Set Match** (0-10)
   - Does the job **align with my expertise** (LLM, ML, NLP, consulting, analytics)?
   - 0 = Mismatch, 10 = Perfect fit.

5. **Research & Exploration Freedom** (0-10)
   - How much of the role is **dedicated to experimentation** vs. execution?
   - 0 = Pure product execution, 10 = Full-time research.

6. **Business Influence & Consulting Fit** (0-10)
   - Does the role **leverage my consulting skills**?
   - 0 = Internal-facing, no consulting, 10 = High stakeholder impact.

7. **Engineering vs. Analytics Split** (0-10)
   - Is it **too engineering-heavy** or **too analytics-heavy**?
   - 0 = Full software engineering, 10 = Full business analytics.
   - **Ideal target range: 4-7 (balanced).**

This structured approach will make **your job search significantly more efficient**, allowing you to **focus only on high-value opportunities**.


## Example output

* ML/LLM Depth: 9
* Prestige: 10
* Compensation: 9
* Skill Set Match: 8
* Research Freedom: 6
* Business Influence: 9
* Engineering/Analytics Balance: 5

## Pros:

1. Direct hands-on work with GenAI, LLMs, and cloud-based AI solutions.
2. More prototyping and experimentation, working with cutting-edge models.
3. Influence over Google Cloud’s AI strategy through real-world applications.

## Cons:

1. Less of a pure data science role; it leans more toward solutions engineering.
2. Strong customer-facing component (presenting and building prototypes for external clients).
3. Might involve less technical depth and more enablement (i.e., helping others use the models).

## Candidate resume

The following is the candidate's resume

{current_resume}

## Job description

The following is the specific job description of which to engage with

{job_description}
