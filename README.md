# D.Sondars.projektadarbs
## Nedaudz par kodu
Šī koda lietošanai ir nepieciešama selenium bibliotēka, to ieinstalēt ar pip install selenium.
Kā jau pēc bibliotēkas var spriest šis kods ir Webscrapers. Šī webscrapera galvenā misija ir atrast lētāko alkoholu no diviem interneta veikaliem - [Spirits and Wine](https://www.spiritsandwine.lv/en/) un [Latvijas balzāms](https://www.lbveikali.lv/).
(Vēlējos pievienot arī [Alkoutlet](https://alkoutlet.lv/), bet neizdevās). Šo misiju kods izdara pa pusei, tas nozīmē ka kods neizrēķinās pašu lētāko, bet gan parādīs visus dzērienus ar vienādu vai līdzīgu vārdu plus to tilpumus un cenu, un tad koda lietotājs var izvēlēties vai iet uz vienu vai otru veikalu pakaļ savam izvēlētajam dzērienam. Kā arī ja tiks ievadīts dzēriens kas ir pieejams vienā no veikaliem bet nav pieejams otrā, tad kods nevis izvadīs ka vienā no veikaliem nav pieejams, bet gan izvadīs produktus ko veikals piedāvā tā vietā.


## Koda lietošana 
Kā jau iepriekš minēju ir nepieciešams pievienot selenium bibliotēku. Kad tas ir izdarīts tad var iedarbināt kodu. Tiks atvērtas divas jaunas Google Chrome cilnas, bet pašlaik nekas ar tām nenotiks, lai varētu turpināt koda darbošanaos ir nepieciešams atgriezties pie termināla kurā būs izvadīts _Ievadiet dzēriena nosaukumu:_ šeit ir nepieciešams ievadīt vēlāmā dzēriena nosaukumu. Lai pēc iespējas labāk un ērtāk atrastu savu izvēlēto produktu, ir nepieciešams uzrakstīt pēc iespējas pilnāku dzēriena nosaukumu, piemēram, ja tiks ievadīts vienkārši **red label** tad tiks izvadīti vairāki dzērieni kuros ir šī vārda kombinācija, bet ja tiks ievadīts pilnais nosaukums **Johnnie Walker red label** tad tiks izvadīta tikai šo dzērienu informācijas.
Pie izvadītās informācijas tiks parādīts no kura veikala tas ņemts, produkta nosaukums, tilpums un beigu beigās cena.
