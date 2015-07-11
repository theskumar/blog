Title: How to setup an IRC channel properly
Slug: irc
Date: 2015-06-16 01:03:10
Tags: irc, communication
Status: draft
Category: software
Summary: If you need to create a new IRC channel for your community, how to set it up safely and securely.

# Creating a channel 

Creating a new channel is as simple as typing the following IRC command from anywhere:

```
/join #<channel_name>
```


# Inviting people to join channel 

```
/invite <usernmae> #<channel_name>
```


# Protecting the channel against takeover

ChanServ is a network service provided by some IRC networks. Channel takeovers are virtually impossible when a channel is registered with ChanServ.
```
/msg ChanServ register #<channel_name>
```
```
/msg ChanServ set #<channel_name> guard on
```

## Set channel topic

```
/topic #<channel_name> NEW TOPIC
```

__References__

http://www.wikihow.com/wikiHow:IRC-Cheat-Sheet
http://www.wikihow.com/Add-ChanServ-to-Your-IRC-Channel-on-Freenode
