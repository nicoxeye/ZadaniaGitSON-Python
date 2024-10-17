polecenia: 

Zaimplementuj w pythonie, stwórz repozytorium, poużywaj gita: 

1. Pierwszą rzeczą, jaką musi zrobić system sterowania, jest sprawdzenie, czy reaktor jest zrównoważony w stanie krytycznym. Mówi się, że reaktor jest krytyczny, jeśli spełnia następujące warunki:

Temperatura jest niższa niż 800 K.
Liczba neutronów emitowanych na sekundę jest większa niż 500.
Iloczyn temperatury i liczby neutronów emitowanych na sekundę jest mniejszy niż 500000.
Zaimplementuj funkcję is_criticality_balanced(), która przyjmuje temperaturę mierzoną w kelwinach i liczbę emitowanych neutronów jako parametry i zwraca True, jeśli warunki krytyczności są spełnione, a False, jeśli nie.

2. Gdy reaktor zacznie wytwarzać energię, należy określić jego sprawność. Sprawność można podzielić na 4 zakresy:

zielony -> sprawność 80% lub więcej,
pomarańczowy -> sprawność poniżej 80%, ale co najmniej 60%,
czerwony -> sprawność poniżej 60%, ale nadal 30% lub więcej,
czarny -> wydajność poniżej 30%.
Wartość procentową można obliczyć jako (generated_power/theoretical_max_power)*100, gdzie generated_power = voltage * current. Należy pamiętać, że wartość procentowa zwykle nie jest liczbą całkowitą, więc należy pamiętać o prawidłowym użyciu porównań < i <=.

Zaimplementuj funkcję reactor_efficiency(<voltage>, <current>, <theoretical_max_power>) z trzema parametrami: voltage, current i theoretical_max_power. Funkcja ta powinna zwracać pasmo sprawności dławika: „zielone”, „pomarańczowe”, „czerwone” lub „czarne”.

3. Ostatnie zadanie polega na stworzeniu mechanizmu zabezpieczającego przed przeciążeniem i stopieniem reaktora. Mechanizm ten określi, czy reaktor znajduje się poniżej, na lub powyżej idealnego progu krytyczności. Krytyczność można następnie zwiększyć, zmniejszyć lub zatrzymać, wkładając (lub usuwając) pręty kontrolne do reaktora.

Zaimplementuj funkcję o nazwie fail_safe(), która przyjmuje 3 parametry: temperaturę mierzoną w kelwinach, neutrony_produkowane_na_sekundę i próg, a następnie generuje kod stanu reaktora.

Jeśli wartość temperature * neutrons_produced_per_second < 90% wartości progowej, wyprowadzany jest kod stanu „LOW” wskazujący, że pręty kontrolne muszą zostać usunięte w celu wytworzenia energii.

Jeśli wartość temperature * neutrons_produced_per_second mieści się w zakresie 10% wartości progowej (czyli albo 0-10% mniej niż wartość progowa, na poziomie wartości progowej, albo 0-10% więcej niż wartość progowa), reaktor jest w stanie krytycznym i powinien zostać wysłany kod stanu „NORMAL”, wskazujący, że reaktor jest w optymalnym stanie, a pręty sterujące znajdują się w idealnym położeniu.
