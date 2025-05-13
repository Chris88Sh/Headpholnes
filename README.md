# Noslēguma projekts

## $${\color{lightblue}Noslēguma \space projektā \space uzdevums}$$

Šaja projekta galvenais uzdevums ir spēja analīzet un atlasīt datus no Euronics.lv vietnes(programma paredzēta bezvādu austiņas meklēšanai). Programma automatiski ielādē lapas saturu un uz ekrāna izvada preces nosaukumu un cenu. Uzdevuma mērķis ir paradīt vienu no _tīmekļa skrāpēšanas(**web scrapping**)_ piemēriem.

## $${\color{orange}Python \space bibliotēkas}$$

Izstrādes laikā tiek izmantotas trīs bibliotēkas - **requests**, **bs4(BeautifulSoup)** un **csv**. Bibliotēka _**requests**_ tiek izmantota, lai nosūtītu HTTP pieprasījumu uz Euronics mājaslapu un iegūtu HTML saturu. Bibliotēka _**bs4**_ tiek izmantota, lai strukturēti parsētu HTML saturu un meklētu konkrētus elementus (piemēram, produktu nosaukumus un cenas). Bibliotēka _**csv**_ ir nepieciešama datu glabāšanai atsevišķā csv formata failā.

## $${\color{green}Definētas \space datu \space struktūras}$$

Kodā bija izveidots saraksts preces = [] un vārdnica produkts {}. Sarakstā _**preces**_ tiek glabāta vārdnīca _**produkts**_, kura bija izveidota ar atslēgvārdiem _nosaukums_ un _cena_. Pie csv faila bija izveidots vērtību saraksts "laukus_vardi" lai nosauktu kolonnu nosaukumus.

## $${\color{wheat}Programmatūras \space izmantošanas \space metodes}$$

Kā jau iepriekš bija minēts, programmā tiek izmantota requests bibliotēka, lai nosūtītu HTTP pieprasījumu uz konkrētu URL, lai atlasītu vietnes datus. Lai izvairītos no tīmekļa pārlūkošanas bloķēšanas, tiek izmantota User-Agent galvene.
Bija izveidots mainīgais **product_cards**, kurš ir paredzēts data-product-id atrībūtu meklēšanai. Lai atrastu preces nosaukumu un preces cenas, tiek pārbaudīti dažādi selektori(piemēram, "product-title", "product-name", "price", "current-price"). Ja priekš nosaukumam selektori nebija atrasti, tad programma meklēs preces nosaukumus pie <"a"> elementa. Pie csv faila veidošanas bija izmantota metode with open() lai programma varētu atvert un aizvert failu automātiski. "mode = "w"" ir vajadzīgs priekš tam, lai pēc katras koda testēšanas informācija būs atjaunota un pārrakstīta. csv.DictWriter ir vajadzīgs, lai katru rindu piešķirt kā vārdnīcu ar atslēgvārdiem _"nosaukums"_ un _"cena"_.





