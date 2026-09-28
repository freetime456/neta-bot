import os
import random
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =========================
# 起動
# =========================

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"ログイン成功: {bot.user}")
        print(f"スラッシュコマンド同期: {len(synced)}個")
    except Exception as e:
        print(f"同期エラー: {e}")


# =========================
# 共通
# =========================

def target_name(user):
    return user.display_name


def percent_result(name, title, emoji):
    value = random.randint(0, 100)

    if value <= 10:
        comment = "逆にすごい。"
    elif value <= 30:
        comment = "まだ大丈夫……たぶん。"
    elif value <= 50:
        comment = "微妙なライン。"
    elif value <= 70:
        comment = "なかなかですね。"
    elif value <= 90:
        comment = "かなり高いです。"
    else:
        comment = "これはヤバいｗｗｗ"

    embed = discord.Embed(
        title=f"{emoji} {title}",
        description=f"**{name}** の結果",
    )

    embed.add_field(
        name="判定",
        value=f"## {value}%",
        inline=False
    )

    embed.add_field(
        name="コメント",
        value=comment,
        inline=False
    )

    return embed


# =========================
# 人生終了
# =========================

@bot.tree.command(name="人生終了", description="人生終了度を判定します")
@app_commands.describe(user="判定するユーザー")
async def jinsei(interaction: discord.Interaction, user: discord.Member):

    value = random.randint(0, 100)

    comments = [
        "まだ人生は続いています。",
        "ちょっと危ない。",
        "人生の残りHPが少ない。",
        "かなり終わりに近づいています。",
        "人生終了のお知らせ。",
        "伝説になりました。",
    ]

    embed = discord.Embed(
        title="💀 人生終了判定",
        description=f"**{target_name(user)}** の人生終了度",
    )

    embed.add_field(
        name="終了度",
        value=f"## {value}%",
        inline=False
    )

    embed.add_field(
        name="判定",
        value=random.choice(comments),
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 黒歴史
# =========================

@bot.tree.command(name="黒歴史", description="黒歴史度を判定します")
@app_commands.describe(user="判定するユーザー")
async def kurorekishi(interaction: discord.Interaction, user: discord.Member):

    embed = percent_result(
        target_name(user),
        "黒歴史度",
        "📕"
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 好感度
# =========================

@bot.tree.command(name="好感度", description="好感度を判定します")
@app_commands.describe(user="判定するユーザー")
async def koukando(interaction: discord.Interaction, user: discord.Member):

    value = random.randint(0, 100)

    if value <= 10:
        comment = "誰ですか？"
    elif value <= 30:
        comment = "知り合いくらい。"
    elif value <= 50:
        comment = "普通です。"
    elif value <= 70:
        comment = "結構好きかも。"
    elif value <= 90:
        comment = "かなり好かれています。"
    else:
        comment = "めちゃくちゃ好かれています。"

    embed = discord.Embed(
        title="❤️ 好感度判定",
        description=f"**{target_name(user)}** の好感度",
    )

    embed.add_field(
        name="好感度",
        value=f"## {value}%",
        inline=False
    )

    embed.add_field(
        name="評価",
        value=comment,
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# その他の判定
# =========================

@bot.tree.command(name="イケメン度", description="イケメン度を判定します")
@app_commands.describe(user="判定するユーザー")
async def ikemen(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "イケメン度", "😎")
    )


@bot.tree.command(name="バカ度", description="バカ度を判定します")
@app_commands.describe(user="判定するユーザー")
async def baka(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "バカ度", "🧠")
    )


@bot.tree.command(name="運の良さ", description="運の良さを判定します")
@app_commands.describe(user="判定するユーザー")
async def luck(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "運の良さ", "🍀")
    )


@bot.tree.command(name="厨二病度", description="厨二病度を判定します")
@app_commands.describe(user="判定するユーザー")
async def chuunibyou(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "厨二病度", "⚔️")
    )


@bot.tree.command(name="変人度", description="変人度を判定します")
@app_commands.describe(user="判定するユーザー")
async def henjin(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "変人度", "🗿")
    )


@bot.tree.command(name="人間度", description="人間度を判定します")
@app_commands.describe(user="判定するユーザー")
async def ningen(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "人間度", "👤")
    )


