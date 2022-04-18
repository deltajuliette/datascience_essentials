# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Missing Data

---

## Materials We Provide


| Topic | Description | Link |
| --- | --- | --- |
| Slides | Slide Deck | [Link](./missing-data.pdf) |
| Lesson | Starter Code | [Link](./starter-code.ipynb)||

---

## Learning Objectives

*After this lesson, students will be able to:*

1. Define MCAR, MAR, and NMAR.
2. Describe various strategies for dealing with missing data.
3. Understand the assumptions we make when using strategies to handle missing data.

---

## Lesson Outline

I. Introduction to Missing Data

II. Strategies for doing data science with missing data

III. Practical considerations and warnings

---

## OPTIONAL: Resources for Practice and Learning

*For supplemental reading material on this topic, check out the following resources:*

#### Academic Content (roughly sorted from least technical to most)
- [Good summary of single vs. multiple imputation](https://scikit-learn.org/stable/modules/impute.html#multiple-vs-single-imputation)
- [UTexas Slides on Missing Data](https://liberalarts.utexas.edu/prc/_files/cs/Missing-Data.pdf)
- [Flexible Imputation of Missing Data, 2nd ed.](https://stefvanbuuren.name/fimd/)
- [Pattern Submodel Paper from "Biostatistics"](https://academic.oup.com/biostatistics/advance-article/doi/10.1093/biostatistics/kxy040/5092384)
- [The prevention and handling of missing data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668100/)
- [Should you use a missing data indicator?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3414599/)
- [Boston University Technical Report on Missing Data, Assumptions, and Applications](http://www.bu.edu/sph/files/2014/05/Marina-tech-report.pdf)
- [Andrew Gelman Chapter on Missing Data - thorough and very good, but academic](http://www.stat.columbia.edu/~gelman/arm/missing.pdf)

#### Python
- [Scikit-Learn Write-Up of Imputation](https://scikit-learn.org/stable/modules/impute.html)
- [Scikit-Learn SimpleImputer Class](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
- [Scikit-Learn IterativeImputer Class](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html) **note: this is experimental**
- [Scikit-Learn KNNImputer Class](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html)
- [Scikit-Learn Mean Imputation](http://scikit-learn.org/stable/auto_examples/plot_missing_values.html#sphx-glr-auto-examples-plot-missing-values-py)
- [MissingNo in Python](https://github.com/ResidentMario/missingno)
- [MissingNo Paper](http://joss.theoj.org/papers/52b4115d6c03864b884fbf3334851322)
- [KNNImputer or IterativeImputer](https://github.com/justmarkham/scikit-learn-tips/blob/master/notebooks/11_new_imputers.ipynb)
- [Adding a missing indicator](https://github.com/justmarkham/scikit-learn-tips/blob/master/notebooks/09_add_missing_indicator.ipynb)
- [Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-auto-examples-impute-plot-missing-values-py)

#### Rubin's Rules
- [Article about Rubin's Rules](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2727536/)
- [IBM Walkthrough of Rubin's Rules](https://www.ibm.com/support/knowledgecenter/de/SSLVMB_22.0.0/com.ibm.spss.statistics.algorithms/alg_mi-pooling_rubin_combine.htm)
- [R Code for Implementing Rubin's Rules](https://stefvanbuuren.name/mice/reference/pool.html)

#### Non-Statistical References
- [How One 19-Year-Old Illinois Man Is Distorting National Polling Averages - NYTimes](https://www.nytimes.com/2016/10/13/upshot/how-one-19-year-old-illinois-man-is-distorting-national-polling-averages.html)

---

### Authors
- Noelle Brown
- Matt Brems

