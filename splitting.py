from sklearn.model_selection import train_test_split

def splitting_train_test(images_split, labels_int_split):
    #Splitting Train & Test
    X_train, X_need, Y_train, Y_need = train_test_split(images_split, labels_int_split, test_size=0.3, random_state=1)
    #Splitting Validation data from Test data
    X_val, X_test, Y_val, Y_test = train_test_split(X_need, Y_need, test_size=0.333, random_state=1)
    return X_train, Y_train,X_test,Y_test,X_val,Y_val