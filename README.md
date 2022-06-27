# Queen Spy Documentation 
In short, Queen Spy manages the links between brawlhalla and discord accounts. This helps to see if there are currently people in the discord with the clan role that shouldn't have the clan role.

## Commands
- [Prefix](#prefix)
- [How to use](#how-to-use)
- [Command Logic](#command-logic)
- [Clan](#clan-commands)
  - [Get Clan List](#get-clan-list)
- [Discord](#discord-commands)
  - [Get Discord List](#get-discord-list)
- [Linking](#linking-commands)
  - [Add Link](#add-link)
  - [Remove Link](#remove-link)
  - [Get Link List](#get-link-list)
- [Extra](#extra-commands)

# How to use

# Prefix
Both `qs` and `Qs` work.

# Command Logic
A command consists of 2 letters after each other multiple times.

**Example 1**

`qsupcl` stands for 

- qs -> queen spy

- up -> update

- cl -> clan

**Example 2**

`qslsdc` stands for

- qs -> queen spy

- ls -> list

- dc -> discord

# Clan Commands
In this section we'll cover all clan related commands

## Get Clan List
`qslscl` return a list of all clan members in game.

# Discord Commands
In this section we'll cover all discord related commands

## Get Discord List
`qslsdc` / `qslsdi` returns a list of everyone in the discord with the `@Clan Member` role.

# Linking
In this section we'll cover all account linking related commands

## Add Link
`qsadli` / `qsaddli` / `qsali` creates a new link. Keep in mind that you have to provide parameters.

**Example**

`qsadli brawlhalla_id discord_id`

`qsadli 7364605 413070742591373314`

Bot will respond with 

`Are you sure you want to add the following link?`

```py
brawlhalla_id: 7364605
brawlhalla_name: CrossyChainsaw
discord_id: 413070742591373314
discord_name: CrossyChainsaw
```
`Send y to confirm or n to cancel.`

type `y` to confirm and `n` to cancel.

now type `qslsli` to get the list with links. You'll see the new link is added.

## Remove Link
`qsrmli brawlhalla_id` with this command you can remove an existing link, just like adding a link, it will ask for confirmation.

## Get Link List
`qslsli` shows a list of all current links between discord and brawlhalla.

# Extra
`qssay message` makes the bot say something.

`qshelp` sends link to this page.

`qsmeme` sends a queen nai meme.
