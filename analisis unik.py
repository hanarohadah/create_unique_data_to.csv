import streamlit as st
import pandas as pd
import numpy as np

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Generator Matriks Kompetensi", layout="wide")

# --- 2. FUNGSI LOGIKA (BACKEND) ---
def bersihkan_dan_ambil_unik(list_baru, data_lama):
    """
    Fungsi ini:
    1. Menggabungkan data lama dan baru.
    2. Membersihkan simbol bullet point (●) dan spasi.
    3. Mengambil data unik (hapus duplikat).
    """
    # Gabungkan data lama (numpy array) dan list baru
    # Kita ubah data_lama ke list dulu biar bisa digabung
    if isinstance(data_lama, np.ndarray):
        data_lama = data_lama.tolist()
    
    gabungan = data_lama + list_baru
    
    # Bersihkan item (hapus simbol bullet, spasi di awal/akhir)
    # Hapus juga item yang kosong (string kosong)
    data_bersih = []
    for item in gabungan:
        # Hapus simbol bullet '●' dan spasi kiri kanan
        item_clean = str(item).replace('●', '').strip()
        if item_clean: # Jika tidak kosong setelah dibersihkan
            data_bersih.append(item_clean)
    
    # Ambil Unik menggunakan set() -> Lalu ubah ke Numpy Array
    hasil_numpy = np.array(sorted(list(set(data_bersih))))
    
    return hasil_numpy

# --- 3. INISIALISASI SESSION STATE ---
# Ini berguna agar data tidak hilang saat tombol diklik (sebelum browser ditutup)
if 'master_data' not in st.session_state:
    st.session_state['master_data'] = np.array([])

# --- 4. TAMPILAN SIDEBAR (AREA UPLOAD & WARNING) ---
with st.sidebar:
    st.header("1. Load Data Lama")
    uploaded_file = st.file_uploader("Upload CSV terakhir Anda di sini:", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Baca CSV
            df_upload = pd.read_csv(uploaded_file)
            # Asumsi kolom pertama adalah data kompetensi
            loaded_data = df_upload.iloc[:, 0].dropna().values
            
            # Masukkan ke sistem hanya jika tombol ditekan (biar gak reload terus)
            if st.button("Terapkan Data Upload"):
                # Gabung dengan yang ada di memori sekarang (jika ada)
                st.session_state['master_data'] = bersihkan_dan_ambil_unik([], loaded_data)
                st.success(f"Berhasil memuat {len(st.session_state['master_data'])} data!")
        except Exception as e:
            st.error(f"Gagal membaca file: {e}")

    st.markdown("---")
    st.error("⚠️ **PENTING!**")
    st.warning(
        "Data di aplikasi ini bersifat **SEMENTARA**.\n\n"
        "Setiap kali Anda selesai bekerja atau ingin menutup tab ini, "
        "wajib klik **DOWNLOAD CSV** di bagian bawah halaman utama.\n\n"
        "Jika tidak, data hari ini akan hilang."
    )

# --- 5. TAMPILAN UTAMA (MAIN AREA) ---
st.title("Aplikasi Matriks Kompetensi Unik")

st.info("Masukkan daftar kompetensi mentah (boleh copas dari Word/Excel dengan simbol ●).")

# Input Text Area
raw_text = st.text_area("2. Paste Data Baru Di Sini:", height=200, placeholder="● Strategi Business Development\n● Pengembangan Produk\n...")

col1, col2 = st.columns([1, 4])

with col1:
    tombol_proses = st.button("3. Proses & Gabungkan", type="primary")

# Logika saat tombol Proses ditekan
if tombol_proses and raw_text:
    # Pecah teks berdasarkan baris (enter)
    list_input_baru = raw_text.split('\n')
    
    # Jalankan fungsi logika kita
    data_updated = bersihkan_dan_ambil_unik(list_input_baru, st.session_state['master_data'])
    
    # Simpan kembali ke memory (Session State)
    st.session_state['master_data'] = data_updated
    st.success("Data baru berhasil digabungkan dan duplikat dihapus!")

# --- 6. MENAMPILKAN HASIL & DOWNLOAD ---
st.markdown("---")
st.subheader("Hasil Data Unik Terkini")

if len(st.session_state['master_data']) > 0:
    # Konversi Numpy ke Pandas DataFrame agar rapi dan bisa didownload
    df_hasil = pd.DataFrame(st.session_state['master_data'], columns=["Kompetensi / Skill"])
    
    # Tampilkan Dataframe
    st.dataframe(df_hasil, use_container_width=True)
    
    st.write(f"Total Jumlah Unik: **{len(df_hasil)}** item.")
    
    # Tombol Download CSV
    csv_data = df_hasil.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 4. DOWNLOAD CSV (Simpan Data Ini)",
        data=csv_data,
        file_name='master_kompetensi_unik.csv',
        mime='text/csv',
        help="Klik ini sebelum menutup aplikasi!"
    )
else:
    st.write("Belum ada data yang tersimpan.")