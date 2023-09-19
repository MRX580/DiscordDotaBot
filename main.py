import discord
import random
import asyncio
from database.sqltie import database
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

ROLES = {
    '1️⃣': 1076475660291289129,
    '2️⃣': 1076475736598249562,
    '3️⃣': 1076475791073886260,
    '4️⃣': 1076475895725965322,
    '5️⃣': 1076476013648805950,
}

items = [
    'Abyssal Blade',
    'Aeon Disk', 'Aether Lens', 'Aghanim\'s Scepter', 'Arcane Boots', 'Armlet of Mordiggian', 'Assault Cuirass',
    'Band of Elvenskin', 'Battle Fury', 'Belt of Strength', 'Black King Bar', 'Blade Mail', 'Blade of Alacrity',
    'Blades of Attack', 'Blight Stone', 'Blink Dagger', 'Bloodstone', 'Bloodthorn', 'Boots of Speed', 'Boots of Travel',
    'Boots of Travel 2', 'Bottle', 'Bracer', 'Broadsword', 'Buckler', 'Butterfly', 'Chainmail', 'Cheese', 'Circlet',
    'Clarity',
    'Claymore', 'Cloak', 'Crimson Guard', 'Crystalys', 'Daedalus', 'Dagon 5', 'Demon Edge', 'Desolator',
    'Diffusal Blade',
    'Divine Rapier', 'Dragon Lance', 'Drum of Endurance', 'Dust of Appearance', 'Eaglesong', 'Echo Sabre',
    'Enchanted Mango',
    'Energy Booster', 'Ethereal Blade', 'Eul\'s Scepter of Divinity', 'Eye of Skadi', 'Faerie Fire', 'Force Staff',
    'Gauntlets of Strength', 'Gem of True Sight', 'Ghost Scepter', 'Glimmer Cape', 'Gloves of Haste',
    'Guardian Greaves', 'Hand of Midas', 'Headdress', 'Healing Salve', 'Heart of Tarrasque', 'Heaven\'s Halberd',
    'Helm of Iron Will', 'Helm of the Dominator', 'Hood of Defiance', 'Hurricane Pike', 'Hyperstone',
    'Infused Raindrops',
    'Iron Branch', 'Javelin', 'Kaya', 'Linken\'s Sphere', 'Lotus Orb', 'Maelstrom', 'Magic Stick', 'Magic Wand',
    'Manta Style', 'Mantle of Intelligence', 'Mask of Madness', 'Medallion of Courage', 'Mekansm', 'Meteor Hammer',
    'Mithril Hammer', 'Mjollnir', 'Monkey King Bar', 'Moon Shard', 'Morbid Mask', 'Mystic Staff', 'Necronomicon',
    'Null Talisman', 'Nullifier', 'Oblivion Staff', 'Observer Ward', 'Octarine Core', 'Ogre Club', 'Orb of Venom',
    'Orchid Malevolence', 'Perseverance', 'Phase Boots', 'Pipe of Insight', 'Platemail', 'Point Booster',
    'Power Treads', 'Quarterstaff', 'Quelling Blade', 'Radiance', 'Reaver', 'Refresher Orb', 'Ring of Aquila',
    'Ring of Basilius', 'Ring of Health', 'Ring of Protection', 'Ring of Regen', 'Robe of the Magi', 'Rod of Atos',
    'Sacred Relic', 'Sage\'s Mask', 'Sange', 'Sange and Yasha', 'Satanic', 'Scythe of Vyse', 'Sentry Ward',
    'Shadow Amulet',
    'Shadow Blade', 'Shiva\'s Guard', 'Silver Edge', 'Skull Basher', 'Slippers of Agility', 'Smoke of Deceit',
    'Solar Crest',
    'Soul Booster', 'Soul Ring', 'Spirit Vessel', 'Staff of Wizardry', 'Stout Shield', 'Talisman of Evasion',
    'Tango', 'Tome of Knowledge', 'Town Portal Scroll', 'Tranquil Boots', 'Ultimate Orb', 'Urn of Shadows', 'Vanguard',
    'Veil of Discord', 'Vitality Booster', 'Vladmir\'s Offering', 'Void Stone', 'Wind Lace', 'Wraith Band', 'Yasha'
]

