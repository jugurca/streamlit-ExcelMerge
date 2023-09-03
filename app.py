import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Excel Merger",
    page_icon=":bar_chart:",
)

st.title("Merge Excel Files")

with st.sidebar:
    st.header("İbrahim Uğurca")
    st.write("jugurca@gmail.com")

    st.header("How to use excel merger app")
    st.video('https://youtu.be/3cyi-5XVeEU')

birlesmis_dosya_adi = st.text_input("The file to be merged, please enter its name. (Example, 'Combine_Data'):")

if birlesmis_dosya_adi == "":
    st.warning("Please enter a file name!")
elif birlesmis_dosya_adi is not None:
    st.success("Successful! The name has been entered: " + birlesmis_dosya_adi)

secilen_format = st.radio("Select the download format:", ["CSV", "XLSX"])

excel_dosyalari = st.file_uploader("Select the Excel files to be merged", type=["xlsx", "xls"],accept_multiple_files=True)

if st.button("Merge Data"):
    if excel_dosyalari:
        birlesmis_veri = pd.DataFrame()
        for dosya in excel_dosyalari:
            df = pd.read_excel(dosya)

            ilk_satir = df.iloc[0]
            digerleri = df.iloc[0:]

            birlesmis_veri = pd.concat([birlesmis_veri, digerleri], ignore_index=True)

        if birlesmis_dosya_adi:
            if secilen_format == "CSV":
                birlesmis_dosya_adi += ".csv"
                birlesmis_dosya_yolu = birlesmis_dosya_adi
                birlesmis_veri.to_csv(birlesmis_dosya_yolu, index=False)
            elif secilen_format == "XLSX":
                birlesmis_dosya_adi += ".xlsx"
                birlesmis_dosya_yolu = birlesmis_dosya_adi
                birlesmis_veri.to_excel(birlesmis_dosya_yolu, index=False)
            st.success(f"A merged file named '{birlesmis_dosya_adi}' has been created.")

            with open(birlesmis_dosya_adi, "rb") as dosya:
                st.download_button(label=f"Download the merged  {secilen_format}  file", data=dosya,
                                   file_name=birlesmis_dosya_adi)


