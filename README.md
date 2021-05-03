# SynChron
Synchronicity (German: Synchronizität) is a concept first introduced by analytical psychologist Carl G. Jung "to describe circumstances that appear meaningfully related yet lack a causal connection.Jung held that to ascribe meaning to certain acausal coincidences can be a healthy, even necessary, function of the human mind—principally, by way of bringing important material of the unconscious mind to attention. This further developed into the view that there is a philosophical objectivity or suprasubjectivity to the meaningfulness of such coincidences, as related to the collective unconscious.

Package contains modules for interacting with online media sources. We call them widgets. They can either send or receive data. This will be more applicable in some cases than others.

- update() - function which retrieves a single update in the format of a dict
- get_multiple(count) - function which retrieves multiple updates in the above format. You can usually use the count parameter with update function as well, but keepign this one in for clarity and compatibility.

## rsswidget 
- Use this whenever possible. It's simplest to get an rss feed if one is available. 