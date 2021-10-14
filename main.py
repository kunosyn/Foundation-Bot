# General Imports #
import random, discord, asyncio, ro_py, os;

# From Imports #
from datetime import datetime;
from ro_py import Client;
from server import ping_server;

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

    a = discord.Game("with SCP-999.");
    await bot.change_presence(status = discord.Status.do_not_disturb, activity = a);

@bot.event
async def on_message(message):
    msg = message.content.lower();

    if msg == ">o5-x" or msg == ">gay" or msg == ">x":
        arr = ["O5-X is gay.", "Juan."];
        string = random.choice(arr);
        await message.channel.send(string);
    elif msg == ">kuno" or msg == ">the administrator" or msg == ">ta":
        await message.channel.send("Kuno is a woman.");
    elif msg == ">forest" or msg == ">maverick":
        await message.channel.send("https://cdn.discordapp.com/attachments/743511509677637773/893346818929328148/emo-meme-logan-paul.png");
    else:
        pass;

    await bot.process_commands(message);

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

        x = get(bot.get_all_members(), id = 512659924073840644);
        dm = await x.create_dm();

        dm.send(f"yo bruh we got a problem chief \n\nerror: {error}");
    elif isinstance(error, commands.UserInputError):
        em = discord.Embed(title = "***invalid arguments:***", description = f"*error:* {error}", color = colors["err"]);

        await ctx.send(embed = em);
    elif isinstance(error, asyncio.TimeoutError):
        em = discord.Embed(title = "***timed out:***", description = "*error: you took to long to reply to the message as a result the command has timed out, please re run the command if you wish to continue.*", color = colors["err"]);

        await ctx.send(embed = em);

# BOT EVENTS END #


# BOT COMMANDS START # 
group_id = 7434501;
log_chan = 0;

@bot.command(name = "help")
async def help(ctx):
    help_embed = discord.Embed(title = "***help:***", color = discord.Color.from_rgb(255, 255, 255));

    help_embed.add_field(name = "**info**", value = "*shows info about the bot*", inline = False);
    help_embed.add_field(name = "**whois || about**", value = "*displays roblox info about given user.\nargs: roblox username - str*", inline = False);
    help_embed.add_field(name = "**promote || promo**", value = "*promotes given user in group*\nargs: roblox username - str*", inline = False);
    help_embed.add_field(name = "**demote**", value = "*demotes given user in group*\nargs: roblox username - str*", inline = False);
    help_embed.add_field(name = "**rank**", value = "*sets rank of given user in group*\nargs: roblox username - str, rank id - int*", inline = False);
    help_embed.add_field(name = "**shout**", value = "*sets current group shout to given arguments.\nargs: shout*", inline = False);
    help_embed.add_field(name = "**ranks**", value = "*displays all ranks(roles) in group.*", inline = False);
    help_embed.add_field(name = "**exile**", value = "*exiles given user from group.\nargs: roblox username - str*", inline = False);
    help_embed.add_field(name = "**kick**", value = "*kicks mentioned user from server.\nargs: user - discord mention(discord user), reason(optional)*", inline = False);
    help_embed.add_field(name = "**ban**", value = "*bans mentioned user from server.\nargs: user - discord mention(discord user), reason(optional)*", inline = False);

    await ctx.send(embed = help_embed);

# Misc CMDs #

@bot.command(name = "kuno", aliases = ["maverick", "forest", "x", "o5-x", "the administrator", "ta", "gay"])
async def meme():
    pass;

@bot.command(name = "dm", aliases =  ["send"])
async def dm(ctx, member: discord.Member, *args):
    if args[0]:
        try:
            dm = await member.create_dm();
            em = discord.Embed(title = args[0], description = " ".join(args[1:]), color = colors["mod"]);

            await dm.send(embed = em);
        except Exception as err:
            error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

            await ctx.send(embed = error_embed);

@bot.command(name = "apply")
async def apply(ctx, level_num: int):
    await ctx.send(ctx.author.roles)

    if level_num == 0 and "Class Disposable" in ctx.author.roles:
        try:
            answers = [];
            questions = ["Explain in your own words what the meaning of SCPF is.", "Who in the lored was the found of the SCPF anf where was it founded?", "By gaining L0 how could you benefit the Foundation.", "What department are you going to try for?"];

            for question in questions:
                dm = await ctx.author.create_dm();
                em = discord.Embed(title = f"***question {questions.index(question)}:***", description = f"*{question}*");
                await dm.send(embed = em);
                
                response = await client.wait_for('message', check = lambda message: message.author == ctx.author);

                answers.append(response);

            em = discord.Embed(title = f"***{ctx.author.name}\'s application:***", color = discord.Color.from_rgb(255, 255, 255))

            for x in range(3):
                em.add_field(name = f"***question {x}:***", value = "QUESTION HERE: ");
                
        except Exception as err:
            em = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);
            
            dm = await ctx.author.create_dm();
            await dm.send(embed = em);
    elif level_num == 1:
        pass;

@bot.command(name = "info")
async def info(ctx):
    infoE = discord.Embed(title = "***Info:***", description = "**Programmers:** *`O5-X (ry_nt), The Administrator (kunostaken)`*\n**Head Programmer:** *`The Administrator (kunostaken)`*\n **Language:** *`Python`*\n**Version:** *`69.420`*", color = discord.Color.from_rgb(255, 255, 255));

    await ctx.send(embed = infoE);

