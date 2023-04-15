'''
This .py file contains the function(s) used to analyze DAPR data for success percentages.
'''

def successPercent(rawData, institution_column, status_column):
    '''
    This function takes in an original data frame (rawData) with columns "lat", "long", "zip", "Organization", and "status". The function returns a new data frame (newData) with columns "Organization", "Selected Count", "Declined Count", "Total Submissions", and "Success Percent".
    
    rawData = A data frame containing selection status.
    institution_column = The title of the column with homogenized institution names (often 'Homogenized Institution Name')
    status_column = The title of the column with either "SELECTED" or "DECLINED" information (often 'status')
    '''
    import pandas as pd
    
    # STEP 1: Clean rawData
    rawData = rawData[rawData[status_column] != 'SUBMITTED']
    rawData = rawData[rawData[status_column] != 'SELECTABLE']
    rawData = rawData.reset_index(drop = True)
        
    # STEP 2: Group rawData
    groupData = rawData.groupby([institution_column, status_column]).count()

    groupedData = pd.DataFrame()
    groupedData[institution_column] = [str(row[0]) for row in groupData.index]
    groupedData['Status'] = [str(row[1]) for row in groupData.index]
    groupedData['Count'] = [row[0] for row in groupData.values]
    
    # STEP 2: Make newData and populate with Declined Count
    newData = pd.DataFrame()

    newData['Organization'] = ""
    newData['Declined Count'] = ""

    for i in range(len(groupedData[institution_column])):
        if groupedData['Status'][i] == 'DECLINED':
            declined = groupedData['Count'][i]
            org = groupedData[institution_column][i]
            row = pd.DataFrame.from_dict({'Organization': [org], 'Declined Count': [declined]})
            newData = pd.concat([newData, row])

    newData = newData.reset_index(drop = True)
    
    # STEP 3: Populate with Selected Count
    newData['Selected Count'] = ""

    for i in range(len(groupedData[institution_column])):
        org1 = groupedData[institution_column][i]
        for j in range(len(newData['Organization'])):
            org2 = newData['Organization'][j]
            if org1 == org2:
                if groupedData['Status'][i] == 'SELECTED':
                    selected = groupedData['Count'][i]
                    newData.at[j,'Selected Count'] = selected
                    
    newData['Selected Count'] = newData['Selected Count'].replace('',0)
    
    # STEP 4: Populate with Total Submissions and Success Percent
    newData['Total Submissions'] = ""
    newData['Success Percent'] = ""

    for i in range(len(newData['Organization'])):
        dec = newData['Declined Count'][i]
        sel = newData['Selected Count'][i]
        tot = dec + sel
        percent = sel/tot * 100
        newData.at[i, 'Total Submissions'] = tot
        newData.at[i, 'Success Percent'] = percent
    
    # STEP 5: Reorder
    newData = newData[['Organization', 
                       'Declined Count', 
                       'Selected Count', 
                       'Total Submissions', 
                       'Success Percent']]

        
    # STEP 6: Return the spreadsheet 
    return newData

##################################################################################################################################