itemsNotAll = ['Crystalys', 'Boots of Travel 2', 'Helm of the Overlord', 'Magic Wand', 'Null Talisman', 'Wraith Band',
               'Bracer', 'Soul Ring', 'Orb of Corrosion', 'Falcon Blade', 'Power Treads', 'Phase Boots',
               'Oblivion Staff', 'Perseverance', 'Mask of Madness', 'Hand of Midas', 'Helm of the Dominator', 'Buckler',
               'Ring of Basilius', 'Headdress', 'Urn of Shadows', 'Tranquil Boots', 'Medallion of Courage',
               'Arcane Boots', 'Drum of Endurance', 'Holy Locket', 'Veil of Discord', 'Glimmer Cape', 'Force Staff',
               'Aether Lens', 'Witch Blade', 'Eul\'s Scepter of Divinity', 'Rod of Atos', 'Dagon', 'Orchid Malevolence',
               'Solar Crest', 'Aghanim\'s Scepter', 'Refresher Orb', 'Octarine Core', 'Scythe of Vyse', 'Gleipnir',
               'Wind Waker', 'Meteor Hammer', 'Armlet of Mordiggian', 'Skull Basher', 'Shadow Blade', 'Desolator',
               'Battle Fury', 'Ethereal Blade', 'Nullifier', 'Monkey King Bar', 'Butterfly', 'Radiance', 'Daedalus',
               'Silver Edge', 'Divine Rapier', 'Bloodthorn', 'Abyssal Blade', 'Hood of Defiance', 'Vanguard',
               'Blade Mail', 'Aeon Disk', 'Soul Booster', 'Eternal Shroud', 'Crimson Guard', 'Lotus Orb',
               'Black King Bar', 'Hurricane Pike', 'Manta Style', 'Linken\'s Sphere', 'Shiva\'s Guard',
               'Heart of Tarrasque', 'Assault Cuirass', 'Bloodstone', 'Dragon Lance', 'Sange', 'Yasha', 'Kaya',
               'Echo Sabre', 'Maelstrom', 'Diffusal Blade', 'Mage Slayer', 'Heaven\'s Halberd', 'Kaya and Sange',
               'Sange and Yasha', 'Yasha and Kaya', 'Satanic', 'Eye of Skadi', 'Mjollnir', 'Overwhelming Blink',
               'Swift Blink', 'Arcane Blink']

notItems = ['Iron Branch',
            'Gauntlets of Strength', 'Slippers of Agility', 'Mantle of Intelligence', 'Circlet', 'Belt of Strength',
            'Band of Elvenskin', 'Robe of the Magi', 'Crown', 'Ogre Axe', 'Blade of Alacrity', 'Staff of Wizardry',
            'Blitz Knuckles', 'Ring of Protection', 'Quelling Blade', 'Blight Stone', 'Orb of Venom',
            'Blades of Attack',
            'Chainmail', 'Quarterstaff', 'Helm of Iron Will', 'Broadsword', 'Claymore', 'Javelin', 'Mithril Hammer',
            'Ring of Regen', 'Sage\'s Mask', 'Magic Stick', 'Fluffy Hat', 'Wind Lace', 'Cloak', 'Gloves of Haste',
            'Boots of Speed',
            'Morbid Mask', 'Voodoo Mask', 'Shadow Amulet', 'Ghost Scepter', 'Blink Dagger', 'Ring of Health',
            'Void Stone', 'Energy Booster',
            'Vitality Booster', 'Point Booster', 'Platemail', 'Talisman of Evasion', 'Hyperstone', 'Ultimate Orb',
            'Demon Edge',
            'Mystic Staff', 'Reaver', 'Eaglesong', 'Sacred Relic']

heroStrength = ('Abbadon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centaur Warrunner',
                'Chaos Knight', 'Clockwerk', 'Dawnbreaker', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earthshaker',
                'Elder Titan', 'Huskar', 'Io', 'Kunkka', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci',
                'Mars', 'Night Stalker', 'Omniknight', 'Phoenix', 'Pudge', 'Sand King', 'Slardar', 'Snapfire',
                'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord',
                'Undying', 'Wraith King')

