# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Test Analysis

### Overview

Our first module in DSI covers:
- Basic statistics and probability
- Many Python programming concepts
- Programmatically interacting with files and directories
- Visualizations
- EDA
- Working with Jupyter notebooks for development and reporting

You might wonder if you're ready to start doing data science. While you still have **tons** to learn, there are many aspects of the data science process that you're ready to tackle. Project 1 aims to allow you to practice and demonstrate these skills.

For our first project, we're going to take a look at aggregate SAT and ACT scores and participation rates in the United States. We'll seek to identify trends in the data and combine our data analysis with outside research to address our problem statement.

The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

The SAT has two sections of the test: Evidence-Based Reading and Writing and Math ([*source*](https://www.princetonreview.com/college/sat-sections)). The ACT has 4 sections: English, Mathematics, Reading, and Science, with an additional optional writing section ([*source*](https://www.act.org/content/act/en/products-and-services/the-act/scores/understanding-your-scores.html)). They have different score ranges, which you can read more about on their websites or additional outside sources (a quick Google search will help you understand the scores for each test):
* [SAT](https://collegereadiness.collegeboard.org/sat)
* [ACT](https://www.act.org/content/act/en.html)

Standardized tests have long been a controversial topic for students, administrators, and legislators. Since the 1940's, an increasing number of colleges have been using scores from sudents' performances on tests like the SAT and the ACT as a measure for college readiness and aptitude ([*source*](https://www.minotdailynews.com/news/local-news/2017/04/a-brief-history-of-the-sat-and-act/)). Supporters of these tests argue that these scores can be used as an objective measure to determine college admittance. Opponents of these tests claim that these tests are not accurate measures of students potential or ability and serve as an inequitable barrier to entry.

### My problem Statement

Our project aims to identify the counties within California that have the worst overall student performance on the SAT tests so that we can recommend programmes and allocate resources to these counties in need. 

We will also delve deeper into the underlying reasons why some counties underperform to better calibrate our response / recommendations to each individual state.

---

### Datasets

#### Provided Data

There are 10 datasets included in the [`data`](./data/) folder for this project. We have selected the following:

* [`act_2017.csv`](./data/act_2017.csv): 2017 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)) (SELECTED)
* [`act_2018.csv`](./data/act_2018.csv): 2018 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)) (SELECTED)
* [`act_2019.csv`](./data/act_2019.csv): 2019 ACT Scores by State ([source](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)) (SELECTED)
* [`act_2019_ca.csv`](./data/act_2019_ca.csv): 2019 ACT Scores in California by School
* [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)) (SELECTED)
* [`sat_2018.csv`](./data/sat_2018.csv): 2018 SAT Scores by State ([source](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)) (SELECTED)
* [`sat_2019.csv`](./data/sat_2019.csv): 2019 SAT Scores by State ([source](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent)) (SELECTED)
* [`sat_2019_by_intended_college_major.csv`](./data/sat_2019_by_intended_college_major.csv): 2019 SAT Scores by Intended College Major ([source](https://reports.collegeboard.org/pdf/2019-total-group-sat-suite-assessments-annual-report.pdf))
* [`sat_2019_ca.csv`](./data/sat_2019_ca.csv): 2019 SAT Scores in California by School (SELECTED)
* [`sat_act_by_college.csv`](./data/sat_act_by_college.csv): Ranges of Accepted ACT & SAT Student Scores by Colleges ([source](https://www.compassprep.com/college-profiles/)) (SELECTED)

#### Additional Data
We have sourced for the following datasets:

* [`CA_1969_2019.csv`](../data/CAINC1_CA_1969_2019.csv): Personal income by County, Metro, and Other areas ([Add.Source](https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas))
* [`frpm1617.xls`](../data/frpm1617.xls): 2017 California free or reduced price meals by school ([Add. Source](https://web.archive.org/web/20200513024019/https://www.cde.ca.gov/ds/sd/sd/filessp.asp))
* [`frpm1718.xlsx`](../data/frpm1718.xlsx): 2018 California free or reduced price meals by school ([Add. Source](https://web.archive.org/web/20200513024019/https://www.cde.ca.gov/ds/sd/sd/filessp.asp))
* [`frpm1819.xlsx`](../data/frpm1819.xlsx): 2019 California free or reduced price meals by school ([Add. Source](https://web.archive.org/web/20200513024019/https://www.cde.ca.gov/ds/sd/sd/filessp.asp))
* [`currentexpense1617.xlsx`](../data/currentexpense1617.xlsx): 2017 California current expense of education per average daily attendance by county ([Add. Source](https://web.archive.org/web/20200524071811/https://www.cde.ca.gov/ds/fd/ec/currentexpense.asp))
* [`currentexpense1718.xlsx`](../data/currentexpense1718.xlsx): 2018 California current expense of education per average daily attendance by county ([Add. Source](https://web.archive.org/web/20200524071811/https://www.cde.ca.gov/ds/fd/ec/currentexpense.asp))
* [`currentexpense1819.xlsx`](../data/currentexpense1819.xlsx): 2019 California current expense of education per average daily attendance by county ([Add. Source](https://web.archive.org/web/20200524071811/https://www.cde.ca.gov/ds/fd/ec/currentexpense.asp))
* [`P2D_County_Race_Ethnicity`](../data/P2D_County_Race_Ethnicity.xlsx): County population by total hispanic and non-hispanic race ([Add. Source](https://www.dof.ca.gov/Forecasting/Demographics/Projections/))
* [`CA_FIPS.xlsx`](../data/CA_FIPS.xlsx): US FIPS codes for the State of California ([Add. Source](https://www.nrcs.usda.gov/wps/portal/nrcs/detail/ca/home/?cid=nrcs143_013697))

---

### Data dictionaries

[`ca_final`] is our final dataframe after importing, cleaning and merging several datasets. We will list columns of interest below:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|cname|object|2017-19 SAT Scores in California by School|Name of county|
|year|object|2017-19 SAT Scores in California by School|The SAT test administration year: 2017-19|
|per_capita_personal_income|float|Personal income by County, Metro, and Other areas|Personal income per capita|
|enroll12|float|2017-19 SAT Scores in California by School|Enrollment of Grade 12|
|numtsttakr12|float|2017-19 SAT Scores in California by School|Number of test takers Grade 12|
|numerwbenchmark12|float|2017-19 SAT Scores in California by School|The number meeting the Evidence-based reading + writing (ERW) benchmark established by the College Board based on the New 2016 SAT test format as of Mar-2016 for Grade 12 (Adjusted in 2017-18)|
|pcterwbenchmark12|float|2017-19 SAT Scores in California by School|The % of students who met or exceeded the benchmark for Evidence-based reading + writing (ERW) test for Grade 12|
|nummathbenchmark12|float|2017-19 SAT Scores in California by School|The number meeting the benchmark established by the College Board based on the New 2016 SAT Math test format as of Mar-2016 for Grade 12 (Adjusted in 2017-18)|
|pctmathbenchmark12|float|2017-19 SAT Scores in California by School|The % of students who met or exceeded the benchmark for SAT Math test for Grade 12|
|totnumbothbenchmark12|float|2017-19 SAT Scores in California by School|The total number of students who met the benchmark of both Evidence-based reading + writing (ERW) and Math Grade 12|
|pctbothbenchmark12|float|2017-19 SAT Scores in California by School|he % of students who met the benchmark of both Evidence-based reading + writing (ERW) and Math Grade 12|
|current_exp_per_ada|float|2017-19 California current expense of education per average daily attendance by county|Current expense per ADA
|pct_eligible_frpm_k12|float|2017-19 California free or reduced price meals by school|The percent of students eligible for free meals. Free Meal Count (K-12) divided by Enrollment (K-12)
|american_indian_or_alaska_native|float|County population by total hispanic and non-hispanic race|American Indian, Alaska native (% of population)|
|asian|float|County population by total hispanic and non-hispanic race|Asian (% of population)|
|black|float|County population by total hispanic and non-hispanic race|Black (% of population)|
|hispanic|float|County population by total hispanic and non-hispanic race|% hispanic|Hispanics (% of population)|
|multiracial|float|County population by total hispanic and non-hispanic race|Multiracial (% of population)|
|hawaiian_pacific_islander|float|County population by total hispanic and non-hispanic race||Hawaiian, Pacific islander (% of population)|
|white|float|County population by total hispanic and non-hispanic race|White (% of population)|

---

### Findings

**Comparison between SAT and ACT**

The national SAT score averages are at around 1100-1120 for years 2017-19. The standard deviation of SAT scores range from around 90-100. Looking at data over the past few years, Californian students / candidates appear to be scoring below-average in the SAT.

On a separate note, the national ACT score averages are at around 21.50 for years 2017-19. The standard deviation of SAT scores range from around 2.0-2.1. Looking at data over the past few years, Californian students / candidates appear to be scoring better in the ACT.

*Why is this the case?*

* The ACT exam appears to be more popular in recent years although its popularity advantage has been largely eroded by 2019
* States that favour the ACT tend to lean Republican while states that favour the SAT tend to lean Democrat
* Although California does not make SAT or ACT tests mandatory for university admissions, the majority of students in California take SATs
* The regression plot (SAT scores vs. SAT participation rates) may indicate some form of selection bias given the negative correlation between both variables (i.e. A smaller group of high achieving students that take both tests are high scorers, hence inflating California's averages for the ACT)

**State-level**

Based on our analysis, we note candidates in California are scoring below-average in the SAT. Like most states, students in California tend to underperform in Math relative to Evidence-based reading and writing.

More attention should be paid towards students' mathematical standards, since the % of students meeting SAT math benchmarks is positively correlated to the % of students meeting overall SAT benchmarks. 

**County-level**

Within California, we see a number of counties consistently over/underperforming the state average. We will delve deeper into specific county demographics to find out the underlying cause of this phenomenom.

Counties can be grouped into different tiers:
* Counties consistently underperforming (Bottom 5), or counties appearing in the Bottom 5 at least once and show deteriorating SAT performance trends (i.e. Glenn, Colusa, Madera, Merced)
* Counties with deteriorating SAT performance trends (i.e. Del Norte, Imperial, Lassen, Monterey, Stanislaus, Tulare)
* Counties with acceptable performance / trends

We also looked at other dataset(s) such as free and reduced price meals, current education expenditure and demographics (i.e. personal income per capita and race) and how they correlate to overall SAT passing rates. Because every county is different, approaches may need to be tailored accordingly. 

*Our findings*

* High (but negative) correlations for % of Hispanics in the population with overall SAT performance (i.e. The higher the % of Hispanics in a given county, the lower the SAT passing rates)
* High (but negative) correlations for % of K-12 students eligible for free and reduced price meals in the population with overall SAT performance

*What surprised us*

* Weak correlations between current expenditure per average daily attendance (ADA) and overall SAT performance (%)

### Recommendations
We will address our problem statement using a top-down perspective

*State-level*

* More resources should be devoted to improving students/candidates' mathematical standards since it has a positive correlation with overall SAT scores
* There may be strong regional / political affiliations associated with ACT and SATs
* ACT and SAT scores are also inversely correlated with their respective participation rates, which may be due to selection bias (Lower participation rates indicate students participating tend to be higher-achieving students)

*County-level*

* Increase efforts to engage county administrators to identify systemic issues with more resources dedicated to counties such as Del Norte, Imperial, Lassen, Monterey, Stanislaus, Tulare
* It appears there is a relationship between % of students eligible for free and reduced price meals, median household income and race/ethnicities with overall SAT performance - which may be indicative of income inequality perpetuated by racial undertones
* Organising learning journeys, seminars or workshops for educators to learn best practices from states that have consistently performed above-average

*School-level*

* At a school level, we should be identifying students receiving free, reduced price meals to ensure they are not deprived of educational resources or conducive learning environments
