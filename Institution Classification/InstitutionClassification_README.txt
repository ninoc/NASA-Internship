Hi ! Thanks for accessing my files. This document contains a bunch of information and explanation of how my code works. Please take the time to read over the NECESSARY PACKAGES & ITEMS and the ABOUT THE CODE sections. If you come across specific questions when running, please take a look at THE DETAILS section in case your questions has already been addressed there. Thanks !

——————————————————————————————————————————————————

NECESSARY PACKAGES & FILES
Import pandas before running this code.

The following files must be on your device for running my code:
- CarnegieMatchingFunction.py: This file contains all of the primary functions of this module.
- CarnegieClassification_Data.csv: This spreadsheet contains data from the Carnegie Classification of Institutions of Higher Education on US-based universities.
- Exceptions_3-22_3.csv: This spreadsheet contains data on institutions names that are not within CarnegieClassification_Data.csv.

——————————————————————————————————————————————————

ABOUT THE CODE
This collection of functions and files was developed over several months while working as a USRA intern at NASA HQ. It was built in response to NASA’s call to expand and improve the diversity of its pool of potential proposal reviewers. These functions facilitate data analysis for large collections of information on NASA proposals and reviewers to track their institutions. 
Its main functionality is, using information available from the Carnegie Institution and across the Internet, to organize institutions into categories. Institutions are matched to their research class and Minority Serving Institution class. The former consists of the following "types": 
- R1 = University with very high research activity
- R2 = University with high research activity
- 4Y = 4-year university
- G = Government-affiliated institution
- RC = Research center
- F = Foreign institution (academic or other)
- I = Industry company
- None = An individual, other
As for the MSI classification, this applies to only US-based universities that fall under one of the following categories:
- HBCU = Historically Black College or University
- BSI = Black Serving Institution
- HSI = Hispanic Serving Institution


