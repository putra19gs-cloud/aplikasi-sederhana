import streamlit as st

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon=":sunglasses:"
)

with st.sidebar:
    col1, col2, col3 = st.columns((1, 2, 1))
    with col2:
        try:
            st.image("Geometri.png")
        except:
            pass
        st.title("Bangun Datar")
        pilihan = st.selectbox("Pilihan Bangun Datar", ("Persegi", "Persegi Panjang", "Segitiga", "Lingkaran", "Kubus"))
        st.caption("Dibuat dengan :sparkles: oleh **Efraim Aditya Putra**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi")
        
        with st.form("form_persegi"):
            sisi = st.number_input("Masukkan Sisi", min_value=0.0, step=0.1)
            submitted = st.form_submit_button("Hitung")
            if submitted:
                Luas = sisi * sisi
                Keliling = 4 * sisi
                st.success(f"Luas persegi adalah {Luas:.2f} dan kelilingnya adalah {Keliling:.2f}")
                st.balloons()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi panjang")
        
        with st.form("form_persegi_panjang"):
            panjang = st.number_input("Masukkan Panjang", min_value=0.0, step=0.1)
            lebar = st.number_input("Masukkan Lebar", min_value=0.0, step=0.1)
            submitted = st.form_submit_button("Hitung")
            if submitted:
                Luas = panjang * lebar
                Keliling = 2 * (panjang + lebar)
                st.success(f"Luas persegi panjang adalah {Luas:.2f} dan kelilingnya adalah {Keliling:.2f}")

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung 'luas' dan 'keliling' segitiga")
        
        with st.form("form_segitiga"):
            alas = st.number_input("Masukkan Alas", min_value=0.0, step=0.1)
            tinggi = st.number_input("Masukkan Tinggi", min_value=0.0, step=0.1)
            sisi1 = st.number_input("Masukkan Sisi 1", min_value=0.0, step=0.1)
            sisi2 = st.number_input("Masukkan Sisi 2", min_value=0.0, step=0.1)
            sisi3 = st.number_input("Masukkan Sisi 3", min_value=0.0, step=0.1)
            submitted = st.form_submit_button("Hitung")
            if submitted:
                Luas = 0.5 * alas * tinggi
                Keliling = sisi1 + sisi2 + sisi3
                st.success(f"Luas segitiga adalah {Luas:.2f} dan kelilingnya adalah {Keliling:.2f}")

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung 'luas' dan 'keliling' lingkaran")
        
        with st.form("form_lingkaran"):
            jari_jari = st.number_input("Masukkan Jari-Jari", min_value=0.0, step=0.1)
            submitted = st.form_submit_button("Hitung")
            if submitted:
                Luas = 3.14 * jari_jari * jari_jari
                Keliling = 2 * 3.14 * jari_jari
                st.success(f"Luas lingkaran adalah {Luas:.2f} dan kelilingnya adalah {Keliling:.2f}")

    case "Kubus":
        st.title("Kubus")
        st.markdown("Menghitung 'luas permukaan' dan 'keliling/total rusuk' kubus")
        
        with st.form("form_kubus"):
            sisi = st.number_input("Masukkan Sisi", min_value=0.0, step=0.1)
            submitted = st.form_submit_button("Hitung")
            if submitted:
                Luas = 6 * sisi * sisi
                Keliling = 12 * sisi
                st.success(f"Luas permukaan kubus adalah {Luas:.2f} dan total panjang rusuknya adalah {Keliling:.2f}")

    case _:
        st.error("Terjadi kesalahan")