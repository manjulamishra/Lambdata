
# define basic utility functions
#checks if there is any nulls in the df
#returns True False


def no_null_check(df):
	"""
	checks if there is any nulls in the df
     returns True False
	"""
	return not any (df.isna().sum())



#Check if the dataframe is all numeric

def all_numeric(df):
	from pandas.api.dtypes import is_numeric_dtype
	return all(is_numeric_dtype(df[col]) for col in df)


#confusion matrix in a visualiation format
def confusion_matrix_viz(y_true, y_pred):
	matrix = confusion_matrix(y_true, y_pred)
	return sns.heatmap(matrix, annot=True, 
		fmt=",", linewidths=1, linecolor='grey', sqaure=True,
		xticklabels=['Predicted\nNo', 'Predicted\nYes'],
		yticklabels=['Actaul\nNo', 'Actaul\nYes'])



# three way split
def train_validation_test_split(
	X, y, train_size=0.8, val_size=0.1, test_size=0.1,
	random_state=None, shuffle=True):
	
	assert train_size + val_size + test_size == 1

	X_train_val, X_test, y_train_val, y_test = train_test_split(
		X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

	X_train, X_val, y_train, y_val = train_test_split(
		X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
		random_state=random_state, shuffle=shuffle)

	return X_train, X_val, X_test, y_train, y_val, y_test