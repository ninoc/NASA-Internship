import pandas as pd

##################################################################################################################################

def CarnegieMatching_OneSpreadsheet(inputData, institution_column, carnegieData, exceptionsData):
    '''
    This function determines the Carnegie and MSI classification of an institution and collects information on exceptions for later use.
    
    inputData = A data frame containing a list of instiutions to be classified (Must have a column titled 'Institution Name')
    institution_column = The name of the column within inputData that contains information on institution name (string)
    carnegieData = A data frame containing Carnegie Classifications for all US institutions ('CarnegieClassification_Data.csv')
    exceptionsData = A data frame containing a list of erroneous institution names with their correct Carnegie classification names ('Exception_zipcodes_Carnegie.csv)
    
    NOTE: This function's output, 'outputDf', is the same spreadsheet as inputData, only with two new columns: 'MSI Classification' and 'Research Classification'.
    '''
    # Remove exceptions nan
    exceptionsData = exceptionsData.fillna('None')
    
    # Make exceptions into a dictionary
    exceptionsDict = {'Exception Name':list(exceptionsData['Exception Name']), 
                  'GeoPy Sub':list(exceptionsData['GeoPy Sub']),
                  'Carnegie Name':list(exceptionsData['Carnegie Name']), 
                  'MSI Classification':list(exceptionsData['MSI Classification']), 
                  'Research Classification': list(exceptionsData['Research Classification'])}
    
    # Pull out Carnegie institution data
    carnegieInsts = list(carnegieData['name'])
    
    # Pull out input institution data
    inputInsts = list(inputData[institution_column])
    
    print('STEPS 1-3 COMPLETE')
    
    # Make output columns to store new data
    inputData['MSI Classification'] = ''
    inputData['Research Classification'] = ''
    
    print('STEP 4 COMPLETE')
    
    # Start matching
    for i in range(len(inputInsts)):
        inst1 = inputInsts[i]
        # If the institution is in the Carnegie spreadsheet...
        if inst1 in carnegieInsts:
            ### Gather all of the data and put it in the output dictionary
            ###outputDict['Institution Name'].append(inst1)
            c_index = carnegieInsts.index(inst1)

            research_class = ResearchClassFinder(c_index, carnegieData)
            ###outputDict['Research Classification'].append(research_class)

            msi_class = MSIClassFinder(c_index, carnegieData)[3]
            ##outputDict['MSI Classification'].append(msi_class)
            
            # Add class data to the two new columns
            inputData.at[i, 'MSI Classification'] = msi_class
            inputData.at[i, 'Research Classification'] = research_class
        else:
            # If the institution name (inst1) isn't in the Carnegie spreadsheet but happens to be in the exceptions list...
            if inst1 in exceptionsDict['Exception Name']:
                # Find the index of the bad institution name in the exceptions list
                e_index = exceptionsDict['Exception Name'].index(inst1)
                # Find the carnegie name associated with the bad name in the exceptions list
                c_inst = exceptionsDict['Carnegie Name'][e_index]
                ### Add the good name to the outputDict
                ###outputDict['Institution Name'].append(c_inst)

                try:
                    # Find the index of the carnegie name in the big carnegie spreadsheet
                    c_index = carnegieInsts.index(c_inst)

                    # Find the research class of the carnegie name based on its index in the big spreadsheet
                    research_class = ResearchClassFinder(c_index, carnegieData)
                    ###outputDict['Research Classification'].append(research_class)

                    # Find the MSI class of the carnegie name based on its index in the big spreadsheet
                    msi_class = MSIClassFinder(c_index, carnegieData)[3]
                    ###outputDict['MSI Classification'].append(msi_class)
                    
                    # Add class data to the two new columns
                    inputData.at[i, 'MSI Classification'] = msi_class
                    inputData.at[i, 'Research Classification'] = research_class
                except:
                    # Find the research and MSI class based on the exceptions spreadsheet
                    research_class = exceptionsDict['Research Classification'][e_index]
                    ###outputDict['Research Classification'].append(research_class)

                    msi_class = exceptionsDict['MSI Classification'][e_index]
                    ###outputDict['MSI Classification'].append(msi_class)

                    # Add class data to the two new columns
                    inputData.at[i, 'MSI Classification'] = msi_class
                    inputData.at[i, 'Research Classification'] = research_class
            # If the institution name isn't in the exceptions list yet...
            else:
                # Get the Carnegie name from the user
                c_inst = input(f'The institution "{inst1}" was not found in our references. Please input the name we should search for instead:')

                # If their input is in the big carnegie spreadsheet...
                if c_inst in carnegieInsts:
                    ### Add this information to the output dict
                    ###outputDict['Institution Name'].append(c_inst)
                    c_index = carnegieInsts.index(c_inst)

                    research_class = ResearchClassFinder(c_index, carnegieData)
                    ###outputDict['Research Classification'].append(research_class)

                    msi_class = MSIClassFinder(c_index, carnegieData)[3]
                    ###outputDict['MSI Classification'].append(msi_class)
                    
                    # Add class data to the two new columns
                    inputData.at[i, 'MSI Classification'] = msi_class
                    inputData.at[i, 'Research Classification'] = research_class

                    # And add it to the exceptions list
                    exceptionsDict['Exception Name'].append(inst1)
                    exceptionsDict['Carnegie Name'].append(c_inst)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)

                # If their input is in the exceptions spreadsheet already...
                elif c_inst in exceptionsDict['Exception Name']:
                    e_index = exceptionsDict['Exception Name'].index(c_inst)
                    
                    # Grab the correct name
                    c_name = exceptionsDict['Carnegie Name'][e_index]

                    # Find the research and MSI class based on the exceptions spreadsheet
                    # And add to the output
                    research_class = exceptionsDict['Research Classification'][e_index]
                    ###outputDict['Research Classification'].append(research_class)

                    msi_class = exceptionsDict['MSI Classification'][e_index]
                    ###outputDict['MSI Classification'].append(msi_class)
                    
                    # Add class data to the two new columns
                    inputData.at[i, 'MSI Classification'] = msi_class
                    inputData.at[i, 'Research Classification'] = research_class
                    
                    # Append the new exception to the exceptions spreadsheet
                    exceptionsDict['Exception Name'].append(inst1)
                    exceptionsDict['Carnegie Name'].append(c_name)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)

                # If neither...
                else:
                    # Gather info
                    other_inst = input(f'Your input "{c_inst}" was not found in the Carnegie database. Your input may not qualify as a degree-granting institution.\
 Please type the name of your institution.\n')
                    research_class = input(f'What is the research classification of this institution ? (R1, R2, 4Y, G, RC, F, I)\n')
                    msi_class = input(f'What is the MSI classification of this institution ? (HSI, BSI, HBCU, or None ?)')

                    ### Append to output dict
                    ###outputDict['Institution Name'].append(other_inst)
                    ###outputDict['Research Classification'].append(research_class)
                    ###outputDict['MSI Classification'].append(msi_class)

                    # Add class data to the two new columns
                    inputData.at[i, 'MSI Classification'] = msi_class
                    inputData.at[i, 'Research Classification'] = research_class
                    
                    # Append to exceptions dict for future use
                    exceptionsDict['Exception Name'].append(inst1)
                    exceptionsDict['Carnegie Name'].append(other_inst)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)

                    exceptionsDict['Exception Name'].append(c_inst)
                    exceptionsDict['Carnegie Name'].append(other_inst)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)
    
    print('STEP 5 COMPLETE')
    
    # Even out column lengths in the exceptions 
    nones = ['None'] * (len(exceptionsDict['Exception Name']) - len(exceptionsDict['GeoPy Sub']))
    for item in nones:
        exceptionsDict['GeoPy Sub'].append(item)
        
    ### Even out column lengths in the output
    ###nones = ['None'] * (len(outputDict['Research Classification']) - len(outputDict['Institution Name']))
    ###for item in nones:
        ###outputDict['Institution Name'].append(item)
    
    # Turn dictionaries into data frames
    ###outputDf = pd.DataFrame(outputDict)
    exceptionsDf = pd.DataFrame(exceptionsDict)
    
    outputDf = inputData
    
    # Return 
    return outputDf, exceptionsDf

