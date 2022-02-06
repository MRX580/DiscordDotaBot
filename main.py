import discord
import setting
import random

ROLES = {
    '1️⃣': 939606779157966848,
    '2️⃣': 939607566911152199,
    '3️⃣': 939628630340927488,
    '4️⃣': 939628719654436864,
    '5️⃣': 939628793142861826,
}
from discord.ext import commands

heroStrength = ('Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner',
                'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker',
                'Elder Titan', 'Huskar', 'Io', 'Kunkka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci',
                'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Pudge', 'Sand King', 'Slardar', 'Snapfire',
                'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord',
                'Undying', 'Wraith King')

heroAgility = ('Anti-Mage', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Broodmother', 'Clinkz', 'Drow Ranger',
               'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Lone Druid', 'Luna', 'Medusa',
               'Meppo', 'Mirana', 'Monkey King', 'Morphling', 'Nyx Assasin', 'Pangolier', 'Phantom Assasin',
               'Phantom Lanser', 'Razor', 'Riki', 'Shadow Fiend', 'Slark', 'Sniper', 'Spectre', 'Templar Assasin',
               'Terrorblade', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomanser', 'Viper', 'Weaver')

heroIntelligence = ('Ancient Apparition', 'Bane', 'Batrider', 'Chen', 'Cristal Maiden', 'Dark Seer', 'Dark Willow',
                    'Dazzle', 'Death Prophet', 'Disraptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro',
                    'Keep Of The Light', 'Leshrak', 'Lich', 'Lina', 'Lion', 'Nature\'s Prophet', 'Necrophos',
                    'Ogre Magi', 'Oracle', 'Outworld Destroyer', 'Puck', 'Pugna', 'Queen Of Pain', 'Rubick',
                    'Shadow Demon', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Storm Spirit',
                    'Ebanaya Huinya(Techies)', 'Tinker', 'Visage', 'Void Spirit', 'Warlock', 'Windranger',
                    'Winter Wyvern', 'Withc Doctor', 'Zeus')

allHero = heroStrength + heroAgility + heroIntelligence

client = commands.Bot(command_prefix='/', intents = discord.Intents.all())


@client.event
async def on_ready():
    print('Bot connected')
    for guild in client.guilds:
        for member in guild.members:
            print(member.id)

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 939686135259619409:
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = discord.utils.get(message.guild.members,
                           id=payload.user_id)

        try:
            emoji = str(payload.emoji)
            role = discord.utils.get(message.guild.roles, id=ROLES[emoji])
            await payload.member.add_roles(role)
            print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
        except KeyError as e:
            pass
        except Exception as e:
            pass



@client.event
async def on_raw_reaction_remove(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    member = await (await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
    try:
        emoji = str(payload.emoji)
        role = discord.utils.get(message.guild.roles, id=ROLES[emoji])
        await member.remove_roles(role)

    except KeyError as e:
        pass
    except Exception as e:
        pass


try:
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(ctx, amount = 0):
        await ctx.channel.purge(limit=amount+1)
except discord.ext.commands.errors.MissingPermissions:
    pass


@client.command(pass_context=True)
async def rollhero(ctx, arg=None):
    if arg is None:
        await ctx.send(allHero[random.randint(0, len(allHero) - 1)])
    elif arg.lower() == 'сила':
        await ctx.send(heroStrength[random.randint(0, len(heroStrength) - 1)])
    elif arg.lower() == 'ловкость':
        await ctx.send(heroAgility[random.randint(0, len(heroAgility) - 1)])
    elif arg.lower() == 'интелект':
        await ctx.send(heroIntelligence[random.randint(0, len(heroIntelligence) - 1)])


@client.command(pass_context=True)
async def roll(ctx, *arg):
    # author = ctx.message.author
    if len(arg) == 0:
        await ctx.send(random.randint(0, 100))
        return
    try:
        if len(arg) == 2:
            await ctx.send(random.randint(int(arg[0]), int(arg[1])))
        elif len(arg) > 2:
            raise IndexError('more argument')
        else:
            num = arg[0].replace('-', ' ').replace('/', ' ').split()
            await ctx.send(random.randint(int(num[0]), int(num[1])))
    except Exception as _e:
        # print(author.mention, arg, _e)
        await ctx.send('Кажется вы ввели что-то не то')


# Connect

token = setting.TOKEN

client.run(token)
