import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split



def analiz(message):
	df = pd.read_csv("spam.csv",encoding="latin-1")
	df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'],axis=1, inplace=True)
	df['label'] = df['class'].map({'ham':0,'spam':1})

	X = df['message']
	y = df['label']

	cv = CountVectorizer()
	X = cv.fit_transform(X)
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42)

	clf = MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)

	data = [message]
	vect = cv.transform(data).toarray()
	response =  clf.predict(vect)
	if response == 1:
		return True
	else:
		return False


def analizer(message,data):
	df = pd.DataFrame(data)
	# df.drop(['id', 'status', 'message','date'],axis=1, inplace=True)
	df.drop(['message', 'status'],axis=1, inplace=True)
	df = df.reindex(columns=['message','status'])
	df['status'] = df['status'].map({'ham':0,'spam':1})

	X = df[df['message'].notna()]
	y = df['status']

	cv = CountVectorizer()
	X = cv.fit_transform(X)
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42)

	clf = MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)

	# if request.method == 'POST':
	# message = request.args.get('message')
	# message = "Send my sms code"
	data = [message]
	vect = cv.transform(data).toarray()
	response =  clf.predict(vect)
	if response == 1:
		return True
	else:
		return False