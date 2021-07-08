Awesome CLI
===========

Awesome List in CLI search (WIP)


✨✨✨ *So Awesome* ✨✨✨


Current *Awesome* Support:

* [agarrharr/awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)


Quick Start
-----------

Show all awesome list

```
$ awesome-cli
✨ Entertainment
football-cli - Get live scores, fixtures, standings of almost every football competition/league.
🔗 https://github.com/ManrajGrover/football-cli
pockyt - Read, Manage, and Automate your Pocket collection.
🔗 https://github.com/arvindch/pockyt
newsboat - An extendable RSS feed reader for text terminals.
🔗 https://github.com/newsboat/newsboat

- 💥 Music
cmus - Small, fast and powerful console music player.
...
```

Show header only

```
$ awesome-cli -k
✨ Entertainment
- 💥 Music
- 💥 Social Media
- 💥 Video
- 💥 Movies
- 💥 Games
- 💥 Books
✨ Development
- 💥 Text Editors
...
```

Don't show URL

```
$ awesome-cli -u
✨ Entertainment
football-cli - Get live scores, fixtures, standings of almost every football competition/league.
pockyt - Read, Manage, and Automate your Pocket collection.
newsboat - An extendable RSS feed reader for text terminals.

- 💥 Music
cmus - Small, fast and powerful console music player.
...
```

Install
-------

```
$ python -m pip install awesome-cli
```


Prerequirements
---------------

* poetry

Build
-----

```
$ poetry build
```

TODO
----

- [ ] Support multi awesome list
- [ ] Support search
- [ ] Support showing specific section only
