# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothies :cup_with_straw:")
st.write(
    
)

#Write directly to the app

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect ('Choose upt to 5 ingredients:', my_dataframe
                                  , max_selections=5)

name_on_order = title = st.text_input("Name on Smoothie")
st.write("The Name on your smoothie will be", name_on_order)

if ingredients_list:
 ingredients_string = ''
    
     for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
        fv_df = st.dataframe(data= fruityvice_response.json(), use_container_width =True)

#st.write(ingredients_string)

my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

#st.write(my_insert_stmt)
#st.stop()

time_to_insert = st.button('Submit order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()

if ingredients_string:
   session.sql(my_insert_stmt).collect()

   st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fv_df = st.dataframe(data= fruityvice_response.json(), use_container_width =True)
