# finding out the mobile.no
import re
text = '''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern = r'\d\d\d\d\d\d\d\d\d\d'
matches = re.findall(pattern, text)
matches


text = '''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern = r'\d{10}'
matches = re.findall(pattern, text)
matches

# extracting the number.
pattern = r'\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, text)
matches

text = '''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern = r'\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, text)
matches

###########################################################################

# used the OR (|) operator
text1 = '''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches = re.findall(pattern, text1)
matches

#############################################################################
# want to remove the any charater like ; or - used the those symbool in sqaure bracket
text2 = 'A protracted; legal battle; over a 32-carat;Golconda diamond-'
pattern = '[^;-]'
matches = re.findall(pattern, text2)
matches

##########################################################################################

text3 = '''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
Reclassifications
Certain prior period balances have been reclassified to conform to the current period presentation in the accompanying notes.
Revenue Recognition
Revenue by source
The following table disaggregates our revenue by major source (in millions):'''

pattern = 'Note \d - [^\n]'
matches = re.findall(pattern, text3)
matches

#output-['Note 1 - S']

##############################################################################################

# OR

text3 = '''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
Reclassifications
Certain prior period balances have been reclassified to conform to the current period presentation in the accompanying notes.
Revenue Recognition
Revenue by source
The following table disaggregates our revenue by major source (in millions):'''

pattern = 'Note \d - [^\n]*'
matches = re.findall(pattern, text3)
matches

#Output-['Note 1 - Summary of Significant Accounting Policies']

#########################################################################################
