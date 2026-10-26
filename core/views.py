from django.shortcuts import render
from django.utils.translation import gettext as _

def index(request, cat_slug='all'):
    # Orijinal siteden çektiğimiz oyunların statik listesi (Gelecekte veritabanına bağlanabilir)
    oyunlar = [
        {
            'isim': 'Marshmellow run',
            'slug': 'marshmellow-run',
            'logo': 'oyunlar/marshmellow-run/logo.jpg',
            'kategori': ['catPopular', 'catKids', 'catAction']
        },
        {
            'isim': 'Ölkəni Tap',
            'slug': 'olkeni-tap-find-country',
            'logo': 'oyunlar/olkeni-tap-find-country/logo.jpg',
            'kategori': ['catPopular', 'catLogic']
        },
        {
            'isim': 'Marshmellow jetpack',
            'slug': 'marshmellow-jetpack',
            'logo': 'oyunlar/marshmellow-jetpack/logo.jpg',
            'kategori': ['catAction']
        },
        {
            'isim': 'Sudoku Challenge AZ',
            'slug': 'sudoku-challenge-az',
            'logo': 'oyunlar/sudoku-challenge-az/logo.jpg',
            'kategori': ['catLogic']
        },
        {
            'isim': 'Azərbaycan Nərdi',
            'slug': 'azerbaycan-nerdi',
            'logo': 'oyunlar/azerbaycan-nerdi/logo.jpg',
            'kategori': ['catLogic', 'catPopular']
        },
        {
            'isim': 'Şahmat',
            'slug': 'sahmat-chess',
            'logo': 'oyunlar/sahmat-chess/logo.jpg',
            'kategori': ['catLogic']
        }
    ]

    # Kategoriye göre filtreleme
    filtrelenmis_oyunlar = oyunlar if cat_slug == 'all' else [oyun for oyun in oyunlar if cat_slug in oyun['kategori']]

    context = {
        'oyunlar': filtrelenmis_oyunlar,
        'aktif_kategori': cat_slug,
        'sayfa_basligi': _('MİLLİ ƏYLƏNCƏ PORTALI') # Çeviri fonksiyonu
    }
    
    return render(request, 'index.html', context)
