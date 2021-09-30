# General Imports #
import discord, os, time, ro_py, random;

# From Imports #
from datetime import datetime;
from ro_py import Client;

# Discord Imports #
import discord.ext;
from discord.utils import get;
from discord.ext import commands, tasks;
from discord.ext.commands import has_permissions,  CheckFailure, check;


# Initializing Classes #
client = discord.Client();
bot = commands.Bot(command_prefix = os.environ["PREFIX"], case_insensitive = True, help_command = None);
rbx = Client(os.environ["COOKIE"]);

# Defining Essential Variables #
now = datetime.now();
timestamp = now.strftime("%H:%M");
colors = {"mod": discord.Color.from_rgb(87, 64, 255), "err": discord.Color.from_rgb(250, 65, 77)};


# BOT EVENTS START #
@bot.event
async def on_ready():
    os.system("clear");
    print(f"\u001b[32m- Logged in as {bot.user}.");
    print(f"\u001b[32m- Login time {timestamp}.");
    print("\u001b[37m--------------------------------------\n");
    a = random.choice([discord.Game(name = "with SCP-999"), discord.Streaming(name = "your bedroom"), discord.Activity(type = discord.ActivityType.listening, name = os.environ["PREFIX"])]);
    await client.change_presence(status = discord.Status.do_not_disturb, activity = a);

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title = "***command not found:***", description = f"*the command you have entered is an invalid command, use {os.environ['PREFIX']}help for the list of commands.*", color = colors["err"]);

        await ctx.send(embed = em);
    elif isinstance(error, commands.MissingAnyRole) or isinstance(error, commands.MissingPermissions):
        em = discord.Embed(title = "***invalid permissions.***", description = "*error, you are missing the required permissions to execute this command.*", color = colors["err"]);

        await ctx.send(embed = em);
    elif isinstance(error, commands.BotMissingPermissions):
        dm = await ctx.guild.owner.create_dm();

        dm.send(f"yo bruh we got a problem chief \n\nerror: {error}");

        x = get(bot.get_all_members(), id = "0"); # put ur id in place of the 0

        dm = await x.create_dm();

        dm.send(f"yo bruh we got a problem chief \n\nerror: {error}");
    elif isinstance(error, commands.UserInputError):
        em = discord.Embed(title = "***invalid arguments:***", description = f"*error:* {error}", color = colors["err"]);

        await ctx.send(embed = em);
# BOT EVENTS END #


# BOT COMMANDS START # 

@bot.command(name = "help")
async def help(ctx):
    help_embed = discord.Embed(title = "***help:***", color = discord.Color.from_rgb(255, 255, 255));

    help_embed.add_field(name = "**info**", value = "*shows info about the bot*");
    help_embed.add_field(name = "**whois || about**", value = "*displays roblox info about given user.\nargs: roblox username - str*");
    help_embed.add_field(name = "**promote || promo**", value = "*promotes given user in group*\nargs: roblox username - str*");
    help_embed.add_field(name = "**demote**", value = "*demotes given user in group*\nargs: roblox username - str*");
    help_embed.add_field(name = "**rank**", value = "*sets rank of given user in group*\nargs: roblox username - str, rank id - int*");
    help_embed.add_field(name = "**shout**", value = "*sets current group shout to given arguments.\nargs: shout*");
    help_embed.add_field(name = "**ranks**", value = "*displays all ranks(roles) in group.*");
    help_embed.add_field(name = "**exile**", value = "*exiles given user from group.\nargs: roblox username - str*");
    help_embed.add_field(name = "**kick**", value = "*kicks mentioned user from server.\nargs: user - discord mention(discord user), reason(optional)*", inline = True);
    help_embed.add_field(name = "**ban**", value = "*bans mentioned user from server.\nargs: user - discord mention(discord user), reason(optional)*");

    await ctx.send(embed = help_embed);

# Fun CMDs #
@bot.command(name = "gay", aliases = ["o5-x", "x"])
async def gay(ctx):
    await ctx.send("O5-X is gay.");

# Misc CMDs #
@bot.command(name = "info")
async def info(ctx):
    infoE = discord.Embed(title = "***Info:***", description = "**Programmers:** *`O5-X (ry_nt), The Administrator (kunostaken)`*\n**Head Programmer:*** *`The Administrator (kunostaken)`\n***Language:** *`Python`*\n**Version:** *`69.420`*", color = discord.Color.from_rgb(255, 255, 255));

    await ctx.send(embed = infoE);

# RBX CMDs #
group_id = 0;

