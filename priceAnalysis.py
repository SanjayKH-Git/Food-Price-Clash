import pandas as pd
import numpy as np

# food_details = {'swiggy': {'2 Idli 1 Vada': '90', 'Idli': '50', 'Vada': '30', 'Poori Sagu': '100', 'Set Dosa': '85', 'Plain Dosa': '70', 'Cheese Plain Dosa': '100', 'Paper Plain Dosa': '100', 'Masala Dosa': '55', 'Butter Masala Dosa': '90', 'Cheese Masala Dosa': '95', 'Onion Dosa': '95', 'Rava Dosa': '100', 'Mysore Masala Dosa': '110', 'Idli + Vada + Set Dosa': '110', 'Tomato Soup': '85', 'Veg Clear Soup': '100', 'Mushroom Veg Clear Soup': '110', 'Masala Puri': '70', 'Pani Puri': '70', 'Samosa Plain': '85', 'Vada Pav': '90', 'Tea': '25', 'Chocolate Shake': '100', 'Watermelon Juice': '100', 'Musk Melon Juice': '100', 'Jamun': '40', 'Veg Fried Rice': '100', 'Paneer Fried Rice': '179', 'Veg Noodles': '160', 'Schezwan Noodles': '185', 'Mushroom Noodles': '180', 'Paneer Noodles': '180', 'Gobi Manchurian': '140', 'Gobi Chilli': '150', 'Baby Corn Manchurian': '170', 'Baby Corn Chilli': '190', 'Mushroom Pepper Dry': '200', 'Paneer Manchurian': '210', 'Paneer Chilli': '210', 'Paneer Pepper Dry': '210', 'Mushroom Chilli Gravy': '220', 'Mushroom Manchurian Gravy': '200', 'Veg Cheese Grilled Sandwich': '150'}, 'zomato': {'Mini Tiffin': '140', 'Ghee Rice Combo': '180', 'Jeera Rice Combo': '180', 'Chinese Combo': '229', 'Chinese Combo 1': '200', 'Idli Combo': '110', 'Masala Dosa Combo': '200', 'Fried Idli With Idli 65 Combo': '200', 'Dosa Combo': '120', 'Mini Masala Dosa Combo': '190', 'Mysore Masala Dosa Combo': '180', 'Dosa Platter': '399', 'Tomato Soup': '85', 'Cream Veg Soup': '100', 'Sweet Corn Soup': '100', 'Hot & Sour Soup': '105', 'Mushroom Clear Soup': '110', 'Veg Clear Soup': '100', 'Veg Lung Fung Soup': '110', 'Veg Schezwan Soup': '110', 'Mushroom Veg Clear Soup': '110', 'French Onion Soup': '110', 'Pineapple Soup': '110', 'Green Peas Soup': '110', 'Manchow Soup': '110', 'Veg Noodles Soup': '110', 'Lemon Coriander Soup': '110', 'Gobi Manchurian': '140', 'Chilli Gobi': '150', 'Gobi 65': '170', 'Gobi Pepper Dry': '170', 'Gobi Crispy': '170', 'Gobi Salt & Pepper': '170', 'Baby Corn Manchurian': '170', 'Chilli Baby Corn': '190', 'Baby Corn Pepper Dry': '190', 'Baby Corn 65': '190', 'Baby Corn Crispy': '190', 'Baby Corn Salt And Pepper': '190', 'Mushroom Manchurian': '200', 'Mushroom Pepper Dry': '200', 'Crispy Mushroom': '200', 'Mushroom Salt And Pepper': '200', 'Paneer Manchurian': '210', 'Chilli Paneer': '210', 'Paneer 65': '210', 'Paneer Pepper Dry': '210', 'Paneer Cripsy': '210', 'Paneer Salt And Pepper': '210', 'American Corn Manchurian': '200', 'American Corn Pepper Dry': '200', 'Crispy American Corn': '200', 'American Corn Salt And Pepper': '200', 'Veg Balls Manchurian': '190', 'Spanish Manchurian': '200',
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'Idli [2 Pieces] With Vada [1 Piece]': '90', 'Chilli Idli': '120', 'Fry Idli': '120', 'Idli 65': '130', 'Idli Vada': '70', 'Idli': '50', 'Vada': '46', 'Set Dosa': '85', 'Plain Dosa': '70', 'Butter Plain Dosa': '80', 'Paneer Plain Dosa': '85', 'Cheese Plain Dosa': '100', 'Pepper Plain Dosa': '100', 'Masala Dosa': '85', 'Butter Masala Dosa': '90', 'Paneer Masala Dosa': '100', 'Cheese Masala Dosa': '95', 'Paper Masala Dosa': '110', 'Khali Dosa': '80', 'Butter Khali Dosa': '95', 'Onion Dosa': '95', 'Rava Dosa': '100', 'Rava Onion Dosa': '110', 'Rava Masala Dosa': '110', 'Onion Rava Masala Dosa': '120', 'Open Butter Masala Dosa': '110', 'Mysore Masala Dosa': '110', 'Shri Udupi Special Dosa': '110', 'Ghee Podi Masala': '100', 'Mini Vada With Sambar Dip': '80', 'Button Idli With Sambar Dip': '80', '2 Mini Masala Dosa': '100', 'Veg Noodles': '160', 'Schezwan Noodles': '185', 'Mushroom Noodles': '180', 'Paneer Noodles': '180', 'Singapore Noodles': '190', 'Hakka Noodles': '180', 'Chowmein Noodles': '180', 'Veg Triple Noodles': '180', 'Veg Fried Rice': '169', 'Paneer Fried Rice': '179', 'Mushroom Fried Rice': '179', 'Schezwan Fried Rice': '179', 'Combination Fried Rice': '179', 'Ginger Garlic Fried Rice': '179', 'Schezwan Paneer Fried Rice': '185', 'Schezwan Mushroom Fried Rice': '185', 'Schezwan Baby Corn Fried Rice': '185', 'Bread Butter Jam Sandwich': '80', 'Bread Butter Toast Sandwich': '70', 'Bread Butter Gulkand Sandwich': '80', 'Krishnam Special Sandwich': '150', 'Veg Grilled Sandwich': '100', 'Veg Cheese Grilled Sandwich': '150', 'Cheese Toast Grilled Sandwich': '130', 'Veg Paneer Grilled Sandwich': '130', 'Paneer Toast Grilled Sandwich': '130', 'Veg Cheese Paneer Grilled Sandwich': '150', 'Veg Mushroom Grilled Sandwich': '150', 'Sandwich Dosa': '120', 'Masala Puri': '70', 'Paani Puri': '70', 'Bhel Puri': '75', 'Dahi Puri': '75', 'Aloo Puri': '75', 'Sev Dahi Potato Puri': '75', 'Special Bhel': '85', 'Plain Samosa': '85', 'Masala Samosa': '50', 'Udupi Special Chaat': '80', 'Vada Pav': '90', 'Fingers Chips': '120', 'Potato Twisters': '120', 'Spring Rolls': '140', 'Paneer Pav Bhaji': '130', 'Pav Bhaji': '120', 'Cheese Pav Bhaji': '150', 'Kadhai Pav Bhaji': '130', 'Vanilla Ice Cream': '60', 'Strawberry Ice Cream': '60', 'Chocolate Ice Cream': '80', 'Mango Ice Cream': '80', 'Pista Ice Cream': '80', 'Butterscotch Ice Cream': '80', 'Fig Honey Ice Cream': '80', 'Blackcurrant Ice Cream': '80', 'Cut Fruit': '100', '110 Fruit Salad with Jelly': '130', 'Fruit Salad': '120', 'Ice Cream': '30', 'Jelly Ice': '60', 'Jelly With Ice Cream': '150', 'Fresh Mango With Ice Cream': '160', 'Gulab Jamun': '40', 'Gur Bud Ice Cream': '150', 'Falooda Ice Cream': '150', 'Special Falooda Ice Cream': '160', 'Banana Split Ice Cream': '160', 'Shri Udupi Ice Cream': '180', 'Nut Sundae Ice Cream': '160', 'Vanilla Nut Sundae Ice Cream': '160', 'Chocolate Nut Sundae Ice Cream': '160', 'Raja Rani Ice Cream': '160', 'Titanic Special Ice Cream': '170', 'Honeymoon Special Ice Cream': '160', 'Fruit Sundae Ice Cream': '160', 'Tea': '25', 'Ginger Coffee': '40', 'Lemon Tea': '30', 'Green Tea': '30', 'Badam Milk': '40', 'Horlicks': '40', 'Bournvita': '40', 'Coffee [110 ml]': '25', 'Chocolate Shake': '100', 'Strawberry Shake': '100', 'Cold Coffee Shake': '100', 'Cold Badam Shake': '100', 'Rose Milkshake': '110', 'Pista Shake': '120', 'Vanilla Shake': '110', 'Butterscotch Shake': '110', 'Blackcurrant Shake': '110', 'Sapota Shake With Ice Cream': '130', 'Dry Fruit Milkshake': '170', 'Daily Special Shake': '160', 'Mausami Juice': '100', 'Pineapple Juice': '100', 'Ganga Jamuna Juice': '100', 'Watermelon Juice': '100', 'Mango Juice': '100', 'Cocktail Juice': '100', 'Muskmelon Juice': '100', 'Lime Juice': '60', 'Pudina Lime Juice': '70', 'Grapes Juice': '90', 'Mausambi Solid Juice': '120', 'Apple Shake': '120', 'Sapota Shake': '120', 'Pomegranate Shake': '120', 'Batter Fruit Shake': '120', 'Muskmelon Shake': '120', 'Banana Milkshake': '120', 'Mango Shake': '120', 'Buttermilk': '60', 'Sweet Lassi': '80', 'Salted Lassi': '80', 'Khara Lassi': '90', 'Mango Lassi': '100', 'Special Lassi': '100', 'Dry Fruit Lassi': '120', 'Fresh Lime Soda': '80', 'Pudina Lime Soda': '85', 'Ginger Lime Soda': '95', 'Masala Soda': '95', 'Kiwi Soda': '100'}}
# print(food_details.keys())