@bot.tree.command(name="犯罪者度", description="ネタとして犯罪者度を判定します")
@app_commands.describe(user="判定するユーザー")
async def criminal(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "犯罪者度", "🚓")
    )


@bot.tree.command(name="犬化", description="犬度を判定します")
@app_commands.describe(user="判定するユーザー")
async def inu(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "犬化度", "🐕")
    )


@bot.tree.command(name="存在価値", description="存在価値を謎判定します")
@app_commands.describe(user="判定するユーザー")
async def sonzai(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "存在価値", "🗿")
    )


@bot.tree.command(name="陽キャ度", description="陽キャ度を判定します")
@app_commands.describe(user="判定するユーザー")
async def youkyado(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "陽キャ度", "✨")
    )


@bot.tree.command(name="陰キャ度", description="陰キャ度を判定します")
@app_commands.describe(user="判定するユーザー")
async def inkyado(interaction: discord.Interaction, user: discord.Member):

    await interaction.response.send_message(
        embed=percent_result(target_name(user), "陰キャ度", "🌑")
    )


# =========================
# 運勢
# =========================

@bot.tree.command(name="運勢", description="今日の謎の運勢を占います")
async def unsei(interaction: discord.Interaction):

    results = [
        "今日は何をしてもだいたい普通です。",
        "コンビニに行くと何か起きます。",
        "今日は運がいい……気がします。",
        "財布を確認しましょう。",
        "誰かからメッセージが来るかもしれません。",
        "今日は早く寝ましょう。",
        "何も考えずに生きてください。",
    ]

    embed = discord.Embed(
        title="🔮 今日の運勢",
        description=random.choice(results)
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 逮捕
# =========================

@bot.tree.command(name="逮捕", description="ユーザーを適当な罪で逮捕します")
@app_commands.describe(user="逮捕するユーザー")
async def taiho(interaction: discord.Interaction, user: discord.Member):

    crimes = [
        "存在した罪",
        "寝坊した罪",
        "Discordを開きすぎた罪",
        "しょうもない発言をした罪",
        "急に黙った罪",
        "意味不明な行動をした罪",
        "飯を食べすぎた罪",
    ]

    embed = discord.Embed(
        title="🚓 逮捕",
        description=f"**{target_name(user)}** を逮捕しました。",
    )

    embed.add_field(
        name="罪状",
        value=random.choice(crimes),
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 裁判
# =========================

@bot.tree.command(name="裁判", description="有罪か無罪か判定します")
@app_commands.describe(user="裁判するユーザー")
async def saiban(interaction: discord.Interaction, user: discord.Member):

    result = random.choice(["⚖️ 有罪", "⚖️ 無罪"])

    embed = discord.Embed(
        title="⚖️ Discord裁判所",
        description=f"被告：**{target_name(user)}**\n\n# {result}",
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 予言
# =========================

@bot.tree.command(name="予言", description="意味不明な未来を予言します")
@app_commands.describe(user="予言するユーザー")
async def yogen(interaction: discord.Interaction, user: discord.Member):

    predictions = [
        "明日、何かを忘れます。",
        "近いうちにお腹が空きます。",
        "誰かと目が合います。",
        "スマホを落としそうになります。",
        "突然眠くなります。",
        "冷蔵庫を開けます。",
        "Discordを開きます。",
        "特に何も起きません。",
    ]

    embed = discord.Embed(
        title="🔮 未来予言",
        description=f"**{target_name(user)}** の未来\n\n{random.choice(predictions)}"
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 死亡
# =========================

@bot.tree.command(name="死亡", description="ユーザーの死亡判定をします")
@app_commands.describe(user="対象ユーザー")
async def shibou(interaction: discord.Interaction, user: discord.Member):

    reasons = [
        "眠気に負けました。",
        "スマホを見すぎました。",
        "腹が減りました。",
        "人生に疲れました。",
        "階段を見ただけで力尽きました。",
        "Discordをやりすぎました。",
        "特に理由はありません。",
    ]

    embed = discord.Embed(
        title="💀 死亡判定",
        description=f"**{target_name(user)}** は死亡しました。",
    )

    embed.add_field(
        name="死因",
        value=random.choice(reasons),
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 起動
# =========================

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN が設定されていません。")

bot.run(TOKEN)
