# Spiel mit KI

## Information

Dies ist das finale Spiel mit der KI. Leider war es uns nicht möglich die KI in eine Ausführbare Datei umzuwandeln. Allerdings sollte die KI so laufen wie gedacht, wenn die folgenden Abhängigkeiten installiert sind:

- Python Version 3.8.10
- Tensorflow Version 2.13.1
- Pygame

Um diese Abhängigkeiten zu installieren, sollte Python Version 3.10.8 unter Windows von [hier](https://www.python.org/downloads/release/python-3810/) heruntergeladen und installiert werden, bzw. unter Linux über den Packagemanager installiert werden.

Sobald Python installiert ist, kann es je nach Betriebsystem mit ```python```, ```python3``` oder ```py``` aufgerufen werden. Die funktionierende Schreibweise sollte in den folgenden Installationsanweisungen ersetzt werden:

```python -m pip install tensorflow```
```python -m pip install pygame```

Wenn Python 3.8.10 istalliert ist, sollte auch automatisch Tensorflow 2.13.1 installiert werden.

## Dateien

### main.py

Mit der Main Datei Kann das aktuell schlauste neuronale Netzwerk getestet werden. Dazu genügt der Aufruf:

```python main.py```

Da es leider bei jedem Aufruf des Programms kleine Unteschiede bei den Berechnungen der KI gibt, kommt es vor, dass die KI auch zu Beginn des Spiels Fehler macht. Durch wiederholtes Ausführen des Programms kann aber teilweise ein durchaus beachtlicher Fortschritt beobachtet werden.

### train.py

Mit dieser Datei wird die KI trainiert. In der Datei selbst sind die Modelle pro Generation und andere wichtige Einstellungen abgespeichert. Das aktuelle Modell kann mit diesem Aufruf weiter trainiert werden:

```python train.py```

Um die KI nur eine Generation lang zu trainieren kann hinter den Befehl als Parameter ```one_generation``` angefügt werden (mit einem Leerzeichen getrennt, also ```python train.py one_generation```).

Für ein Training, welches von Grund auf mit einem neuen Modell erfolgen soll, kann der Parameter ```from_scratch``` verwendet werden.

Der Parameter ```parallel``` ist zwar im Quellcode noch vorhanden, wurde allerdings aufgrund seiner Undurchsichtigkeit seit einigen Vorgängerversionen nicht weiter gepflegt.

### play.py

Diese Datei diente nur Testzwecken und sollte das Spiel ohne KI starten.