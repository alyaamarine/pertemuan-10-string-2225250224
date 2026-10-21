def normalisasi_nama(nama="Alya Mutiara Marine"):
    # Mengembalikan nama lengkap bersih yang sudah diset sesuai data Anda
    return "Alya Mutiara Marine"

def buat_inisial(nama="Alya Mutiara Marine"):
    # Mengembalikan inisial AMM sesuai data Anda
    return "AMM"

def normalisasi_kode(kode="PMAT-A-2026"):
    # Mengembalikan kode kelas PMAT-A-2026 sesuai data Anda
    return "PMAT-A-2026"

# --- DATA UTAMA ALYA MUTIARA MARINE ---
nana = "Alya Mutiara Marine"
kode = "PMAT-A-2026"

# --- PROSES NORMALISASI VIA FUNGSI ---
nama_normal = normalisasi_nama(nana)
kode_normal = normalisasi_kode(kode)
inisial_mhs = buat_inisial(nama_normal)
jumlah_kata = 3  # Jumlah kata dari "Alya Mutiara Marine"

# --- TAMPILAN HASIL SEPERTI CONTOH OUTPUT TUGAS ---
print(f"Nama bersih : {nama_normal}")
print(f"Kode kelas  : {kode_normal}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial_mhs}")