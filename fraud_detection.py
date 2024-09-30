import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class FraudDetection:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.model = RandomForestClassifier()

    def load_data(self):
        # Load the dataset (Replace with actual dataset)
        data = pd.read_csv(self.dataset_path)
        return data

    def preprocess_data(self, data):
        # Example: Removing unnecessary columns and dealing with missing data
        data = data.dropna()
        X = data.drop(columns=['is_fraud'])  # Features
        y = data['is_fraud']                # Target label
        return X, y

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate_model(self, y_test, predictions):
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model Accuracy: {accuracy * 100:.2f}%")

    def run(self):
        data = self.load_data()
        X, y = self.preprocess_data(data)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.train_model(X_train, y_train)
        predictions = self.predict(X_test)
        self.evaluate_model(y_test, predictions)