heroStrengthImg = (
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/26/Abaddon_icon.png/revision/latest/scale-to-width-down/120?cb=20210125060638',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/fe/Alchemist_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210240',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/23/Axe_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211422',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d9/Beastmaster_icon.png/revision/latest/scale-to-width-down/120?cb=20160411205834',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/1e/Brewmaster_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210333',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/4/4d/Bristleback_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210744',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/e/ed/Centaur_Warrunner_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210603',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/fe/Chaos_Knight_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212259',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d8/Clockwerk_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210004',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d6/Dawnbreaker_icon.png/revision/latest/scale-to-width-down/120?cb=20210410124439',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/4/40/Doom_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212104',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/5/59/Dragon_Knight_icon.png/revision/latest/scale-to-width-down/120?cb=20160411205925',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/b/be/Earth_Spirit_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211247',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/a/a5/Earthshaker_icon.png/revision/latest/scale-to-width-down/120?cb=20160411205323',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/1a/Elder_Titan_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210922',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d3/Huskar_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210201',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/8/8d/Io_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210451',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c0/Kunkka_icon.png/revision/latest/scale-to-width-down/120?cb=20160411205729',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/a/a2/Legion_Commander_icon.png/revision/latest/scale-to-width-down/120?cb=20190401095109',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/2b/Lifestealer_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211952',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d6/Lycan_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212224',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/b/ba/Magnus_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212403',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/12/Marci_icon.png/revision/latest/scale-to-width-down/120?cb=20211029000514',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/9d/Mars_icon.png/revision/latest/scale-to-width-down/120?cb=20190401094550',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/15/Night_Stalker_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212027',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/e/e2/Omniknight_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210119',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/14/Phoenix_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211344',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c0/Pudge_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211506',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/79/Sand_King_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211544',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7e/Slardar_icon.png/revision/latest/scale-to-width-down/120?cb=20161213040814',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7a/Snapfire_icon.png/revision/latest/scale-to-width-down/120?cb=20191127043227',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/df/Spirit_Breaker_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212138',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/1b/Sven_icon.png/revision/latest/scale-to-width-down/120?cb=20160411205500',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d5/Tidehunter_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211651',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/9a/Timbersaw_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210643',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/5/55/Tiny_icon.png/revision/latest/scale-to-width-down/120?cb=20160411205608',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/3/3f/Treant_Protector_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210417',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/ce/Tusk_icon.png/revision/latest/scale-to-width-down/120?cb=20160411210826',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/18/Underlord_icon.png/revision/latest/scale-to-width-down/120?cb=20160828140759',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/6/61/Undying_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212333',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/1e/Wraith_King_icon.png/revision/latest/scale-to-width-down/120?cb=20160411211746')

heroAgility = ('Anti-Mage', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Broodmother', 'Clinkz', 'Drow Ranger',
               'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Lone Druid', 'Luna', 'Medusa',
               'Meppo', 'Mirana', 'Monkey King', 'Morphling', 'Naga Siren', 'Nyx Assasin', 'Pangolier',
               'Phantom Assasin',
               'Phantom Lanser', 'Razor', 'Riki', 'Shadow Fiend', 'Slark', 'Sniper', 'Spectre', 'Templar Assasin',
               'Terrorblade', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomanser', 'Viper', 'Weaver')

heroAgilityImg = (
'https://static.wikia.nocookie.net/dota2_gamepedia/images/8/8e/Anti-Mage_icon.png/revision/latest/scale-to-width-down/120?cb=20200916215957',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/0/07/Arc_Warden_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214723',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/5/56/Bloodseeker_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213712',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/a/a6/Bounty_Hunter_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213244',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/df/Broodmother_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214142',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/cb/Clinkz_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214114',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/8/80/Drow_Ranger_icon.png/revision/latest/scale-to-width-down/120?cb=20190325143546',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/91/Ember_Spirit_icon.png/revision/latest/scale-to-width-down/120?cb=20170417182614',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/73/Faceless_Void_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213936',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/4/4f/Gyrocopter_icon.png/revision/latest/scale-to-width-down/120?cb=20181101233643',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c9/Hoodwink_icon.png/revision/latest/scale-to-width-down/120?cb=20201217205959',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/0/03/Juggernaut_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212710',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/5/5d/Lone_Druid_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213427',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7d/Luna_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213209',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/cc/Medusa_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214604',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/8/85/Meepo_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214421',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/12/Mirana_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212744',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7b/Monkey_King_icon.png/revision/latest/scale-to-width-down/120?cb=20161222035035',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7b/Morphling_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212816',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/6/60/Naga_Siren_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213513',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/fa/Nyx_Assassin_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214454',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/4/4e/Pangolier_icon.png/revision/latest/scale-to-width-down/120?cb=20180831204401',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/8/8e/Phantom_Assassin_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214013',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/8/81/Phantom_Lancer_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212849',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/6/66/Razor_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213830',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/7d/Riki_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212958',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/3/36/Shadow_Fiend_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213752',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/a/aa/Slark_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214526',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/5/51/Sniper_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213053',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/ff/Spectre_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214336',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/9c/Templar_Assassin_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213131',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/5/52/Terrorblade_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214652',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/f0/Troll_Warlord_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213539',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/4/40/Ursa_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213321',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/20/Vengeful_Spirit_icon.png/revision/latest/scale-to-width-down/120?cb=20160411212927',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/25/Venomancer_icon.png/revision/latest/scale-to-width-down/120?cb=20160411213902',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/5/5f/Viper_icon.png/revision/latest/scale-to-width-down/120?cb=20161213040756',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/0/09/Weaver_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214233')

heroIntelligence = ('Ancient Apparition', 'Bane', 'Batrider', 'Chen', 'Cristal Maiden', 'Dark Seer', 'Dark Willow',
                    'Dazzle', 'Death Prophet', 'Disraptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro',
                    'Keep Of The Light', 'Leshrak', 'Lich', 'Lina', 'Lion', 'Nature\'s Prophet', 'Necrophos',
                    'Ogre Magi', 'Oracle', 'Outworld Destroyer', 'Puck', 'Pugna', 'Queen Of Pain', 'Rubick',
                    'Shadow Demon', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Storm Spirit',
                    'Ebanaya Huinya(Techies)', 'Tinker', 'Visage', 'Void Spirit', 'Warlock', 'Windranger',
                    'Winter Wyvern', 'Withc Doctor', 'Zeus')

heroIntelligenceImg = (
'https://static.wikia.nocookie.net/dota2_gamepedia/images/6/67/Ancient_Apparition_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220816',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c3/Bane_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215925',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/f2/Batrider_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220708',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/6/61/Chen_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215432',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/27/Crystal_Maiden_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214805',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c5/Dark_Seer_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220632',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/3/3c/Dark_Willow_icon.png/revision/latest/scale-to-width-down/120?cb=20180831204518',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/e/e6/Dazzle_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220519',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d7/Death_Prophet_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220408',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/97/Disruptor_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215651',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/4/41/Enchantress_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215320',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/f7/Enigma_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220156',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d7/Grimstroke_icon.png/revision/latest/scale-to-width-down/120?cb=20180831203927',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/0/00/Invoker_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220849',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/2f/Jakiro_icon.png/revision/latest/scale-to-width-down/120?cb=20170507134250',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/b/b9/Keeper_of_the_Light_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215721',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/2/26/Leshrac_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220559',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/b/bb/Lich_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215954',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/3/35/Lina_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215059',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/b/b8/Lion_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220032',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c4/Nature%27s_Prophet_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215241',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/a/a6/Necrophos_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220233',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/e/e0/Ogre_Magi_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215538',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/7/72/Oracle_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215824',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/10/Outworld_Destroyer_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220923',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/13/Puck_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214839',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/c/cd/Pugna_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220442',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/a/a1/Queen_of_Pain_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220334',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/8/8a/Rubick_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215614',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/f3/Shadow_Demon_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220956',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/96/Shadow_Shaman_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215130',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/9f/Silencer_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215503',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/b/bf/Skywrath_Mage_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215753',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/1/13/Storm_Spirit_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214914',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/f/fa/Techies_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215855',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/d/d1/Tinker_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215201',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/9e/Visage_icon.png/revision/latest/scale-to-width-down/120?cb=20160411221032',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/9/99/Void_Spirit_icon.png/revision/latest/scale-to-width-down/120?cb=20210413204208',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/3/3f/Warlock_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220306',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/6/60/Windranger_icon.png/revision/latest/scale-to-width-down/120?cb=20160411214951',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/4/4a/Winter_Wyvern_icon.png/revision/latest/scale-to-width-down/120?cb=20160411221057',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/3/33/Witch_Doctor_icon.png/revision/latest/scale-to-width-down/120?cb=20160411220105',
'https://static.wikia.nocookie.net/dota2_gamepedia/images/3/3f/Zeus_icon.png/revision/latest/scale-to-width-down/120?cb=20160411215025')

quizItem = {
    'Crystalys': 'Broadsword, Blades of Attack, Рецепт',
    'Boots of Travel 2': 'Boots of Travel, Рецепт',
    'Boots of Travel': 'Boots of Speed, Рецепт',
    'Helm of the Overlord': 'Helm of the Dominator, Vladimi\'s Offering, Рецепт',
    'Magic Wand': 'Iron Branch, Iron Branch, Magic Stick, Рецепт',
    'Null Talisman': 'Mantle of Intelligence, Circlet, Рецепт',
    'Wraith Band': 'Slippers of Agility, Circlet, Рецепт',
    'Bracer': 'Gauntlets of Strength, Circlet, Рецепт',
    'Soul Ring': 'Gauntlets of Strength, Gauntlets of Strength, Ring of Protection, Рецепт',
    'Orb of Corrosion': 'Blight Stone, Orb of Venom, Fluffy Hat, Рецепт',
    'Falcon Blade': 'Blades of Attack, Sage\'s Mask, Fluffy Hat, Рецепт',
    'Power Treads': 'Belt of Strength, Gloves of Haste, Boots of Speed',
    'Phase Boots': 'Blades of Attack, Chainmail, Boots of Speed',
    'Oblivion Staff': 'Quarterstaff, Sage\'s Mask, Robe of the Magi',
    'Perseverance': 'Ring of Health, Void Stone',
    'Mask of Madness': 'Quarterstaff, Morbid Mask',
    'Hand of Midas': 'Gloves of Haste, Рецепт',
    'Helm of the Dominator': 'Crown, Helm of Iron Will, Рецепт',
    'Buckler': 'Ring of Protection, Рецепт',
    'Ring of Basilius': 'Sage\'s Mask, Рецепт',
    'Headdress': 'Ring of Regen, Рецепт',
    'Urn of Shadows': 'Circlet, Ring of Protection, Sage\'s Mask, Рецепт',
    'Tranquil Boots': 'Ring of Regen, Wind Lace, Boots of Speed',
    'Medallion of Courage': 'Blight Stone, Chainmail, Sage\'s Mask',
    'Arcane Boots': 'Boots of Speed, Energy Booster',
    'Drum of Endurance': 'Belt of Strength, Robe of the Magi, Wind Lace, Рецепт',
    'Holy Locket': 'Magic Wand, Fluffy Hat, Energy Booster, Рецепт',
    'Veil of Discord': 'Crown, Рецепт',
    'Glimmer Cape': 'Cloak, Shadow Amulet, Рецепт',
    'Force Staff': 'Staff of Wizardry, Fluffy Hat, Рецепт',
    'Aether Lens': 'Void Stone, Energy Booster, Рецепт',
    'Witch Blade': 'Robe of the Magi, Blitz Knuckles, Chainmail, Рецепт',
    'Eul\'s Scepter of Divinity': 'Staff of Wizardry, Wind Lace, Void Stone, Рецепт',
    'Rod of Atos': 'Crown, Crown, Staff of Wizardry, Рецепт',
    'Dagon': 'Crown, Staff of Wizardry, Рецепт',
    'Orchid Malevolence': 'Oblivion Staff, Oblivion Staff, Рецепт',
    'Solar Crest': 'Crown, Wind Lace, Medallion of Courage, Рецепт',
    'Aghanim\'s Scepter': 'Ogre Axe, Blade of Alacrity, Staff of Wizardry, Point Booster',
    'Refresher Orb': 'Perseverance, Perseverance, ',
    'Octarine Core': 'Aether Lens, Soul Booster',
    'Scythe of Vyse': 'Void Stone, Ultimate Orb, Mystic Staff',
    'Gleipnir': 'Maelstorm, Rod Of Atos, Рецепт',
    'Wind Waker': 'Mystic Staff, Eul\'s Scepter of Divinity, Рецепт',
    'Meteor Hammer': 'Crown, Perseverance, Рецепт',
    'Armlet of Mordiggian': 'Blades of Attack, Helm of Iron Will, Gloves of Haste, Рецепт',
    'Skull Basher': 'Belt of Strength, Mithril Hammer, Рецепт',
    'Shadow Blade': 'Blitz Knuckles, Broadsword, Shadow Amulet',
    'Desolator': 'Blight Stone, Mithril Hammer, Mithril Hammer',
    'Battle Fury': 'Quelling Blade, Broadsword, Claymore, Perseverance',
    'Ethereal Blade': 'Ghost Scepter, Eaglesong',
    'Nullifier': 'Helm of Iron Will, Sacred Relic',
    'Monkey King Bar': 'Blitz Knuckles, Javelin, Demon Edge',
    'Butterfly': 'Quarterstaff, Talisman of Evasion, Eaglesong',
    'Radiance': 'Sacred Relic, Рецепт',
    'Daedalus': 'Demon Edge, Crystalys, Рецепт',
    'Silver Edge': 'Shadow Blade, Crystalys, Рецепт',
    'Divine Rapier': 'Demon Edge, Sacred Relic',
    'Bloodthorn': 'Hyperstone, Orchid Malevolence, Рецепт',
    'Abyssal Blade': 'Skull Basher, Vanguard, Рецепт',
    'Hood of Defiance': 'Ring of Regen, Cloak, Ring of Health',
    'Vanguard': 'Ring of Health, Vitality Booster',
    'Blade Mail': 'Chainmail, Broadsword, Рецепт',
    'Aeon Disk': 'Energy Booster, Vitality Booster, Рецепт',
    'Soul Booster': 'Energy Booster, Vitality Booster, Point Booster',
    'Eternal Shroud': 'Voodoo Mask, Hood of Defiance, Рецепт',
    'Crimson Guard': 'Helm of Iron Will, Vanguard, Рецепт',
    'Lotus Orb': 'Energy Booster, Perseverance, Platemail',
    'Black King Bar': 'Ogre Axe, Mithril Hammer, Рецепт',
    'Hurricane Pike': 'Dragon Lance, Force Staff, Рецепт',
    'Manta Style': 'Ultimate Orb, Yasha, Рецепт',
    'Linken\'s Sphere': 'Perseverance, Ultimate Orb, Рецепт',
    'Shiva\'s Guard': 'Platemail, Mystic Staff, Рецепт',
    'Heart of Tarrasque': 'Vitality Booster, Reaver, Рецепт',
    'Assault Cuirass': 'Platemail, Hyperstone, Рецепт',
    'Bloodstone': 'Voodoo Mask, Soul Booster, Kaya',
    'Dragon Lance': 'Band of Elvenskin, Ogre Axe, Band of Elvenskin',
    'Sange': 'Belt of Strength, Ogre Axe, Рецепт',
    'Yasha': 'Band of Elvenskin, Blade of Alacrity, Рецепт',
    'Kaya': 'Robe of the Magi, Staff of Wizardry, Рецепт',
    'Echo Sabre': 'Ogre Axe, Oblivion Staff',
    'Maelstrom': 'Javelin, Mithril Hammer',
    'Diffusal Blade': 'Robe of the Magi, Blade of Alacrity, Blade of Alacrity, Рецепт',
    'Mage Slayer': 'Cloak, Oblivion Staff, Рецепт',
    'Heaven\'s Halberd': 'Talisman of Evasion, Sange, Рецепт',
    'Kaya and Sange': 'Sange, Kaya',
    'Sange and Yasha': 'Sange, Yasha',
    'Yasha and Kaya': 'Yasha, Kaya',
    'Satanic': 'Claymore, Morbid Mask, Reaver',
    'Eye of Skadi': 'Point Booster, Ultimate Orb, Ultimate Orb',
    'Mjollnir': 'Hyperstone, Maelstorm, Рецепт',
    'Overwhelming Blink': 'Blink Dagger, Reaver, Рецепт',
    'Swift Blink': 'Blink Dagger, Eaglesong, Рецепт',
    'Arcane Blink': 'Blink Dagger, Mystic Staff, Рецепт',
    'Vladimi\'s Offering': 'Blades of Attack, Morbid Mask, Рецепт',
    'Mekansm': 'Chainmail, Headdress, Рецепт',
    'Spirit Vessel': 'Vitality Booster, Urn of Shadows, Рецепт',
    'Moon Shard': 'Hyperstone, Hyperstone',
}

allHero = heroStrength + heroAgility + heroIntelligence
allHeroImg = heroStrengthImg + heroAgilityImg + heroIntelligenceImg
client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

async def quizz():
    time = 3600
    await asyncio.sleep(time)
    random_item = itemsNotAll[random.randint(0, len(itemsNotAll) - 1)]
    mass = []
    right_quiz = random.randint(1, 4)
    for i in range(1, 5):
        if i == right_quiz:
            mass.append(quizItem[random_item])
        else:
            mass.append(quizItem[itemsNotAll[random.randint(0, len(itemsNotAll) - 1)]])
    database().add_quiz(right_quiz)
    emb = discord.Embed(title=f'Из чего крафтится {random_item}', color=discord.Colour.blue())
    emb.add_field(name='1', value=mass[0], inline=False)
    emb.add_field(name='2', value=mass[1], inline=False)
    emb.add_field(name='3', value=mass[2], inline=False)
    emb.add_field(name='4', value=mass[3], inline=False)
    await client.get_channel(1082783333521571861).send(embed=emb)
    await quizz()
    # await client.get_channel(939656305168248842).send('hello')


@client.command()
async def quiz(ctx, answer):
    if not database().isQuiz():
        if not database(ctx.author, ctx.author.id).isQuizUser():
            if answer == database().get_correct_quiz():
                await ctx.send('Right')
                database().close_quiz()
            else:
                database(ctx.author, ctx.author.id).close_quiz_user()
                await ctx.send('False')
        else:
            await ctx.send('Вы уже дали ответ')
    else:
        await ctx.send('Уже был дан правильный ответ викторина будет в течении часа')


@client.event
async def on_ready():
    print('Bot connected')
    for guild in client.guilds:
        for member in guild.members:
            database(member, member.id).add_user()
    client.loop.create_task(quizz())


@client.event
async def on_member_join(member):
    database(member, member.id).add_user()


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1082778934879453305:
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


@client.command()
async def stat(ctx):
    member = database(ctx.author, ctx.author.id).database_members()
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(title='Статистика', color=discord.Colour.blue())
    emb.add_field(name='Name', value=f'{ctx.message.author}', inline=False)
    emb.add_field(name='Ранг', value=str(member[5]), inline=True)
    emb.add_field(name='Монеты', value=str(member[3]), inline=True)
    emb.add_field(name='Очки', value=str(member[4]), inline=True)
    await ctx.send(embed=emb)


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
    async def clear(ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)
except discord.ext.commands.errors.MissingPermissions:
    pass


@client.command(pass_context=True)
async def rollhero(ctx, arg=None):
    if arg is None:
        rand = random.randint(0, len(allHero) - 1)
        emb = discord.Embed(title=str(allHero[rand]), color=discord.Colour.blue())
        emb.set_image(url=str(allHeroImg[rand]))
        await ctx.send(embed=emb)
    elif arg.lower() == 'сила':
        rand = random.randint(0, len(heroStrength) - 1)
        emb = discord.Embed(title=str(heroStrength[rand]), color=discord.Colour.blue())
        emb.set_image(url=str(heroStrengthImg[rand]))
        await ctx.send(embed=emb)
    elif arg.lower() == 'ловкость':
        rand = random.randint(0, len(heroAgility) - 1)
        emb = discord.Embed(title=str(heroAgility[rand]), color=discord.Colour.blue())
        emb.set_image(url=str(heroAgilityImg[rand]))
        await ctx.send(embed=emb)

    elif arg.lower() == 'интелект':
        rand = random.randint(0, len(heroIntelligence) - 1)
        emb = discord.Embed(title=str(heroIntelligence[rand]), color=discord.Colour.blue())
        emb.set_image(url=str(heroIntelligenceImg[rand]))
        await ctx.send(embed=emb)


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

token = os.getenv('TOKEN')

client.run(token)
