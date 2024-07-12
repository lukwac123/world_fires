# Użycie danych w formacie CSV i przedstawienie ich na interaktywnej mapie świata.

Używamy danych zapisanych w formacie _*.csv_ z których w pierwszej kolejności pobieramy informację o długości i szerokości geograficznej,
w krórej doszło do pożaru, a takżę informację o jego sile / rozmiarze. W kolejnym etapie używając **modułu plotly.express** oraz korzystając 
z funkcji **scatter_geo** i możliwości dostosowania wyglądu mapy, ustawiamy stopniowanie siły pożaru (kolor od jasnoczerwony do ciemno czerwony) dodajemy skalę.
Mamy również możliwość zmiany wyglądu samej mapy za pomocą argumentu **projection**. Całość przedstawiona jest w przeglądarce internetowej. Mapa jest interaktywna 
co pozwala nam na wyświetlenie szczegółów dotyczących posszczególnych punktów na niej. Mapę możemy również przybliżać bądź oddalać. Poniżej przedstawione zostały
screeny z gotowego programu.

![world_fires](https://github.com/user-attachments/assets/60e09e83-b1c7-46d5-a363-7b64e92d4691)

<sup>Rysunek 1. Interaktywna mapa świata z pożarami jakie miały miejsce w dniu 03.04.2022.</sup>

![world_fires_zoom](https://github.com/user-attachments/assets/1e88e4a9-41f1-41b4-a0c9-283dee67c550)

<sup>Rysunek 2. Interaktywność mapy pozwala do powiększanie jej i odczytywanie szczegółów dla danego miejsca.</sup>