##################################################################################################################################

def MAINCarnegieMatching(inputData, institution_column, carnegieData, exceptionsData):
    '''
    This function is the main function in this file. It takes in a spreadsheet containing various institution names and returns a spreadsheet containing MSI and Research classifications for each institution based on the Carnegie Classification database. It incorporates user inputs to address any exceptions.
    
    inputData = A data frame containing a list of instiutions to be classified (Must have a column titled 'Institution Name')
    institution_column = The name of the column within inputData that contains information on institution name (string)
    carnegieData = A data frame containing Carnegie Classifications for all US institutions ('CarnegieClassification_Data.csv')
    exceptionsData = A data frame containing a list of erroneous institution names with their correct Carnegie classification names ('Exception_zipcodes_Carnegie.csv', 'Exceptions_2-16.csv', etc.)
    '''
    # Run the exception matching function the first time:
    outputDf_temp, exceptionsDf = CarnegieExceptionsMatching(inputData, institution_column, carnegieData, exceptionsData)
    
    # Re-run to address any mis-matches in outputDf:
    outputDf, exceptionsDf_temp = CarnegieExceptionsMatching(inputData, institution_column, carnegieData, exceptionsData)
    
    # Return the appropriate files:
    return outputDf, exceptionsDf

##################################################################################################################################

