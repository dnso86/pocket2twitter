# pocket2tweet

A Python script to keep your followers updated about your reading-list!

It picks one of the articles from the linked Pocket account which is tagged as **twitter** for example and tweets a status update with it - then archives it.

## Introduction

I find the app called [Pocket](https://getpocket.com/) immensely useful to maintain an ever-growing reading list of interesting articles that I could access later anywhere on any platform. I also have an account on [Twitter](https://twitter.com/0d8x86) where I regularly post interesting articles relevant to my line of work. However in order to share items saved in Pocket on Twitter, a checkbox is ought to be checked each time - also, we may save items to our Pocket that wouldn't be relevant to our Twitter at all.

## Installation

1. Create an App on Twitter Developers [here](https://developer.twitter.com/en/apps), and make sure you have 
both _Consumer API keys_ and a read-write _Access token & access token secret_.

2. Create an Application on Pocket [here](https://getpocket.com/developer/apps/). Doesn't need to be public.

3. Get an _Access Token_ for Pocket based on your _Consumer Key_ - this is needed due to Pocket's Authentication API using OAuth 2.0 as detailed [here](https://getpocket.com/developer/docs/authentication). There is also an on-line tool for this task [here](http://reader.fxneumann.de/plugins/oneclickpocket/auth.php) but I haven't tried it yet.

5. Add the tokens to `config.py`.

6. Install `pocket-api` and `python-twitter` with: `pip install pocket-api python-twitter`

7. Run `pocket2tweet.py` each time when you'd like to update your followers `python pocket2tweet.py`.

8. You may obviously want to do the last automatically from [cron](https://crontab.guru/), or set up a [scheduled task](https://stackoverflow.com/questions/6568736/how-do-i-set-a-windows-scheduled-task-to-run-in-the-background) for it on Windows.

## Parameters

There are three optional command-line parameters:

* `--elapsed-hours`: how many hours to wait after your most recent tweet - exiting otherwise. Defaults to 24.
* `--article-tag`: which tag to look for in your Pocket. Default is **twitter**.
* `--random-delay`: a random delay of at most the specified minutes before doing anything

## Misc

### Legal

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

This project is not endorsed by the vendors of Pocket and Twitter in any way and use it only at your own responsibility.

### PRs are welcome - future ideas:

* Only archiving the Pocket item if **twitter** is the only single tag - otherwise only removing it.
