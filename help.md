install nltk
```pip install nltk```

```import nltk
nltk.download()```


start/stop mongo:
```
brew services start mongodb-community
brew services stop mongodb-community

mongod --config /usr/local/etc/mongod.conf --fork
```

install pymongo
```python -m pip install pymongo```

insert csv file
```
mongoimport --db mean --collection movies-subs --type=csv --headerline --file=movies_subtitles.csv
```