def successPercent_withCarnegieClass(rawData, institution_column, status_column):
    '''
    This function takes in an original data frame (rawData) and returns a new data frame (newData) with columns "Organization", "MSI Classification", "Research Classification", "Selected Count", "Declined Count", "Total Submissions", and "Success Percent".
    
    rawData = A data frame containing selection status.
    institution_column = The title of the column with homogenized institution names (often 'Homogenized Institution Name')
    status_column = The title of the column with either "SELECTED" or "DECLINED" information (often 'status')
    '''
    import pandas as pd
    
    # STEP 1: Clean rawData
    rawData = rawData[rawData[status_column] != 'SUBMITTED']
    rawData = rawData[rawData[status_column] != 'SELECTABLE']
    rawData = rawData.reset_index(drop = True)
        
    # STEP 2: Group rawData
    groupData = rawData.groupby([institution_column, status_column, 'MSI Classification', 'Research Classification']).count()

    groupedData = pd.DataFrame()
    groupedData[institution_column] = [str(row[0]) for row in groupData.index]
    groupedData['Status'] = [str(row[1]) for row in groupData.index]
    groupedData['MSI Classification'] = [str(row[2]) for row in groupData.index]
    groupedData['Research Classification'] = [str(row[3]) for row in groupData.index]
    groupedData['Count'] = [row[0] for row in groupData.values]
    
    # STEP 2: Make newData and populate with Declined Count
    newData = pd.DataFrame()

    newData['Organization'] = ""
    newData['MSI Classification'] = ""
    newData['Research Classification'] = ""
    newData['Declined Count'] = ""

    for i in range(len(groupedData[institution_column])):
        if groupedData['Status'][i] == 'DECLINED':

            declined = groupedData['Count'][i]
            org = groupedData[institution_column][i]
            msi = groupedData['MSI Classification'][i]
            rc = groupedData['Research Classification'][i]

            row = pd.DataFrame.from_dict({'Organization': [org], 
                                          'Declined Count': [declined], 
                                          'MSI Classification': [msi], 
                                          'Research Classification': [rc]})
            newData = pd.concat([newData, row])

    newData = newData.reset_index(drop = True)
    
    # STEP 3: Populate with Selected Count
    newData['Selected Count'] = ""

    for i in range(len(groupedData[institution_column])):
        org1 = groupedData[institution_column][i]

        for j in range(len(newData['Organization'])):
            org2 = newData['Organization'][j]

            if org1 == org2:
                if groupedData['Status'][i] == 'SELECTED':
                    selected = groupedData['Count'][i]
                    newData.at[j,'Selected Count'] = selected

    newData['Selected Count'] = newData['Selected Count'].replace('',0)
    
    # STEP 4: Populate with Total Submissions and Success Percent
    newData['Total Submissions'] = ""
    newData['Success Percent'] = ""

    for i in range(len(newData['Organization'])):
        dec = newData['Declined Count'][i]
        sel = newData['Selected Count'][i]
        tot = dec + sel
        percent = sel/tot * 100
        newData.at[i, 'Total Submissions'] = tot
        newData.at[i, 'Success Percent'] = percent
    
    # STEP 5: Reorder
    newData = newData[['Organization',
                       'MSI Classification', 
                       'Research Classification', 
                       'Declined Count', 
                       'Selected Count', 
                       'Total Submissions', 
                       'Success Percent']]

    # STEP 6: Return the spreadsheet 
    return newData

######################################################################################################################################################################################################################################################################################################################################################################################################

def prepostData(preData, postData):
    '''
    This function takes in speadsheets with DAPR success percents pre and post DAPR, and returns a single spreadsheet.
    '''
    import pandas as pd
    
    allData = pd.DataFrame()
    allData['Organization'] = preData['Organization']
    allData['Pre-DAPR Declined Submissions'] = preData['Declined Count']
    allData['Pre-DAPR Selected Submissions'] = preData['Selected Count']
    allData['Pre-DAPR Total Submissions'] = preData['Total Submissions']
    allData['Pre-DAPR Success Percent'] = preData['Success Percent']
    
    allData['Post-DAPR Declined Submissions'] = ""
    allData['Post-DAPR Selected Submissions'] = ""
    allData['Post-DAPR Total Submissions'] = ""
    allData['Post-DAPR Success Percent'] = ""

    for i in range(len(allData['Organization'])):
        org1 = allData['Organization'][i]
        for j in range(len(postData['Organization'])):
            org2 = postData['Organization'][j]
            dec = postData['Declined Count'][j]
            sel = postData['Selected Count'][j]
            tot = postData['Total Submissions'][j]
            percent = postData['Success Percent'][j]
            if org1 == org2:
                allData.at[i, 'Post-DAPR Declined Submissions'] = dec
                allData.at[i, 'Post-DAPR Selected Submissions'] = sel
                allData.at[i, 'Post-DAPR Total Submissions'] = tot
                allData.at[i, 'Post-DAPR Success Percent'] = percent
                
    for i in range(len(postData['Organization'])):
        org1 = postData['Organization'][i]
        if org1 not in allData['Organization'].unique():
            row = pd.DataFrame.from_dict({'Organization':[org1], 
                                          'Pre-DAPR Declined Submissions':[""],
                                          'Pre-DAPR Selected Submissions':[""],
                                          'Pre-DAPR Total Submissions':[""],
                                          'Pre-DAPR Success Percent':[""],
                                          'Post-DAPR Declined Submissions':[postData['Declined Count'][i]],
                                          'Post-DAPR Selected Submissions':[postData['Selected Count'][i]],
                                          'Post-DAPR Total Submissions':[postData['Total Submissions'][i]],
                                          'Post-DAPR Success Percent':[postData['Success Percent'][i]]})
            allData = pd.concat([allData, row])
    
    allData = allData.replace('','No information')
    allData = allData.reset_index(drop = True)
    
    return allData

