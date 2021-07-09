Awesome CLI
===========

Awesome List in CLI search (WIP)


✨✨✨ *So Awesome* ✨✨✨


Current *Awesome* Support:

* [agarrharr/awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)


Quick Start
-----------

Interactive query

```
$ awesome-cli -i
Please select one section to show: 18.  - Time Tracking (5) [RET]
                00.  Entertainment (3)                     15.  - Npm (7)                             30.  - Markdown (3)                        45.  Version Control (1)
                01.  - Music (14)                          16.  - Boilerplate (5)                     31.  Command Line Learning (9)             46.  - Git (18)
                02.  - Social Media (7)                    17.  Productivity (14)                     32.  Data Manipulation (1)                 47.  Images (0)
                03.  - Video (5)                           18.  - Time Tracking (5)                   33.  - Processors (5)                      48.  - Gif Creation (7)
                04.  - Movies (2)                          19.  - Note Taking and Lists (10)          34.  - JSON (6)                            49.  - Image Conversion (3)
                05.  - Games (2)                           20.  - Finance (4)                         35.  - Columns (2)                         50.  - SVG (1)
                06.  - Books (3)                           21.  - Presentations (4)                   36.  - Text (2)                            51.  Screensavers (4)
                07.  Development (9)                       22.  - Calendars (5)                       37.  Files and Directories (0)             52.  Graphics (3)
                08.  - Text Editors (5)                    23.  Utilities (12)                        38.  - File Managers (6)                   53.  Just for Fun (9)
                09.  - Web Development (19)                24.  - macOS (11)                          39.  - Deleting, Copying, and Renaming (7) 54.  Other (24)
                10.  - Mobile Development (3)              25.  - Terminal Sharing Utilities (10)     40.  - Files (10)                          55.  - Emoji (5)
                11.  - Database (5)                        26.  - Network Utilities (6)               41.  - File Sync/Sharing (5)               56.  Other Awesome Lists (7)
                12.  - Devops (9)                          27.  - Theming and Customization (6)       42.  - Directory Listing (4)
                13.  - Docker (5)                          28.  - Shell Utilities (6)                 43.  - Directory Navigation (9)
                14.  - Release (5)                         29.  - System Interaction Utilities (7)    44.  - Search (8)

- 💥 Time Tracking
Timetrap - Simple timetracker.
🔗 https://github.com/samg/timetrap
moro - Simple tool for tracking work hours.
🔗 https://github.com/omidfi/moro
Timewarrior - Utility with simple stopwatch, calendar-based backfill and flexible reporting.
🔗 https://github.com/GothenburgBitFactory/timewarrior
Watson - Generate reports for clients and manage your time.
🔗 https://github.com/TailorDev/Watson
utt - Simple time tracking tool.
🔗 https://github.com/larose/utt
```

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
