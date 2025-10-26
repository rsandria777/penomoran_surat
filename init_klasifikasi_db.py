import sqlite3

# Membuat atau membuka database
conn = sqlite3.connect('klasifikasi.db')
c = conn.cursor()

# Hapus tabel lama jika ada
c.execute('DROP TABLE IF EXISTS klasifikasi_surat')

# Buat tabel baru
c.execute('''
CREATE TABLE klasifikasi_surat (
    kode TEXT PRIMARY KEY,
    nama TEXT NOT NULL,
    parent_kode TEXT
)
''')

# Daftar data klasifikasi surat
data = [
    # ===== LAYER 1 =====
    ('000', 'Umum', None),
    ('100', 'Pemerintahan', None),
    ('200', 'Politik', None),
    ('300', 'Keamanan dan Ketertiban', None),
    ('400', 'Kesejahteraan Rakyat', None),
    ('500', 'Perekonomian', None),
    ('600', 'Pekerjaan Umum dan Ketenagaan', None),
    ('700', 'Pengawasan', None),
    ('800', 'Kepegawaian', None),
    ('900', 'Keuangan', None),

    # ===== LAYER 2 (Umum) =====
    ('000.1', 'Ketatausahaan dan Kerumahtanggaan', '000'),
    ('000.2', 'Perlengkapan', '000'),
    ('000.3', 'Pengadaan', '000'),
    ('000.4', 'Perpustakaan', '000'),
    ('000.5', 'Kearsipan', '000'),
    ('000.6', 'Persandian', '000'),
    ('000.7', 'Perencanaan Pembangunan', '000'),
    ('000.8', 'Organisasi dan Tata Laksana', '000'),
    ('000.9', 'Penelitian, Pengkajian, dan Pengembangan', '000'),

    # ===== LAYER 2 (Pemerintahan) =====
    ('100.1', 'Otonomi Daerah', '100'),
    ('100.2', 'Pemerintahan Umum', '100'),
    ('100.3', 'Hukum', '100'),

    # ===== LAYER 2 (Politik) =====
    ('200.1', 'Kesatuan Bangsa dan Politik', '200'),
    ('200.2', 'Pemilu', '200'),

    # ===== LAYER 2 (Keamanan dan Ketertiban) =====
    ('300.1', 'Satuan Polisi Pamong Praja', '300'),
    ('300.2', 'Penanggulangan Bencana, Pencarian, dan Pertolongan', '300'),

    # ===== LAYER 2 (Kesejahteraan Rakyat) =====
    ('400.1', 'Pembangunan Daerah Tertinggal', '400'),
    ('400.2', 'Pemberdayaan Perempuan dan Perlindungan Anak', '400'),
    ('400.3', 'Pendidikan', '400'),
    ('400.4', 'Keolahragaan', '400'),
    ('400.5', 'Kepemudaan', '400'),
    ('400.6', 'Kebudayaan', '400'),
    ('400.7', 'Kesehatan', '400'),
    ('400.8', 'Agama dan Kepercayaan', '400'),
    ('400.9', 'Sosial', '400'),
    ('400.10', 'Pemberdayaan Masyarakat Desa', '400'),
    ('400.11', 'Pertamanan dan Pemakaman', '400'),
    ('400.12', 'Kependudukan dan Pencatatan Sipil', '400'),
    ('400.13', 'Keluarga Berencana', '400'),
    ('400.14', 'Hubungan Masyarakat', '400'),

# ===== LAYER 2 (Perekonomian) =====
    ('500.1', 'Ketahanan Pangan', '500'),
    ('500.2', 'Perdagangan', '500'),
    ('500.3', 'Koperasi dan Usaha Kecil Menengah', '500'),
    ('500.4', 'Kehutanan', '500'),
    ('500.5', 'Kelautan dan Perikanan', '500'),
    ('500.6', 'Pertanian', '500'),
    ('500.7', 'Peternakan', '500'),
    ('500.8', 'Perkebunan', '500'),
    ('500.9', 'Perindustrian', '500'),
    ('500.10', 'Energi dan Sumber Daya Mineral', '500'),
    ('500.11', 'Perhubungan', '500'),
    ('500.12', 'Komunikasi dan Informatika', '500'),
    ('500.13', 'Pariwisata dan Ekonomi Kreatif', '500'),
    ('500.14', 'Statistik', '500'),
    ('500.15', 'Ketenagakerjaan', '500'),
    ('500.16', 'Penanaman Modal', '500'),
    ('500.17', 'Pertanahan', '500'),
    ('500.18', 'Transmigrasi', '500'),

    # ===== LAYER 2 (Pekerjaan Umum dan Ketenagaan) =====
    ('600.1', 'Pekerjaan Umum', '600'),
    ('600.2', 'Perumahan Rakyat dan Kawasan Pemukiman', '600'),
    ('600.3', 'Tata Ruang', '600'),
    ('600.4', 'Lingkungan Hidup', '600'),

    # ===== LAYER 2 (Pengawasan) =====
    ('700.1', 'Pengawasan Internal', '700'),

    # ===== LAYER 2 (Kepegawaian) =====
    ('800.1', 'Sumber Daya Manusia', '800'),
    ('800.2', 'Pendidikan dan Pelatihan', '800'),

    # ===== LAYER 2 (Pengawasan) =====
    ('900.1', 'Keuangan Daerah', '900'),
    
    # ===== LAYER 3 (000.1) =====
    ('000.1.1', 'Telekomunikasi', '000.1'),
    ('000.1.2', 'Perjalanan Dinas Dalam Negeri', '000.1'),
    ('000.1.3', 'Perjalanan Dinas Luar Negeri', '000.1'),
    ('000.1.4', 'Penggunaan Fasilitas Kantor', '000.1'),
    ('000.1.5', 'Rapat Pimpinan (Notula/Risalah Rapat)', '000.1'),
    ('000.1.6', 'Penyediaan Konsumsi', '000.1'),
    ('000.1.7', 'Pengurusan Kendaraan Dinas', '000.1'),
    ('000.1.8', 'Pemeliharaan Gedung, Taman, dan Peralatan Kantor', '000.1'),
    ('000.1.9', 'Pengelolaan Jaringan Listrik, Air, Telepon, dan Komputer', '000.1'),
    ('000.1.10', 'Ketertiban dan Keamanan', '000.1'),
    ('000.1.11', 'Administrasi Pengelolaan Parkir', '000.1'),
    ('000.1.12', 'Administrasi Pakaian Dinas Pegawai, Satpam, Petugas Kebersihan dan Pegawai lainnya', '000.1'),

    # ===== LAYER 4 (000.1.2 & 000.1.3) =====
    ('000.1.2.1', 'Perjalanan Dinas Kepala Daerah', '000.1.2'),
    ('000.1.2.2', 'Perjalanan Dinas DPRD', '000.1.2'),
    ('000.1.2.3', 'Perjalanan Dinas Pegawai', '000.1.2'),
    ('000.1.3.1', 'Perjalanan Dinas Kepala Daerah', '000.1.3'),
    ('000.1.3.2', 'Perjalanan Dinas DPRD', '000.1.3'),
    ('000.1.3.3', 'Perjalanan Dinas Pegawai', '000.1.3')
]

# Masukkan ke database
c.executemany('INSERT INTO klasifikasi_surat VALUES (?, ?, ?)', data)
conn.commit()
conn.close()

print("✅ Database klasifikasi.db berhasil dibuat dan diisi data.")