##################################################################################################################################

def prepostData_withCarnegieClass(preData, postData):
    '''
    This function takes in speadsheets with DAPR success percents pre and post DAPR, and returns a single spreadsheet, including MSI and research classifications of each organization.
    '''
    import pandas as pd
    
    allData = pd.DataFrame()
    allData['Organization'] = preData['Organization']
    allData['MSI Classification'] = preData['MSI Classification']
    allData['Research Classification'] = preData['Research Classification']
    allData['Pre-DAPR Declined Submissions'] = preData['Declined Count']
    allData['Pre-DAPR Selected Submissions'] = preData['Selected Count']
    allData['Pre-DAPR Total Submissions'] = preData['Total Submissions']
    allData['Pre-DAPR Success Percent'] = preData['Success Percent']
    
    allData['Post-DAPR Declined Submissions'] = ""
    allData['Post-DAPR Selected Submissions'] = ""
    allData['Post-DAPR Total Submissions'] = ""
    allData['Post-DAPR Success Percent'] = ""

    
    
    for i in range(len(allData['Organization'])):
        org1 = allData['Organization'][i]
        
        for j in range(len(postData['Organization'])):
            org2 = postData['Organization'][j]
            dec = postData['Declined Count'][j]
            sel = postData['Selected Count'][j]
            tot = postData['Total Submissions'][j]
            percent = postData['Success Percent'][j]
            
            if org1 == org2:
                allData.at[i, 'Post-DAPR Declined Submissions'] = dec
                allData.at[i, 'Post-DAPR Selected Submissions'] = sel
                allData.at[i, 'Post-DAPR Total Submissions'] = tot
                allData.at[i, 'Post-DAPR Success Percent'] = percent
                
                
                
    for i in range(len(postData['Organization'])):
        org1 = postData['Organization'][i]
        
        if org1 not in allData['Organization'].unique():
            row = pd.DataFrame.from_dict({'Organization':[org1], 
                                          'MSI Classification':[""], 
                                          'Research Classification':[""],
                                          'Pre-DAPR Declined Submissions':[""],
                                          'Pre-DAPR Selected Submissions':[""],
                                          'Pre-DAPR Total Submissions':[""],
                                          'Pre-DAPR Success Percent':[""],
                                          'Post-DAPR Declined Submissions':[postData['Declined Count'][i]],
                                          'Post-DAPR Selected Submissions':[postData['Selected Count'][i]],
                                          'Post-DAPR Total Submissions':[postData['Total Submissions'][i]],
                                          'Post-DAPR Success Percent':[postData['Success Percent'][i]]})
            allData = pd.concat([allData, row])
    
    allData = allData.replace('','No information')
    allData = allData.reset_index(drop = True)
    
    return allData