def CarnegieExceptionsMatching(inputData, institution_column, carnegieData, exceptionsData):
    '''
    This function determines the Carnegie and MSI classification of an institution and collects information on exceptions for later use.
    
    inputData = A data frame containing a list of instiutions to be classified (Must have a column titled 'Institution Name')
    institution_column = The name of the column within inputData that contains information on institution name (string)
    carnegieData = A data frame containing Carnegie Classifications for all US institutions ('CarnegieClassification_Data.csv')
    exceptionsData = A data frame containing a list of erroneous institution names with their correct Carnegie classification names ('Exception_zipcodes_Carnegie.csv)
    '''
    # Remove Nan
    exceptionsData = exceptionsData.fillna('None')
    
    # Make into a dictionary
    exceptionsDict = {'Exception Name':list(exceptionsData['Exception Name']), 
                  'GeoPy Sub':list(exceptionsData['GeoPy Sub']),
                  'Carnegie Name':list(exceptionsData['Carnegie Name']), 
                  'MSI Classification':list(exceptionsData['MSI Classification']), 
                  'Research Classification': list(exceptionsData['Research Classification'])}
    
    # Pull out institution data
    inputInsts = list(inputData[institution_column])
    carnegieInsts = list(carnegieData['name'])
    
    # Make output dictionary to store new data
    outputDict = {'Institution Name':[], 'MSI Classification':[], 'Research Classification':[]}
    
    # Start matching
    for inst1 in inputInsts:
        # If the institution is in the Carnegie spreadsheet...
        if inst1 in carnegieInsts:
            # Gather all of the data and put it in the output dictionary
            outputDict['Institution Name'].append(inst1)

            index = carnegieInsts.index(inst1)

            research_class = ResearchClassFinder(index, carnegieData)
            outputDict['Research Classification'].append(research_class)

            msi_class = MSIClassFinder(index, carnegieData)[3]
            outputDict['MSI Classification'].append(msi_class)
        else:
            # If the institution name (inst1) isnt' in the Carnegie spreadsheet but happens to be in the exceptions list...
            if inst1 in exceptionsDict['Exception Name']:
                # Find the index of the bad institution name in the exceptions list
                index1 = exceptionsDict['Exception Name'].index(inst1)
                # Find the carnegie name associated with the bad name in the exceptions list
                c_inst = exceptionsDict['Carnegie Name'][index1]
                # Add the good name to the outputDict
                outputDict['Institution Name'].append(c_inst)

                try:
                    # Find the index of the carnegie name in the big carnegie spreadsheet
                    index2 = carnegieInsts.index(c_inst)

                    # Find the research class of the carnegie name based on its index in the big spreadsheet
                    research_class = ResearchClassFinder(index2, carnegieData)
                    outputDict['Research Classification'].append(research_class)

                    # Find the MSI class of the carnegie name based on its index in the big spreadsheet
                    msi_class = MSIClassFinder(index2, carnegieData)[3]
                    outputDict['MSI Classification'].append(msi_class)
                except:
                    # Find the research and MSI class based on the exceptions spreadsheet
                    research_class = exceptionsDict['Research Classification'][index1]
                    outputDict['Research Classification'].append(research_class)

                    msi_class = exceptionsDict['MSI Classification'][index1]
                    outputDict['MSI Classification'].append(msi_class)

            # If the instiuttion name isn't in the exceptions list yet...
            else:
                # Get the Carnegie name from the user
                c_inst = input(f'The institution "{inst1}" was not found in our references. Please input the name we should search for instead:')

                # If their input is in the big carnegie spreadsheet...
                if c_inst in carnegieInsts:
                    # Add this information to the output dict
                    outputDict['Institution Name'].append(c_inst)

                    index = carnegieInsts.index(c_inst)

                    research_class = ResearchClassFinder(index, carnegieData)
                    outputDict['Research Classification'].append(research_class)

                    msi_class = MSIClassFinder(index, carnegieData)[3]
                    outputDict['MSI Classification'].append(msi_class)

                    # And add it to the exceptions list
                    exceptionsDict['Exception Name'].append(inst1)
                    exceptionsDict['Carnegie Name'].append(c_inst)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)

                # If their input is in the exceptions spreadsheet already...
                elif c_inst in exceptionsDict['Exception Name']:
                    index = exceptionsDict['Exception Name'].index(c_inst)
                    
                    # Grab the correct name
                    c_name = exceptionsDict['Carnegie Name'][index]

                    # Find the research and MSI class based on the exceptions spreadsheet
                    # And add to the output
                    research_class = exceptionsDict['Research Classification'][index]
                    outputDict['Research Classification'].append(research_class)

                    msi_class = exceptionsDict['MSI Classification'][index]
                    outputDict['MSI Classification'].append(msi_class)
                    
                    # Append the new exception to the exceptions spreadsheet
                    exceptionsDict['Exception Name'].append(inst1)
                    exceptionsDict['Carnegie Name'].append(c_name)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)

                # If neither...
                else:
                    # Gather info
                    other_inst = input(f'Your input "{c_inst}" was not found in the Carnegie database. Your input may not qualify as a degree-granting institution. Please type the name of your institution.')
                    research_class = input(f'What is the research classification of this institution ? (R1, R2, 4Y, G, RC, F, I)')
                    msi_class = input(f'What is the MSI classification of this institution ? (HSI, BSI, HBCU, or None ?)')

                    # Append to output dict
                    outputDict['Institution Name'].append(other_inst)
                    outputDict['Research Classification'].append(research_class)
                    outputDict['MSI Classification'].append(msi_class)

                    # Append to exceptions dict for future use
                    exceptionsDict['Exception Name'].append(inst1)
                    exceptionsDict['Carnegie Name'].append(other_inst)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)

                    exceptionsDict['Exception Name'].append(c_inst)
                    exceptionsDict['Carnegie Name'].append(other_inst)
                    exceptionsDict['MSI Classification'].append(msi_class)
                    exceptionsDict['Research Classification'].append(research_class)
    
    # Even out column lengths in the exceptions 
    nones = ['None'] * (len(exceptionsDict['Exception Name']) - len(exceptionsDict['GeoPy Sub']))
    for item in nones:
        exceptionsDict['GeoPy Sub'].append(item)
        
    # Even out column lengths in the output
    nones = ['None'] * (len(outputDict['Research Classification']) - len(outputDict['Institution Name']))
    for item in nones:
        outputDict['Institution Name'].append(item)
    
    # Turn dictionaries into data frames
    outputDf = pd.DataFrame(outputDict)
    exceptionsDf = pd.DataFrame(exceptionsDict)
    
    # Return the outputDict and the exceptionsDict
    return outputDf, exceptionsDf