def priceAnalyser(food_details):

    food_details_df = pd.DataFrame(food_details)
    # print(food_details_df)

    # Reset the index to remove the platform names from the index
    food_details_df.reset_index(inplace=True)

    # Rename the columns to remove the 'index' column name
    food_details_df.columns = ['FoodName'] + \
        food_details_df.columns[1:].tolist()

    # Drop duplicate rows based on the 'FoodName' column
    food_details_df.drop_duplicates(
        subset='FoodName', keep='first', inplace=True)

    # Reset the index again to have a clean index after dropping duplicates
    food_details_df.reset_index(drop=True, inplace=True)

    # print(food_details_df)

    # # Get the common food names and their prices using dictionary comprehension
    common_food_data = {
        food_name: {'Swiggy Price': food_details['swiggy'].get(food_name),
                    'Zomato Price': food_details['zomato'].get(food_name)}
        for food_name in set(food_details['swiggy'].keys()) & set(food_details['zomato'].keys())
    }

    # Create the DataFrame
    common_food_df = pd.DataFrame.from_dict(common_food_data, orient='index')

    print(common_food_df)
    swiggy_common_Total = pd.to_numeric(common_food_df["Swiggy Price"]).sum()
    zomato_common_Total = pd.to_numeric(common_food_df["Zomato Price"]).sum()

    if swiggy_common_Total == zomato_common_Total:
        print("Based on Our Analysis Looks both are having similar prices,\
            But We recommend to see the Real-Time Price Table displayed below.")
    if swiggy_common_Total < zomato_common_Total:
        print('Based on Our Real-Time Analysis "Swiggy" is Cheaper than "Zomato" Today')
    else:
        print('Based on Our Real-Time Analysis "Zomato" is Cheaper than "Swiggy" Today')

    # Combine data from both platforms into a single DataFrame
    food_details_df = pd.DataFrame(food_details)

    # Find the common food items between swiggy and zomato
    common_food_items = list(
        set(food_details['swiggy'].keys()) & set(food_details['zomato'].keys()))

    # Extract the common food items and sort them
    common_food_df = food_details_df.loc[common_food_items]

    # Append the rest of the items (non-common) at the bottom
    non_common_food_df = food_details_df.drop(index=common_food_items)

    # Concatenate common_food_df and non_common_food_df to get the final sorted DataFrame
    final_sorted_df = pd.concat([common_food_df, non_common_food_df])

    # Display the final sorted DataFrame
    # print(final_sorted_df)

    # Convert the DataFrame to a dictionary
    # result_dict = final_sorted_df.to_dict()

    # Convert the DataFrame to a dictionary
    result_dict = {}

    # Process Swiggy data
    swiggy_data = final_sorted_df['swiggy'].dropna()  # Remove rows with NaN values
    result_dict['swiggy'] = swiggy_data.to_dict()

    # Process Zomato data
    zomato_data = final_sorted_df['zomato'].dropna()  # Remove rows with NaN values
    result_dict['zomato'] = zomato_data.to_dict()

    # Display the result
    # print(result_dict)

    result_dict['swiggy_common_Total'] = str(swiggy_common_Total)
    result_dict['zomato_common_Total'] = str(zomato_common_Total)

    print(result_dict)
    return result_dict


# priceAnalyser(food_details)
