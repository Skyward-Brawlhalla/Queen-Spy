# Queen Spy Documentation 
In short, Queen Spy manages the links between brawlhalla and discord accounts. This helps to see if there are currently people in the discord with the clan role that shouldn't have the clan role.

## Commands
- [Prefix](#prefix)
- [Command Logic](#command-logic)
- [Clan](#clan-commands)
  - [Update Clan Data](#update-clan-data)
  - [Get Clan List](#get-clan-list)
- [Discord](#discord-commands)
  - [Update Discord Data](#update-discord-data)
  - [Get Discord List](#get-discord-list)
- [Linking](#linking-commands)
  - [Add Link](#add-link)
  - [Remove Link](#remove-link)
  - [Get Link List](#get-link-list)
- [Extra](#extra-commands)

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

## Update Clan Data
`qsupcl` updates the clan data. Take note that Brawlhalla doesn't update their data in real time, so it might take up to 15 mintues for data to get updated in the Brawlhalla database. To solve this update clan data again in 15 minutes. Don't overuse this command since we might get a timeout from the Brawlhalla API.

## Get Clan List
`qslscl` return a list of all clan members in game. Don't forget to first update the data using `qsupcl`.

# Discord Commands
In this section we'll cover all discord related commands

## Update Discord Data
`qsupdc` / `qsupdi` updates the discord data.

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

## Get Link List

# Extra
