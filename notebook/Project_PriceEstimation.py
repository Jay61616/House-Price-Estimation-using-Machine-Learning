# Name : Jaya Chandra Kadiveti

# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
import ipywidgets as widgets
from IPython.display import display

# Load data and select columns of interest
data = pd.read_csv('housePrice.csv')
X = data[['Elevator', 'Address', 'Warehouse', 'Parking', 'Room', 'Area']]
y = data['Price(USD)']

# Extract unique addresses from the 'Address' column
addresses = X['Address'].unique()

# Preprocess categorical features
ct = ColumnTransformer([('encoder', OneHotEncoder(), ['Address'])], remainder='passthrough')
X = ct.fit_transform(X)

# Train random forest regression model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Calculate mean squared error and R-squared of model
y_pred = rf_model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("R-squared:", r2)
print("Mean squared error:", mse)

# Plot distribution of price
sns.histplot(y, kde=False)
plt.xlabel('Price(USD)')
plt.ylabel('Frequency')
plt.title('Distribution of House Prices')
plt.show()

# Plot predicted vs actual prices
plt.scatter(y, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.show()

# Plot price distribution based on presence of elevator
sns.boxplot(x='Elevator', y='Price(USD)', data=data)
plt.xlabel('Elevator')
plt.ylabel('Price(USD)')
plt.title('Price Distribution Based on Presence of Elevator')
plt.show()

print("Estimate the price of house by its parameters")

# Define function to predict price based on user inputs
def predict_price(elevator, address, warehouse, parking, room, area):
    # Preprocess user inputs
    user_input = pd.DataFrame({
        'Elevator': [elevator],
        'Address': [address],
        'Warehouse': [warehouse],
        'Parking': [parking],
        'Room': [room],
        'Area': [area],
    })
    user_input = ct.transform(user_input)
    
    # Predict price using trained model
    price = rf_model.predict(user_input)[0]
    return price

# Define widgets for user input
elevator_widget = widgets.RadioButtons(options=['Yes', 'No'], description='Elevator:')
address_widget = widgets.Dropdown(options=addresses, description='Address:')
warehouse_widget = widgets.RadioButtons(options=['Yes', 'No'], description='Warehouse:')
parking_widget = widgets.RadioButtons(options=['Yes', 'No'], description='Parking:')
room_widget = widgets.IntSlider(min=1, max=10, value=3, description='Rooms:')
area_widget = widgets.IntSlider(min=10, max=1000, value=100, description='Area (sqm):')

# Define function to update predicted price based on user input
def update_price(change):
    price = predict_price(elevator_widget.value=='Yes', 
                          address_widget.value, 
                          warehouse_widget.value=='Yes', 
                          parking_widget.value=='Yes', 
                          room_widget.value, 
                          area_widget.value)
    price_label.value = f'Predicted price: ${price:,.0f}'

# Link widgets to update function
elevator_widget.observe(update_price, 'value')
address_widget.observe(update_price, 'value')
warehouse_widget.observe(update_price, 'value')
parking_widget.observe(update_price, 'value')
room_widget.observe(update_price, 'value')
area_widget.observe(update_price, 'value')

# Create layout for user input
input_widgets = widgets.VBox([elevator_widget, address_widget, warehouse_widget, parking_widget, room_widget, area_widget])

# Create label to display predicted price
price_label = widgets.Label(value='Predicted price: $0')

# Display widgets and predicted price
display(input_widgets, price_label)