##################################################################################################################################

def ResearchClassFinder(index, carnegieInfo):
    '''
    This function determines the Carnegie research classification (4Y, R2, R1, etc.) of an institution.
    
    index = The index of the institution in the Carnegie reference file 'CarnegieClassification_Data.csv' (int)
    '''
    # Create reference dictionary
    classDict = {14: '4Y', 
                 15: 'R1', 
                 16: 'R2', 
                 17: 'R2 - 17', 
                 18: 'R2 - 18', 
                 19: 'R2 - 19', 
                 20: 'R2 - 20', 
                 21: '4Y', 
                 22: '4Y', 
                 23: '4Y', 
                 33: 'TC'}
    
    # Find number associated with research class
    research_class_num = carnegieInfo['basic2021'][index]
    
    # Find descriptor associated with number
    try:
        research_class = classDict[research_class_num]
    except:
        if 9 < research_class_num < 13:
            research_class = 'SF'
        elif 0 < research_class_num < 10:
            research_class = '2Y'
        elif research_class_num == -2:
            research_class = 'N/A'
        elif 23 < research_class_num < 33:
            research_class = '4Y'
            
    return research_class

##################################################################################################################################

def MSIClassFinder(index, carnegieInfo):
    '''
    This function determines the MSI classification of an institution based on the Carnegie classification database.
    
    index = The index of the institution in the Carnegie reference file 'CarnegieClassification_Data.csv' (int)
    '''
    hbcu = carnegieInfo['hbcu'][index]
    if hbcu == 1:
        hbcu_class = 'Yes'
        #newCarnegieDict['HBCU'].append(hbcu_class)
    else:
        hbcu_class = 'No'
        #newCarnegieDict['HBCU'].append(hbcu_class)

    tribal = carnegieInfo['tribal'][index]
    if tribal == 1:
        tribal_class = 'Yes'
        #newCarnegieDict['Tribal College'].append(tribal_class)
    else:
        tribal_class = 'No'
        #newCarnegieDict['Tribal College'].append(tribal_class)

    hsi = carnegieInfo['hsi'][index]
    if hsi == 1:
        hsi_class = 'Yes'
        #newCarnegieDict['HSI'].append(hsi_class)
    else:
        hsi_class = 'No'
        #newCarnegieDict['HSI'].append(hsi_class)

    msi = carnegieInfo['msi'][index]
    if msi == 1:
        if hbcu_class == 'Yes':
            msi_class = 'HBCU'
            #newCarnegieDict['MSI Classification'].append(msi_class)
        elif tribal_class == 'Yes':
            msi_class = 'TC'
            #newCarnegieDict['MSI Classification'].append(msi_class)
        elif hsi_class == 'Yes':
            msi_class = 'HSI'
            #newCarnegieDict['MSI Classification'].append(msi_class)
        else:
            msi_class = 'Undefined'
            #newCarnegieDict['MSI Classification'].append(msi_class)
    else:
        msi_class = 'None'
        #newCarnegieDict['MSI Classification'].append(msi_class)
        
    return hbcu_class, tribal_class, hsi_class, msi_class

