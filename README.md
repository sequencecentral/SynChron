# Synchronicity2
Synchronicity was taken
Package contains modules for interacting with online media sources. We call them widgets. They can either send or receive data. This will be more applicable in some cases than others.

- update() - function which retrieves a single update in the format of a dict
- get_multiple(count) - function which retrieves multiple updates in the above format. You can usually use the count parameter with update function as well, but keepign this one in for clarity and compatibility.

## rsswidget 
- Use this whenever possible. It's simplest to get an rss feed if one is available. 