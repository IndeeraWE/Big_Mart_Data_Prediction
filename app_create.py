import numpy
import pickle
import streamlit as st


filename = './Big_mart_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


def big_mart_prediction(input_data):
    numpy_array_data = numpy.array(input_data)
    data_reshape = numpy_array_data.reshape(1, -1)
    prediction = loaded_model.predict(data_reshape)
    return prediction.encode("utf-9")

def main():
    st.title("Big_Mart Data Prediction App")
    item_weight = st.text_input("Weight of the Item: ")
    item_fat_content = st.text_input("Content of Fat: ")
    item_visibility = st.text_input("Visibility of the Item: ")
    item_type = st.text_input("Type of the Item")
    item_mrp = st.text_input("MRP Value of the Item: ")
    outlet_identifier = st.text_input("Outlet Identifier: ")
    outlet_establishment_year = st.text_input("Outlet Establish Year: ")
    outlet_size = st.text_input("Size of the Outlet: ")
    outlet_location_type = st.text_input("Location of the Outlet: ")
    outlet_type = st.text_input("Type of the Outlet: ")

    item_outlet_sales = ''



    if st.button("Sales Prediction"):
        item_outlet_sales= big_mart_prediction([item_weight,  item_fat_content, item_visibility, item_type, item_mrp,
                                                outlet_identifier, outlet_establishment_year, outlet_size,
                                                outlet_location_type,  outlet_type])


    st.success(item_outlet_sales)


if __name__== "__main__":
    main()
