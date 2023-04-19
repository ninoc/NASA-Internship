Hi ! Thanks for accessing my files. This document contains a bunch of information and explanation of how my code works. Please take the time to read over the NECESSARY PACKAGES & ITEMS and the ABOUT THE CODE sections. If you come across specific questions when running, please take a look at THE DETAILS section in case your questions has already been addressed there. Thanks !

——————————————————————————————————————————————————

NECESSARY PACKAGES & FILES
Import pandas before running this code.

The following files must be on your device for running my code:
- CarnegieMatchingFunctions.py: This file contains all of the primary functions of this module.
- CarnegieClassification_Data.csv: This spreadsheet contains data from the Carnegie Classification of Institutions of Higher Education on US-based universities.
- Exceptions_3-22_3.csv: This spreadsheet contains data on institutions names that are not included in CarnegieClassification_Data.csv.

——————————————————————————————————————————————————

ABOUT THE CODE
This collection of functions and files was developed over several months while working as a USRA intern at NASA HQ. It was built in response to NASA’s call to expand and improve the diversity of its pool of potential proposal reviewers. These functions facilitate data analysis for large collections of information on NASA proposals and reviewers to track their affiliate institutions. 
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

——————————————————————————————————————————————————

THE DETAILS
In this section, I will highlight the main and component functions of this module and explain their functionalities, beginning with the central function of the package.

———————
CarnegieMatching_OneSpreadsheet(): This function is the main function of this module. It determines the research (Carnegie) classification and MSI classification of an institution via the Carnegie database, the exceptions spreadsheet, or via user input. 

This function has the following arguments...
inputData = A data frame containing institution names that we wish to identify (imported earlier).
institution_column = A string name of the column within inputData that contains information on institution names.
carnegieData = A data frame of the Carnegie classification database (imported earlier).
exceptionsData = A data frame of potential erroneous or missing names from the Carnegie database (imported earlier).

The function returns the following...
outputDf = A data frame identical to inputData, except with three additional columns: "Homogenized Institution Name", "Research Classification" and "MSI Classification".
exceptionsDf = A data frame identical to exceptionsData, except with additional columns containing new exceptions encountered when analyzing inputData.

In order for this function to return a complete list of MSI and research classifications for each institution, it may pause at certain institution names it does not recognize in neither the Carnegie database nor the exceptions spreadsheet. Sometimes, this is due to the fact that the institution is not a university or it has not been encountered in previous tests of this function. Or, it may have some sort of strange capitalization or spacing.
In any case, the user will be prompted to input another name for the erroneous institution that the code can search for again. You may need to manually search CarnegieClassification_Data or Exceptions_3-22_3.csv for the correct name. If the name is not in either of those spreadsheets, you will need to input the classification by hand. The code will prompt the user on how to do so.

In the last step of the function, the user will be prompted with a final question: "Would you like to automatically update and save your exceptions file ? (Yes/No)". It is highly encouraged to answer "Yes" to this question, as then the code will ask for your input in automatically saving your exceptions file as a .csv to your device. This adds a layer of security from any new exceptions being lost. If you respond "No", your exceptions file will still be returned from the function, but you will then need to save the file on your own.
———————
ResearchClassFinder(): This function is a component function to CarnegieMatching_OneSpreadsheet(). It determines the research (Carnegie) classification of an institution based on information in CarnegieClassification_Data.csv. It is not recommended to use this function alone.
———————
MSIClassFinder(): This function is a component function to CarnegieMatching_OneSpreadsheet(). It determines the MSI classification of an institution based on information in CarnegieClassification_Data.csv. It is not recommended to use this function alone.
———————
All of the remaining functions in the file CarnegieMatchingFunctions.py are previous (unused) generations of CarnegieMatching_OneSpreadsheet().

——————————————————————————————————————————————————

I would like to give special thanks to Antonino Cucchiara, my supervisor and guide at NASA, who offered invaluable guidance and input while I developed this code. I would also like to thank the great people at NASA HQ APD for their constant encouragement and support. Thank you to USRA and the internship coordinators for offering such a special opportunity to work at NASA HQ for almost a full year. This experience was life-changing. 

Please do not hesitate to contact me via GitHub with any comments, questions, concerns, or bugs. Happy coding !