##################################################################################################################################

def CarnegieSearcher(instsList, carnegieInfo, exceptionsFile):
    '''
    This function determines the Carnegie research and MSI classification of a list of institutions. 
    
    instsList = a list of all of the institutions to be searched
    carnegieInfo = a data frame containing the most up-to-date Carnegie classifications for universities ('CarnegieClassification_Data.csv')
    exceptionsFile = a data frame containing multiple variations of a university name with their associated name in the carnegieFile ('Exception_zipcodes_Carnegie.csv')
    
    Returns:
    newCarnegieDf = a data frame with each university's name and their Carnegie and MSI classification
    outCarnegieList = a list of names that did not appear in the Carnegie database nor in the exceptions file
    '''
    
    exceptionsName = list(exceptionsFile['Exception Name'])
    exceptionsGeoPy = list(exceptionsFile['GeoPy Sub'])
    exceptionsCarnegie = list(exceptionsFile['Carnegie Name'])
        
    inCarnegieList = []
    outCarnegieList = []

    newCarnegieDict = {'Institution Name': [],
                       'HBCU': [], 
                       'Tribal College': [], 
                       'HSI': [],
                       'MSI Classification': [], 
                       'Research Classification': []}

    carnegieInsts = list(carnegieInfo['name'])
    for item in instsList:
        if item in carnegieInsts:
            index = carnegieInsts.index(item)
            inCarnegieList.append((item, index))

            inst = carnegieInfo['name'][index]
            newCarnegieDict['Institution Name'].append(inst)

            # Find research class
            research_class = ResearchClassFinder(index, carnegieInfo)
            newCarnegieDict['Research Classification'].append(research_class)

            # Find MSI class
            hbcu_class, tribal_class, hsi_class, msi_class = MSIClassFinder(index, carnegieInfo)
            newCarnegieDict['HBCU'].append(hbcu_class)
            newCarnegieDict['Tribal College'].append(tribal_class)
            newCarnegieDict['HSI'].append(hsi_class)
            newCarnegieDict['MSI Classification'].append(msi_class)

        else: 
            if item in exceptionsName:
                index1 = exceptionsName.index(item)
                
                # Find in exceptions csv
                inst = exceptionsCarnegie[index1]
                newCarnegieDict['Institution Name'].append(inst)
                
                # Find inst in main Carnegie list
                index2 = carnegieInsts.index(inst)

                # Find research class
                research_class = ResearchClassFinder(index2, carnegieInfo)
                newCarnegieDict['Research Classification'].append(research_class)

                # Find MSI class
                hbcu_class, tribal_class, hsi_class, msi_class = MSIClassFinder(index2, carnegieInfo)
                newCarnegieDict['HBCU'].append(hbcu_class)
                newCarnegieDict['Tribal College'].append(tribal_class)
                newCarnegieDict['HSI'].append(hsi_class)
                newCarnegieDict['MSI Classification'].append(msi_class)
            elif item in exceptionsGeoPy:
                index = exceptionsGeoPy.index(item)

                # Find in exceptions csv
                inst = exceptionsCarnegie[index1]
                newCarnegieDict['Institution Name'].append(inst)
                
                # Find inst in main Carnegie list
                index2 = carnegieInsts.index(inst)

                # Find research class
                research_class = ResearchClassFinder(index, carnegieInfo)
                newCarnegieDict['Research Classification'].append(research_class)

                # Find MSI class
                hbcu_class, tribal_class, hsi_class, msi_class = MSIClassFinder(index, carnegieInfo)
                newCarnegieDict['HBCU'].append(hbcu_class)
                newCarnegieDict['Tribal College'].append(tribal_class)
                newCarnegieDict['HSI'].append(hsi_class)
                newCarnegieDict['MSI Classification'].append(msi_class)
            else:
                outCarnegieList.append(item)
        
    newCarnegieDf = pd.DataFrame.from_dict(newCarnegieDict)
    
    return newCarnegieDf, outCarnegieList

##################################################################################################################################
