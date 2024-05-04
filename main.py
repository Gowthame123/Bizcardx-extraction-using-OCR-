import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu 
from PIL import Image
import easyocr
import mysql.connector
import re
import io

#-------------------------------------------------------my sql connection ----------------------------------------------------------------------
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password='root',
    database = "bizcardx")
mycursor = mydb.cursor()

#-------------------------------------------------------streamlit part--------------------------------------------------------------------------------
#menu bar 
st.set_page_config(layout="wide")
img = Image.open(r"C:\Users\gowth\Downloads\project_3\file\2.png")
st.image(img, use_column_width=True)                
selected = option_menu(
    menu_title = None,
    options = ["Project", "Database", "About"],
    icons = ["book", "database-fill-check", "blockquote-right"],
    default_index = 0,
    orientation=  "horizontal")



#-------------------------------------------------------Project--------------------------------------------------------------------------------
# extract the data
def extracted_text(picture):
    ext_dic = {'Name': [], 'Designation': [], 'Company name': [], 'Contact': [], 'Email': [], 'Website': [],
               'Address': [], 'Pincode': []}

    ext_dic['Name'].append(result[0])
    ext_dic['Designation'].append(result[1])

    for m in range(2, len(result)):
        if result[m].startswith('+') or (result[m].replace('-', '').isdigit() and '-' in result[m]):
            ext_dic['Contact'].append(result[m])

        elif '@' in result[m] and '.com' in result[m]:
            small = result[m].lower()
            ext_dic['Email'].append(small)

        elif 'www' in result[m] or 'WWW' in result[m] or 'wwW' in result[m]:
            small = result[m].lower()
            ext_dic['Website'].append(small)

        elif 'TamilNadu' in result[m] or 'Tamil Nadu' in result[m] or result[m].isdigit():
            ext_dic['Pincode'].append(result[m])

        elif re.match(r'^[A-Za-z]', result[m]):
            ext_dic['Company name'].append(result[m])

        else:
            removed_colon = re.sub(r'[,;]', '', result[m])
            ext_dic['Address'].append(removed_colon)

    for key, value in ext_dic.items():
        if len(value) > 0:
            concatenated_string = ' '.join(value)
            ext_dic[key] = [concatenated_string]
        else:
            value = 'NA'
            ext_dic[key] = [value]

    return ext_dic

if selected == "Project":
    image = st.file_uploader(label="Upload the image", type=['png', 'jpg', 'jpeg'], label_visibility="hidden")
    @st.cache_data
    def load_image():
        reader = easyocr.Reader(['en'], model_storage_directory=".")
        return reader


    reader_1 = load_image()
    if image is not None:
        input_image = Image.open(image)
        # Setting Image size
        st.image(input_image, width=350, caption='Uploaded Image')
        st.markdown(
            f'<style>.css-1aumxhk img {{ max-width: 300px; }}</style>',
            unsafe_allow_html=True
        )

        result = reader_1.readtext(np.array(input_image), detail=0)

                # creating dataframe
        ext_text = extracted_text(result)
        df = pd.DataFrame(ext_text)
        st.dataframe(df)
        # Converting image into bytes
        image_bytes = io.BytesIO()
        input_image.save(image_bytes, format='PNG')
        image_data = image_bytes.getvalue()
        # Creating dictionary
        data = {"Image": [image_data]}
        df_1 = pd.DataFrame(data)
        concat_df = pd.concat([df, df_1], axis=1)

        # Database
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            selected = option_menu(
                menu_title=None,
                options=["Preview"],
                icons=['file-earmark'],
                default_index=0,
                orientation="horizontal"
            )

            ext_text = extracted_text(result)
            df = pd.DataFrame(ext_text)
        if selected == "Preview":
            col_1, col_2 = st.columns([4, 4])
            with col_1:
                modified_n = st.text_input('Name', ext_text["Name"][0])
                modified_d = st.text_input('Designation', ext_text["Designation"][0])
                modified_c = st.text_input('Company name', ext_text["Company name"][0])
                modified_con = st.text_input('Mobile', ext_text["Contact"][0])
                concat_df["Name"], concat_df["Designation"], concat_df["Company name"], concat_df[
                    "Contact"] = modified_n, modified_d, modified_c, modified_con
            with col_2:
                modified_m = st.text_input('Email', ext_text["Email"][0])
                modified_w = st.text_input('Website', ext_text["Website"][0])
                modified_a = st.text_input('Address', ext_text["Address"][0])
                modified_p = st.text_input('Pincode', ext_text["Pincode"][0])
                concat_df["Email"], concat_df["Website"], concat_df["Address"], concat_df[
                    "Pincode"] = modified_m, modified_w, modified_a, modified_p

            col3, col4 = st.columns([4, 4])
            with col3:
                Preview = st.button("Preview modified text")
            with col4:
                Upload = st.button("Upload")
            if Preview:
                filtered_df = concat_df[
                    ['Name', 'Designation', 'Company name', 'Contact', 'Email', 'Website', 'Address', 'Pincode']]
                st.dataframe(filtered_df)
            else:
                pass

            if Upload:
                with st.spinner("In progress"):
                    mycursor.execute(
                        "CREATE TABLE IF NOT EXISTS BUSINESS_CARD(NAME VARCHAR(50), DESIGNATION VARCHAR(100), "
                        "COMPANY_NAME VARCHAR(100), CONTACT VARCHAR(35), EMAIL VARCHAR(100), WEBSITE VARCHAR("
                        "100), ADDRESS TEXT, PINCODE VARCHAR(100))")
                    mydb.commit()
                    A = "INSERT INTO BUSINESS_CARD(NAME, DESIGNATION, COMPANY_NAME, CONTACT, EMAIL, WEBSITE, ADDRESS, " \
                        "PINCODE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    for index, i in concat_df.iterrows():
                        result_table = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
                        mycursor.execute(A, result_table)
                        mydb.commit()
                        st.success('SUCCESSFULLY UPLOADED', icon="✅")
    else:
        st.write("Upload an image")

