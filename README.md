# dd-discord-bot 
DD's personal Discord bot 

## Config files 
### `_config_discord_api.json` 
Go to https://discord.com/developers/applications/ 

- Applications 
- (Your Discord App) 
- Settings 
- Bot 
- **Token** 

### `_config_twitch_api.json` 
Go to https://dev.twitch.tv/console 

- Applications 
- Manage Application: (Your Twitch App) 
- **Client ID** and **Client Secret** 

## Creating the applications 
### Discord 
Go to https://discord.com/developers/applications/ 

- Create an application 
- Create a bot 
- Invite it to your guild 
- Copy the guild's ID and add it in the `guild_ids` of the commands you want 

The **Token** will be shown only once! However, you can reset it if needed. 

### Twitch 
https://dev.twitch.tv/console/apps 

- Register Your Application 
- Add a unique name 
- URL: you can put http://localhost:3000/auth/twitch/callback 
- Category: Website Integration
- Client Type: Confidential 

The **Client Secret** will be shown only once, **and it can't be reset**! 

