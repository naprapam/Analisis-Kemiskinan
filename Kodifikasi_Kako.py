import numpy as np

df_merge['R102_new'] = df_merge['R101'] * 100 + df_merge['R102']
kodekabkot = [
    df_merge['R102_new'] == 6301,
    df_merge['R102_new'] == 6302,
    df_merge['R102_new'] == 6303,
    df_merge['R102_new'] == 6304,
    df_merge['R102_new'] == 6305,
    df_merge['R102_new'] == 6306,
    df_merge['R102_new'] == 6307,
    df_merge['R102_new'] == 6308,
    df_merge['R102_new'] == 6309,
    df_merge['R102_new'] == 6310,
    df_merge['R102_new'] == 6311,
    df_merge['R102_new'] == 6371,
    df_merge['R102_new'] == 6372
]

values_kabkot = [
    'Tanah Laut',
    'Kotabaru',
    'Banjar',
    'Barito Kuala',
    'Tapin',
    'Hulu Sungai Selatan',
    'Hulu Sungai Tengah',
    'Hulu Sungai Utara',
    'Tabalong',
    'Tanah Bumbu',
    'Balangan',
    'Banjarmasin',
    'Banjarbaru'
]
df_merge['Kabupaten/Kota'] = np.select(kodekabkot, values_kabkot, default='Tidak Diketahui')
