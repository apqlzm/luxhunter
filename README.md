# luxhunter

## Do czego to służy?
Bywa że musimy umówić się na wizytę do specjalisty lecz nie ma dostępnych wizyt w dogodnym terminie. Wtedy możemy ustawić luxhunter który będzie monitorował portal i informował nas w razie zwolnienia się wizyty.

## Konfiguracja
Skrypt należy ustawić w crontab z odpowiednimi parametrami. 
Na przykład:
*/1 * * * *  python /home/user/luxhunter/luxhunter.py login_do_portalu_luxmed haslodo_portalu_luxmed adres_email@powiadomienia.tu 2015-06-30 2015-07-02 4436 "" 1

Zadanie będzie sprawdzało co minutę czy zwolniło się miejsce do dowolnego lekarza ("") ze specjalizacją ortopeda (4436), w Warszawie (1). Powiadomienia będą wysyłane na adres adres_email@powiadomienia.tu
