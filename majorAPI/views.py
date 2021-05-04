import joblib
import pandas as pd
import numpy
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
pd.set_option('display.max_columns', 100)

def home(request):
	return render(request,'index.html')
def result(request):
	return render(request,'output.html')
def screening(request):
	if request.method == 'GET':
		q9a=0
		q9b=0
		q9c=0
		q9d=0
		q9e=0
		q20a=0
		q20b=0
		q20c=0
		q20d=0
		q20e=0

		q1=request.GET.get('Q1')
		q2=request.GET.get('Q2')
		q3=request.GET.get('Q3')
		q4=request.GET.get('Q4')
		q5=request.GET.get('Q5')
		q6=request.GET.get('Q6')
		q7=request.GET.get('Q7')
		q8=request.GET.get('Q8')
		q9a=request.GET.get('Q9a')
		q9b=request.GET.get('Q9b')
		q9c=request.GET.get('Q9c')
		q9d=request.GET.get('Q9d')
		q9e=request.GET.get('Q9e')
		q10=request.GET.get('Q10')
		q11=request.GET.get('Q11')
		q12=request.GET.get('Q12')
		q13=request.GET.get('Q13')
		q14=request.GET.get('Q14')
		q15=request.GET.get('Q15')
		q16=request.GET.get('Q16')
		q17=request.GET.get('Q17')
		q18=request.GET.get('Q18')
		q19=request.GET.get('Q19')
		q20a=request.GET.get('Q20a')
		q20b=request.GET.get('Q20b')
		q20c=request.GET.get('Q20c')
		q20d=request.GET.get('Q20d')
		q20e=request.GET.get('Q20e')
		q21=request.GET.get('Q21')
		q22=request.GET.get('Q22')
		q23=request.GET.get('Q23')
		q24=request.GET.get('Q24')
		q25a=request.GET.get('Q25a')
		q25b=request.GET.get('Q25b')
		if q9a==None:
			q9a=0
		if q9b==None:
			q9b=0
		if q9c==None:
			q9c=0
		if q9d==None:
			q9d=0
		if q9e==None:
			q9e=0

		if q20a==None:
			q20a=0
		if q20b==None:
			q20b=0
		if q20c==None:
			q20c=0
		if q20d==None:
			q20d=0
		if q20e==None:
			q20e=0

		# myDict = (request.GET).dict()
		# df=pd.DataFrame(myDict, index=[1])
		# df.insert(0, '', range(880, 880 + len(df)))
		# print(df.head())
		# df1 = pd.read_csv('survey.csv')
		# encoding(df)
		# preprocessin(df)
		# preprocessingg(df1)

		arry=numpy.array([[q1,q2,q3,q4,q5,q6,q7,q8,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q21,q22,q23,q24,q25a,q25b,q9a,q9b,q9c,q9d,q9e,q20a,q20b,q20c,q20d,q20e]])
		
		out_put=preprocessin(arry)
		output=out_put
		
		out_put_content=0
		out_put_content1="Your answers suggest you may not be suffering from depression. Still if you feel something isn’t quite right we recommend you schedule an appointment with your doctor. If you need help finding a mental health professional we suggest that you reach out to emergency mental health resources."
		out_put_content2="Your answers suggest you are suffering from mild depression. Consider watchful waiting, and testing again normally within two weeks. We additionally suggest it would be prudent to start a conversation with your doctor."
		out_put_content3="Your results indicate that you may be experiencing symptoms of moderate depression. Based on your answers, living with these symptoms could be causing difficulty managing relationships and even the tasks of everyday"
		out_put_content4=" You are experiencing symptoms of moderately severe depression. Based on your survey, these symptoms seem to be greatly affecting your lifestyle. It may be time to start a conversation with someone you trust.It is important that you schedule an appointment with your doctor or a mental health worker now.If you need any help finding a mental health professional we suggest that you reach out to emergency mental healthcare - (18002333330)."
		out_put_content5= "Your responses indicate that you may be at risk of harming yourself or someone else. If you are in need of immediate assistance, please call the National Suicide Prevention Hotline at 18002333330-TALK"
		if output=="1":
			out_put_content=out_put_content1
		if output=="2":
			out_put_content=out_put_content2
		if output=="3":
			out_put_content=out_put_content3
		if output=="4":
			out_put_content=out_put_content4
		if output=="5":
			out_put_content=out_put_content5

		contex={
			'q1':q1,		
			'q2':q2,
			'q3':q3,
			'q4':q4,
			'q5':q5,
			'q6':q6,
			'q7':q7,
			'q8':q8,
			'q9a':q9a,
			'q9b':q9b,
			'q9c':q9c,
			'q9d':q9d,
			'q9e':q9e,
			'q10':q10,
			'q11':q11,
			'q12':q12,
			'q13':q13,
			'q14':q14,
			'q15':q15,
			'q16':q16,
			'q17':q17,
			'q18':q18,
			'q19':q19,
			'q20a':q20a,
			'q20b':q20b,
			'q20c':q20c,
			'q20d':q20d,
			'q20e':q20e,
			'q21':q21,
			'q22':q22,
			'q23':q23,
			'q24':q24,
			'q25a':q25a,
			'q25b':q25b,
			'out_put':out_put,
			'output':output,
			'out_put_content':out_put_content,
			

			
		}
		# return render(request,'index-1.html',contex)
		if q1==None:
			return render(request,'index-1.html',contex)
		else:
			return render(request,'output.html',contex)
	
	#  def pridect
	# 	try:
	# 		mdl = joblib.load('dectree.ml')
	# 		scaler = joblib.load('scaler.save')
	# 		X=scalers.transform(unit)
	# 		y_pred=mdl.predict(X)
	# 		K.clear_session()
			
		# except ValueError as e:
		# 	return (e.args[0])
