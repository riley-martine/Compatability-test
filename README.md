[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d469de280d8d4364ae46169c58c6b9f6)](https://www.codacy.com/app/***REMOVED***/Compatability-test?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=riley-martine/Compatability-test&amp;utm_campaign=Badge_Grade)
# Compatability-test
Test for two people matching, using google spreadsheet/forms for data. 


-


Instructions: Make google form with questions/answers. Types of questions are 

single number (matches number a on question a to number b on question a, with deviation from number factored in),

pair (answer a to question a matches to answer b on question a),

and single (answer a on question a matches to answer a on question a).

Find the right place in the code to put the column numbers for these. You can configure the email part if you don't want to see the data yourself. 



To run: put run.sh and the .py file in the same directory and run the run.sh file.

You will have to edit the sh file to get the download url for your spreadsheet. 

May have to chmod +x run.sh:wq
