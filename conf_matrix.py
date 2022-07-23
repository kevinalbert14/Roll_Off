import numpy as np
from sklearn.metrics import confusion_matrix

def conf_matrix(test, test_prediction):
      y_true = test
      y_prend = test_prediction
      y_pred_norm = []
      for y in y_prend:
            y_pred_norm.append(np.argmax(y))
      y_pred_norm = np.array(y_pred_norm)
      return confusion_matrix(y_true, y_pred_norm)