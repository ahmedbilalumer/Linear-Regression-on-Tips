import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
df_complete = pd.read_csv('tips.csv') 

# Split the data into training and testing sets
X = df_complete[['total_bill']]
y = df_complete['tip']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Define a function to predict the tip based on the total bill
def predict_tip(total_bill):
    input_data = pd.DataFrame({'total_bill': [total_bill]})
    return model.predict(input_data)[0]

# Bot interface
def tip_predictor_bot():
    while True:
        user_input = input("Enter the total bill amount (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            total_bill = float(user_input)
            predicted_tip = predict_tip(total_bill)
            print(f"The predicted tip for a total bill of {total_bill} is ${predicted_tip:.2f}")
        except ValueError:
            print("Please enter a valid number for the total bill amount.")

# Run the bot
tip_predictor_bot()