# def preprocessingg(df1):
# 	df1 = df1.drop(['Please write a very short summary of your lockdown experience in terms of your physical, mental, and emotional health.', "Editor's note: We hope you liked our questionnaire; Let us know how much.", "Unnamed: 29", "Unnamed: 32", "Unnamed: 0", "Remarks (section wise rating: I+ II+ III+ IV+ V)"], axis = 1)
# 	# using 2nd row as header
# 	df1.loc[0, 'Output Level (1-5)'] = "output"
# 	headers = df1.iloc[0]
# 	df1 = pd.DataFrame(df1.values[1:], columns=headers)
# 	df1["Q25a"].fillna("NA", inplace = True)
# 	df1["Q25b"].fillna("NA", inplace = True)
# 	print(df1.head(5))
# 	encoder = joblib.load('label_encoder.pkl')
# 	# encoder.classes_ = numpy.load('classes.npy')
# 	for col in df1.columns:
# 		if col not in ['Q9', 'Q20']:
# 			df1[col]= encoder.fit_transform(df1[col])
# 	print(df1.head)
# # def encoding(df):

# 	df['Q9(1)'] = 0
# 	df['Q9(2)'] = 0
# 	df['Q9(3)'] = 0
# 	df['Q9(4)'] = 0
# 	df['Q9(5)'] = 0
# 	items
# 	for i in range(len(items)):
# 		items[i] = items[i].strip()
# 	for item in items:
# 		if item=="Studying /being academically inclined": df.loc[index, 'Q9(1)'] = 1
# 		elif item=="Household chores": df.loc[index, 'Q9(2)'] = 1
# 		elif item=="Netflix or Other OTT": df.loc[index, 'Q9(3)'] = 1
# 		elif item=="Sleeping": df.loc[index, 'Q9(4)'] = 1
# 		else: df.loc[index, 'Q9(5)'] = 1
# 		df = df.drop(['Q9'], axis = 1)
	
	# df['Q20(1)'] = 0
	# df['Q20(2)'] = 0
	# df['Q20(3)'] = 0
	# df['Q20(4)'] = 0
	# df['Q20(5)'] = 0
	# for index, row in df:
	# 	items = row['Q20']
	# 	for i in range(len(items)):
	# 		items[i] = items[i].strip()
	# 	for item in items:
	# 		if item=="Moody": df.loc[index, 'Q20(1)'] = 1
	# 		elif item=="Satisfied": df.loc[index, 'Q20(2)'] = 1
	# 		elif item=="Happy": df.loc[index, 'Q20(3)'] = 1
	# 		elif item=="Sad": df.loc[index, 'Q20(4)'] = 1
	# 		else: df.loc[index, 'Q20(5)'] = 1

	# df = df.drop(['Q20'], axis = 1)	
def preprocessin (arry):
	try:
		model=joblib.load('dectree82.ml')
		scler = joblib.load('scaler.pkl')
		scler_output=scler.transform(arry)
		final_output=model.predict(scler_output)
		return final_output[0]
		

	except ValueError as e:
		return (e.args[0])

	# ans=scler_output[0]
	# print(ans)
# def pridecting(ans):
# 	try:s
		
# 	# print(final_output[0]
# 	print(ans)

	
		
		


# def result(request):
# 	return render(request,'output.html')