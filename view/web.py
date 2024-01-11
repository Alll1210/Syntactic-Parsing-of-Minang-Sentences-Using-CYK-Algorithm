# import streamlit as front end framework
import streamlit as st

# import necessary functions
from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

# prepare the web view
def run_streamlit():
    # title for the web
    title = 'Parsing Sintaksis Kalimat Bahasa Minang Menggunakan Algoritma CYK'

    # setup the web configuration
    st.set_page_config(layout='wide', page_title=title, menu_items={
        'About': f"""
        ### {title}
        Proyek UAS Aplikasi CYK Bahasa Minang
        Nama Anggota Kelompok:
        1. Ali Sya'bana Syukurillah [210111008]
        2. Lutviana                 [210111004]
        3. Yulin Penggu             [210111006]
        """
    })
    
    # prepare the cnf rules
    raw_cfg = open_file('model/cnf.txt')
    # convert the raw cnf rules into readable format for Python
    cnf = raw_to_cfg(raw_cfg)

    # web title
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)

    # split web into two columns, left column displays the cnf rule, right column displays the filling table
    col1, col2 = st.columns(2, gap='small')

    # prepre the left column
    with col1:
        st.write("### Aturan CNF:")
        st.write(raw_cfg)

    # prepare the right column
    with col2:
        # the input sentence text field
        string_input = st.text_input('Masukkan kalimat')
        # convert sentence into list
        list_string = string_input.split(' ')
        # check button
        button_click = st.button('Cek', type='primary')

        # action if button clicked
        if button_click:
            # show error when no string or just one string entered
            if len(list_string) <= 1:
                st.error("Kalimat tidak boleh kosong atau berupa sebuah kata.")
            # else, process the filing table
            elif string_input != '':
                st.write('<br><p>Algoritma Pengisian Tabel:</p>', unsafe_allow_html=True)
                parse(cnf, string_input.split(' '))