# Python Data Analysis: How I Built a Data Pipeline

I created this project to show how raw, messy datasets can be programmatically cleaned, analyzed, and visualized. Instead of running analysis on clean CSVs, I wanted to document the actual grunt work: loading data from APIs, dealing with missing values, and running statistical checks to verify my findings.

Here is the step-by-step breakdown of how the code works and the choices I made along the way.

---

## The Code Step-by-Step

### 1. Starting with Python basics
Before diving into libraries like Pandas, I focused on basic syntax. I wanted to make sure I was using the right data structures for the right tasks:
* **Lists** were my choice for ordered data that needed to be sorted or changed on the fly, like names or simple numbers.
* **Tuples** came in handy for fixed values that shouldn't change. Attempting to modify a tuple raises an error, which prevents bugs later on.
* **Dictionaries** worked best for key-value pairs where lookup speed matters and duplicate keys aren't allowed. 

### 2. Loading and cleaning the data
Data is rarely clean. I used NumPy and Pandas to pull down raw financial data (Samsung stock prices from Naver and SPY ETF from Yahoo Finance) and clean up local transaction files. 

For the cleaning script:
* **Standardizing columns**: I renamed columns to clean up messy formatting and cast categories to the correct data types.
* **Missing values**: I used forward-fill (`ffill`) and backward-fill (`bfill`) for time-series data to maintain continuity. For other datasets, I filled missing values using the column median to avoid skewing the averages.
* **Duplicates and splits**: I dropped duplicate rows and used string splits to break up compound product codes (like `ID-suffix`) into separate columns.

### 3. Transforming and analyzing the numbers
Once the data was clean, I wrote logic to slice it and calculate metrics:
* **Filtering**: I used Pandas boolean indexing and `.query()` to pull specific records, like high-scoring students in engineering.
* **Derived columns**: I calculated things like participation rates and inserted them directly into specific index spots in the tables.
* **Joins**: I merged tables using left joins to align student data with scholarships.
* **Outliers and correlations**: I calculated Z-scores to see how far values sat from the average. I also set Interquartile Range (IQR) fences to catch extreme outliers and ran correlation matrices to see how variables moved together.

### 4. Making charts
I split my charts into two groups based on who was looking at them:
* **For quick diagnosis**: I used Seaborn to generate histograms of return splits, box plots to check spreads, and correlation heatmaps to spot relationships quickly.
* **For presentations**: I spent time polishing the visuals. I adjusted axis limits, changed line styles and markers, used colorblind-safe colors, and added text notes directly onto the charts so the viewer can see the main point immediately.

---

## What I learned from this project

* **Cleaning takes up most of your time.** You spend 80% of your time formatting, removing duplicates, and handling nulls. If your input data is wrong, your final chart will be wrong too.
* **Vectorization is much faster than loops.** When working with 1,000 rows, iterating with loops is slow. Writing vectorized operations in Pandas lets the computer run calculations in compiled code, which is nearly instant.
* **Good charts don't need explanation.** An exploratory plot is fine for an analyst, but a slide deck needs custom axes, clear labels, and annotations pointing out the main trend.
* **Look at the numbers, not just the charts.** A visual correlation can be misleading. You need calculations like Z-scores and IQR outlier counts to prove your findings are mathematically sound.
