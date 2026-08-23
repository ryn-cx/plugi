# Plugi

Tubi API wrapper.

```python
from plugi import Plugi

client = Plugi()

series = client.content("300018492")
print(series.title)
for season in series.children or []:
    for episode in season.children or []:
        print(season.title, episode.episode_number, episode.title)

results = client.search("drago")
for container in results.containers or []:
    print(container.id, [item.id for item in container.items or []])
```

Each endpoint is also two halves: `client.content.download(id)` returns the
response as text and `client.content.load(text)` reads text into the model.
