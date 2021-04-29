'''
This Program is for students who wanted to crack or check their ATS score before they 
apply and improvise there results in better way.
-------------------------------------------------------------------------------------
->Make sure you have installed docx2txt ,matplotlib, sklearn through pip.
->Make a Folder where it contains this program and below files.
1) Maintain one Resume file i.e Profile.docx (used in this program).
2) Have some Job description files i.e job.docx job2......(used in this program).
'''


import docx2txt #Library to read document i.e docx
import matplotlib.pyplot as plt #Library to plot graph acording to match
#The below 2 Library is used for counting the matched words from one file to another one
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 

#Reading Resume file
resume=docx2txt.process('Profile.docx')
#Reading Job discription file
job_list=['job.docx','job2.docx','job3.docx','job4.docx','job5.docx']

#Slicing the Job discription names to output at last(removing .docx on each file)
job_name = [x[:-5] for x in job_list]
#Storing Job Score
job_match=[]

#Function that automates the words matching into matrix format then  
#converting it into cosine similarity 
def process(resume, job_desc,i):
      #Storing all data of resume and job description to a list
      text=[resume, job_desc]
      #Vectorizing count
      cv=CountVectorizer()
      count_matrix=cv.fit_transform(text)
      #You can UnComment below line to see how the data is shown in matrix format
      #print(cosine_similarity(count_matrix))
      #Rounding the percentage to 2 digits 
      match=round((cosine_similarity(count_matrix)[0][1])*100,2)
      #Storing all data in Order
      job_match.append(match)

#Loop to call process function 
for i in range(0,len(job_list)):
      #Reading current Job discription
      job_desc=docx2txt.process(job_list[i])
      #Each Job Description is being sending with one resume
      process(resume, job_desc,i)
	
print('Job Name  : Score')

#Loop to fetch and output job name and its score 
for i in range(0,len(job_list)):
      print(job_name[i],':',job_match[i])

#OutPut:
'''
Job Name  : Score
job : 40.99
job2 : 36.96
job3 : 41.75
job4 : 41.75
job5 : 40.57
'''
