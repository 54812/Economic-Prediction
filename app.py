import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame to store economic events
events_data = pd.DataFrame(columns=['Date', 'Inflation'])

# Function to add economic event
def add_event(date, inflation_rate):
    global events_data
    events_data = events_data.append({'Date': date, 'Inflation': inflation_rate}, ignore_index=True)

# Function to plot line chart
def plot_line_chart():
    global events_data
    plt.figure(figsize=(10, 6))
    plt.plot(events_data['Date'], events_data['Inflation'], marker='o')
    plt.title('Economic Events - Inflation Rate')
    plt.xlabel('Date')
    plt.ylabel('Inflation Rate (%)')
    st.pyplot()

# Streamlit app
def main():
    st.title('Economic Events Dashboard')

    # Check if the user is an admin
    is_admin = st.checkbox('Are you an admin?')

    if is_admin:
        st.header('Add Economic Event')
        date = st.date_input('Select Date')
        inflation_rate = st.number_input('Inflation Rate (%)', min_value=0.0, step=0.1)
        above_below_option = st.radio('Select above or below current inflation rate:', ['Above', 'Below'])

        if above_below_option == 'Above':
            inflation_rate = max(inflation_rate, 5.0)
        elif above_below_option == 'Below':
            inflation_rate = min(inflation_rate, 5.0)

        if st.button('Add Event'):
            add_event(date, inflation_rate)
            st.success('Economic event added successfully!')

    st.header('Economic Events Line Chart')
    plot_line_chart()

if __name__ == '__main__':
    main()
