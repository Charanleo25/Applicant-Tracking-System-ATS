import docx2txt, matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
resume=docx2txt.process('CMA audit Profile (1).docx')
job_list=['job.docx','job2.docx','job3.docx','job4.docx','job5.docx','job6.docx','job7.docx','job8.docx','job9.docx','job10.docx','job11.docx','job12.docx']


job_name = [x[:-5] for x in job_list]
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
      

      

'''
for i in job_list:
      j=1
      job_desc=docx2txt.process(i)
      job=job_desc[i]
      #print(job_desc)
'''




'''
#imp
job_desc=docx2txt.process('job3.docx')
job_desc_2=docx2txt.process('job2.docx')
job_desc_3=docx2txt.process('job.docx')


text=[resume, job_desc]
text1=[resume, job_desc_2]
text2=[resume, job_desc_3]

cv=CountVectorizer()
count_matrix=cv.fit_transform(text)
count_matrix_1=cv.fit_transform(text1)
count_matrix_2=cv.fit_transform(text2)

print(cosine_similarity(count_matrix))
print(cosine_similarity(count_matrix_1))
print(cosine_similarity(count_matrix_2))


match=cosine_similarity(count_matrix)[0][1]
match=match*100
match=round(match,2)
print('job1:',match)

match1=cosine_similarity(count_matrix_1)[0][1]
match1=match1*100
match1=round(match1,2)
print('job2:',match1)

match2=cosine_similarity(count_matrix_2)[0][1]
match2=match2*100
match2=round(match2,2)
print('job3:',match2)
'''


'''
Ploting Graph
# defining labels
activities = ['High', 'Low']

# portion covered by each label
i=match/10
j=(100-match)/10
slices = [i,j]

# color for each label
colors = ['r', 'b']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
		startangle=90, shadow = True, explode = (0, 0),
		radius = 1.2, autopct = '%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()'''
