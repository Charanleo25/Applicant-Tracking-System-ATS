import docx2txt #library to read document i.e docx
import matplotlib.pyplot as plt #library to plot graph acording to match
# the below library is used for count match words from one file to another one  
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 

#reading resume
resume=docx2txt.process('Profile.docx')
#reading job discription
job_list=['job.docx','job2.docx','job3.docx','job4.docx','job5.docx']

#slicing the job discription names to output
job_name = [x[:-5] for x in job_list]
#storing job score
job_match=[]


def process(resume, job_desc,i):
      text=[resume, job_desc]
      cv=CountVectorizer()
      count_matrix=cv.fit_transform(text)
      match=round((cosine_similarity(count_matrix)[0][1])*100,2)
      job_match.append(match)

for i in range(0,len(job_list)):
      job_desc=docx2txt.process(job_list[i])
      process(resume, job_desc,i)
	
print('job  : score')

for i in range(0,len(job_list)):
      print(job_name[i],':',job_match[i])