#-------------------------------------------------------Database--------------------------------------------------------------------------------    
if selected == "Database":
    selected = option_menu(
        menu_title = None,
        options = ["Database","Deleted"],
        default_index = 0,
        orientation=  "horizontal")
    if selected == "Database":
            mycursor.execute(f"SELECT * FROM BUSINESS_CARD;")
            rslt = mycursor.fetchall()
            if not rslt:
                st.write("# None")
            else:
                df_rslt = pd.DataFrame(np.array(rslt),columns=["NAME", "DESIGNATION", "COMPANY_NAME", "CONTACT", "EMAIL", "WEBSITE", "ADDRESS", "PINCODE"])
                df_rslt1 = df_rslt.set_index(pd.Index(range(1, len(df_rslt) + 1)))
                st.dataframe(df_rslt1)

    if selected == "Deleted":
        col1, col2 = st.columns([4, 4])
        with col1:
            mycursor.execute("SELECT NAME FROM BUSINESS_CARD")
            Y = mycursor.fetchall()
            names = ["Select"]
            for i in Y:
                names.append(i[0])
            name_selected = st.selectbox("Select the name to delete", options=names)
            # st.write(name_selected)
        with col2:
            mycursor.execute(f"SELECT DESIGNATION FROM BUSINESS_CARD WHERE NAME = '{name_selected}'")
            Z = mycursor.fetchall()
            designation = ["Select"]
            for j in Z:
                designation.append(j[0])
            designation_selected = st.selectbox("Select the designation of the chosen name", options=designation)

        st.markdown(" ")

        col_a, col_b, col_c = st.columns([5, 3, 3])
        with col_b:
            remove = st.button("Clik here to delete")
        if name_selected and designation_selected and remove:
            mycursor.execute(
                f"DELETE FROM BUSINESS_CARD WHERE NAME = '{name_selected}' AND DESIGNATION = '{designation_selected}'")
            mydb.commit()
            if remove:
                st.warning('DELETED', icon="⚠️")




#-------------------------------------------------------About--------------------------------------------------------------------------------
if selected == "About":
    selected = option_menu(
    menu_title = None,
    options = ["Project", "Personal"],
    icons = ["projector-fill", "file-earmark-person-fill"],
    default_index = 0,
    orientation=  "horizontal")
    if selected == "Project":
        st.header("ABOUT THE PROJECT")
        st.write("""BizCardX sounds like a valuable tool for streamlining the extraction of information from business cards. Leveraging Optical Character Recognition (OCR) through the EasyOCR Python library makes it efficient and accessible. 
                 Its emphasis on user-friendliness, straightforward installation, minimal dependencies, and easy integration into development environments suggests that it aims to provide a hassle-free experience for users.""") 

        st.write("""By simplifying the OCR process, BizCardX could save users time and effort typically spent manually inputting data from business cards. 
         This could be particularly useful for professionals who frequently network or handle large volumes of business cards, such as salespeople, recruiters, or event organizers.""") 

        st.write("""Overall, BizCardX seems like a practical solution for automating the extraction of information from business cards, making it a valuable tool for various industries and professionals.""") 
        st.header("Key Features:")
        st.write("""BizCardX Application: BizCardX is a versatile tool that harnesses OCR technology to recognize text on business cards, extracting valuable data into a MySQL workbench. The process involves classification using regular expressions to enhance accuracy.
                  The user interacts with a user-friendly GUI built using Streamlit, guiding them through the steps of uploading a business card image and extracting information.""") 

    if selected == "Personal":
        col1, col2 = st.columns(2)  
        col2.image(Image.open(r'C:\Users\gowth\Downloads\project_phonepe\files\gowtham.JPG'), width=600)
        with col1:
            st.markdown("## Done by : GOWTHAM E") 
            st.markdown(" An Aspiring DATA-SCIENTIST..!")
            st.markdown("Gmail: gowthame82000@gmail.com")
            st.markdown("[Githublink](https://github.com/Gowthame123)")
            st.markdown("[LinkedIn](https://www.linkedin.com/in/gowthamesakki/)") 
        st.write("---") 
                