@bot.command(name = "whois", aliases = ["about"])
async def whois(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user =  await group.get_member_by_username(roblox_username);
        rank = user.role;
        followers = await user.get_followers_count();
        following = await user.get_following_count();
        friends = await user.get_friends_count();
        status = await user.get_status();

        whois_embed = discord.Embed(title = f"*** Whois {user.name}***", description = f"*Status: `{status}`\n\nRank: `{rank.name}`\n\nFollowers: `{followers}`\n\nFollowing: `{following}`\n\nFriends: `{friends}`*", color = discord.Color.from_rgb(255, 255, 255));

        await ctx.send(embed = whois_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

@bot.command(name = "ranks")
async def ranks(ctx):
    try:
        group = await rbx.get_group(group_id);
        roles = await group.get_roles();
        
        roles_embed = discord.Embed(title = "**rank:**", color = discord.Color.from_rgb(255, 255, 255));
        
        for role in roles:
            roles_embed.add_field(name = f"**{role.name}**", value = f"*id: `{role.id}`*");
        
        await ctx.send(embed = roles_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "**error:**", description = f"*error - `{err}`*");

        await ctx.send(embed = error_embed);
            
@bot.command(name = "promote", aliases = ["promo"])
@commands.has_any_role("The Administrator", "O5-X", "O5 Council")
async def promote(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user = await group.get_member_by_username(roblox_username);
        old_rank = user.role;
        await user.promote();
        await user.update_role();

        rank_embed = discord.Embed(title = f"***Promoted {user.name}***", description = f"*user: `{user.name}`\n\nold rank: `{old_rank.name}`\n\nnew rank: `{user.role.name}`*");

        rank_embed.set_footer(text = f"Command executed by {ctx.author.name}.");

        await ctx.send(embed = rank_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

@bot.command(name = "demote")
@commands.has_any_role("The Administrator", "O5-X", "O5 Council")
async def demote(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user = await group.get_member_by_username(roblox_username);
        old_rank = user.role;
        await user.demote();
        await user.update_role();

        rank_embed = discord.Embed(title = f"***Demoted {user.name}***", description = f"*user: `{user.name}`\n\nold rank: `{old_rank.name}`\n\nnew rank: `{user.role.name}`*");

        rank_embed.set_footer(text = f"Command executed by {ctx.author.name}.");

        await ctx.send(embed = rank_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

@bot.command(name = "rank")
@commands.has_any_role("The Administrator", "O5-X", "O5-Council")
async def rank(ctx, roblox_username: str, rank_id: int):
    valid_ids = [];
    if rank_id in valid_ids:
        try:
            group = await rbx.get_group(group_id);
            user = await group.get_member_by_username(roblox_username);
            old_rank = user.role;
            await user.setrank(rank_id);
            await user.update_role();

            rank_embed = discord.Embed(title = f"***{user.name}***", description = f"*user: `{user.name}`\n\nold rank: `{old_rank.name}`\n\nnew rank: `{user.role.name}`*");

            rank_embed.set_footer(text = f"Command executed by {ctx.author.name}.");

            await ctx.send(embed = rank_embed);
        except Exception as err:
            error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

            await ctx.send(embed = error_embed);
    else:
        error_embed = discord.Embed(title = "***error:***", description = "*error: the id you entered was not a valid rank id, please use the `ranks` command to see all valid id\'s*");

        await ctx.send(embed = error_embed);

@bot.command(name = "shout")
@commands.has_any_role("The Administrator", "O5-X")
async def shout(ctx, *args):
  try:
      group = await rbx.get_group(group_id);
      old_shout = group.shout;
      new_shout = " ".join(args);
      await group.update_shout(new_shout);
      em = discord.Embed(title = "***Shout Success:***", description = f"*old shout: `{old_shout}`\n\nnew shout: `{new_shout}`*")
  except Exception as err:
      em = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);
  finally:
      return await ctx.send(embed = em);

@bot.command(name = "exile")
@commands.has_any_role("The Administrator", "O5-X", "O5 Council")
async def exile(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user = await group.get_member_by_username(roblox_username);
        await user.exile();

        exile_embed = discord.Embed(title = f"***exiled {user.name}***", description = f"*i have successfully exiled the given user from the group.*", color = discord.Color.from_rgb(255, 255, 255));

        await ctx.send(embed = exile_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

# Mod CMDs #
@bot.command(name = "kick", aliases = ["boot", "italy", "shapeofitaly"])
@commands.has_any_role("The Administrator", "O5-X", "O5 Council")
async def kick(ctx, member : discord.Member, *args):
    try:
        given_reason = " ".join(args[0:]);
        dm = await member.create_dm();

        if given_reason == None:
            given_reason = "breaking the rules.";

        notify_embed = discord.Embed(title = f"moderation notice:", description = f"you have been kicked from {ctx.guild.name}.\n\nreason: {given_reason}", color = colors['mod'])

        await dm.send(embed = notify_embed);
        await member.kick(reason = given_reason);

        kicked_embed = discord.Embed(title = "**moderation:***", description = f"*kicked: {member.mention}\nReason: `{given_reason}`*", color = colors["mod"]);

        kicked_embed.set_footer(text = f"sent at: {timestamp}");

        await ctx.send(embed = kicked_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        error_embed.set_footer(text = f"sent at: {timestamp}");
          
        await ctx.send(embed = error_embed);

@bot.command(name = "ban")
@commands.has_any_role("The Administrator", "O5-X", "O5 Council")
async def ban(ctx, member: discord.Member, *args):
    try:
        given_reason = " ".join(args[0:]);
        dm = await member.create_dm();

        if given_reason == None:
            given_reason = "breaking the rules.";

        notify_embed = discord.Embed(title = f"moderation notice:", description = f"you have been banned from {ctx.guild.name}.\n\nreason: {given_reason}", color = colors['mod'])

        await dm.send(embed = notify_embed);
        await member.ban(reason = given_reason);

        banned_embed = discord.Embed(title = "***moderation:***", description = f"*banned: {member.mention}\nreason: `{given_reason}`*", color = colors["mod"]);

        banned_embed.set_footer(text = f" Sent at: {timestamp}");

        await ctx.send(embed = banned_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        error_embed.set_footer(text = f"sent at: {timestamp}");

        await ctx.send(embed = error_embed);
# BOT COMMANDS END #

bot.run(os.environ['TOKEN'])