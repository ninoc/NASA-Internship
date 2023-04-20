Hi ! Thanks for accessing my files. This document contains a bunch of information and explanation of how my code works. Please take the time to read over the NECESSARY PACKAGES & ITEMS and the ABOUT THE CODE sections. If you come across specific questions when running, please take a look at THE DETAILS section in case your questions has already been addressed there. Thanks !

——————————————————————————————————————————————————

NECESSARY PACKAGES & FILES
Import the following packages...
- pandas
- folium
    - folium plugins
- json
- geopy.geocoders
    - geopy.geocoders Nominatim
PLEASE NOTE: Any user will need to create a Nominatim "user_agent" to align with their usage policy. Please see the following link for more information - https://geopy.readthedocs.io/en/stable/index.html?highlight=user_agent#nominatim.

The files below are required to run my map-making code...
- DepartmentMapMakingCode.py OR FacultyMapMakingCode.py: The file that is imported decides what institutional data is displayed on the map (Astronomy departments vs. astronomy faculty). Both files contain functions that are necessary for recreating the map contained in the file NHFPFellowsMap_Updated2022.html.
- FINAL_MSIR2Data.csv: This file contains information on the astronomy departments and faculty of the institutions displayed as pins on the final map.
- FellowshipTypeSplit_Updated2022.csv: This file contains information on the host institutions of NHFP fellows displayed as red circles on the final map.

The following files are optional...
- MapUtilties.py: Contains functions that were used to develop the two .csv files used to make the map.
- NHFPFellowsMap_Updated2022.html: The final version of the NHFP map made using my code. Download to view.


——————————————————————————————————————————————————

ABOUT THE CODE
This collection of functions and files was developed over several months while working as a USRA intern at NASA HQ. It was built in response to NASA’s call to expand and improve the diversity of its programs, specifically the NASA Hubble Fellowship Program in a 2021 review of the diversity and effectiveness of the fellowship. The visual nature of this map is meant to be a tool for past, current, and future NHFP fellows, as well as the people running the fellowship. 
"The Map" and its associated data sets were compiled using web scraping and surfing. The map itself displays the location of Minority Serving Institutions and R2 Universities in the US with either astronomy departments or at least 2 astronomy faculty. It also displays the NHFP Fellow alumni population at various host institutions in the US.

——————————————————————————————————————————————————

THE DETAILS
In this section, you will find a (relatively) detailed description of the purpose and functionality of the main function contained within the files "DepartmentMapMakingCode.py" and "FacultyMapMakingCode.py".
mapMaker(): This function takes in the necessary files to build the NHFP Map with surrounding institutions. Its inputs are as follows:
- FellowsFile = csv containing fellow information ('FellowshipTypeSplit_Updated2022.csv')
- MSIR2File = csv containing information on MSIs ('FINAL_MSIR2Data.csv')

To use this function, open a Jupyter notebook (or equivalent) and import the necessary files listed in the earlier section. Then, fill in the two inputs to mapMaker with the appropriate .csv files and save the resultant output to your device.