# RBX CMDs #
@bot.command(name = "whois", aliases = ["about"])
async def whois(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user =  await group.get_member_by_username(roblox_username);
        rank = user.role;
        followers = await user.get_followers_count();
        friends = await user.get_friends_count();
        status = await user.get_status();

        whois_embed = discord.Embed(title = f"*** Whois {user.name}***", description = f"*Status: `{status}`\n\nRank: `{rank.name}`\n\nFollowers: `{followers}`\n\nFriends: `{friends}`*", color = discord.Color.from_rgb(255, 255, 255));

        await ctx.send(embed = whois_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

@bot.command(name = "ranks")
async def ranks(ctx):
    try:
        group = await rbx.get_group(group_id);
        roles = await group.get_roles();
        
        roles_embed = discord.Embed(title = "**ranks:**", color = discord.Color.from_rgb(255, 255, 255));
        
        for role in roles:
            roles_embed.add_field(name = f"**{role.name}**", value = f"*rank id: `{role.rank}`\nrbx id: `{role.id}`*", inline = True);
        
        await ctx.send(embed = roles_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "**error:**", description = f"*error - `{err}`*");

        await ctx.send(embed = error_embed);

@bot.command(name = "class-e", aliases = ["ce"])
@commands.has_any_role("The Administrator", "O5-X", "O5 COUNCIL")
async def class_e(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user = await group.get_member_by_username(roblox_username);

        await user.setrole(2);

        em = discord.Embed(title = f"***class e'd {roblox_username}:***", description = f"*class-e success!*");

        await ctx.send(embed = em);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

@bot.command(name = "promote", aliases = ["promo"])
@commands.has_any_role("The Administrator", "O5-X", "O5 COUNCIL")
async def promote(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user = await group.get_member_by_username(roblox_username);
        old_rank = user.role;

        await user.promote();
        await user.update_role();

        rank_embed = discord.Embed(title = f"***promoted {user.name}***", description = f"*user: `{user.name}`\n\nold rank: `{old_rank.name}`\n\nnew rank: `{user.role.name}`*");

        rank_embed.set_footer(text = f"Command executed by {ctx.author.name}.");

        await ctx.send(embed = rank_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

@bot.command(name = "demote")
@commands.has_any_role("The Administrator", "O5-X", "O5 COUNCIL")
async def demote(ctx, roblox_username: str):
    try:
        group = await rbx.get_group(group_id);
        user = await group.get_member_by_username(roblox_username);
        old_rank = user.role;
        await user.demote();
        await user.update_role();
        
        rank_embed = discord.Embed(title = f"***Demoted {user.name}***", description = f"*user: `{user.name}`\n\nold rank: `{old_rank.name}`\n\nnew rank: `{user.role.name}`*", color = discord.Color.from_rgb(50, 168, 82));

        rank_embed.set_footer(text = f"command executed by {ctx.author.name}.");

        await ctx.send(embed = rank_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        await ctx.send(embed = error_embed);

@bot.command(name = "rank")
@commands.has_any_role("The Administrator", "O5-X", "O5 COUNCIL")
async def rank(ctx, roblox_username: str, rank_id: int):
    valid_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    if rank_id in valid_ids:
        try:
            group = await rbx.get_group(group_id);
            user = await group.get_member_by_username(roblox_username);
            old_rank = user.role;
            await user.setrole(rank_id);
            await user.update_role();

            rank_embed = discord.Embed(title = f"***{user.name}***", description = f"*user: `{user.name}`\n\nold rank: `{old_rank.name}`\n\nnew rank: `{user.role.name}`*");

            rank_embed.set_footer(text = f"command executed by {ctx.author.name}.");

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
@commands.has_any_role("The Administrator", "O5-X", "O5 COUNCIL")
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
@commands.has_any_role("The Administrator", "O5-X", "O5 COUNCIL")
async def kick(ctx, member : discord.Member, *args):
    try:
        given_reason = " ".join(args[0:]);
        dm = await member.create_dm();

        if given_reason == None or given_reason == "" or given_reason == " ":
            given_reason = "breaking the rules.";

        notify_embed = discord.Embed(title = f"***moderation notice:***", description = f"you have been kicked from {ctx.guild.name}.\n\nreason: {given_reason}", color = colors['mod'])

        try:
            await dm.send(embed = notify_embed);
        except:
            pass;

        await member.kick(reason = given_reason);

        kicked_embed = discord.Embed(title = "***moderation:***", description = f"*kicked: {member.mention}\nReason: `{given_reason}`*", color = colors["mod"]);

        kicked_embed.set_footer(text = f"sent at: {timestamp}");

        await ctx.send(embed = kicked_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        error_embed.set_footer(text = f"sent at: {timestamp}");
          
        await ctx.send(embed = error_embed);

@bot.command(name = "ban")
@commands.has_any_role("The Administrator", "O5-X", "O5 COUNCIL")
async def ban(ctx, member: discord.Member, *args):
    try:
        given_reason = " ".join(args[0:]);
        dm = await member.create_dm();

        if given_reason == None or given_reason == "" or given_reason == " ":
            given_reason = "breaking the rules.";

        notify_embed = discord.Embed(title = f"moderation notice:", description = f"you have been banned from {ctx.guild.name}.\n\nreason: {given_reason}", color = colors['mod'])

        try:
            await dm.send(embed = notify_embed);
        except: 
            pass;
        await member.ban(reason = given_reason);

        banned_embed = discord.Embed(title = "***moderation:***", description = f"*banned: {member.mention}\nreason: `{given_reason}`*", color = colors["mod"]);

        banned_embed.set_footer(text = f"sent at: {timestamp}");

        await ctx.send(embed = banned_embed);
    except Exception as err:
        error_embed = discord.Embed(title = "***error:***", description = f"*error - `{err}`*", color = colors["err"]);

        error_embed.set_footer(text = f"sent at: {timestamp}");

        await ctx.send(embed = error_embed);
# BOT COMMANDS END #


ping_server();
bot.run(os.environ['TOKEN'])