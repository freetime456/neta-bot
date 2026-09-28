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
        print(f"コマンド同期: {len(synced)}個")
    except Exception as e:
        print(f"同期エラー: {e}")


# =========================
# 共通：％判定
# =========================

def percent_embed(user, title, emoji):
    value = random.randint(0, 100)

    if value <= 10:
        comment = "ほぼ無い。"
    elif value <= 30:
        comment = "まだ普通。"
    elif value <= 50:
        comment = "微妙なところ。"
    elif value <= 70:
        comment = "そこそこ高い。"
    elif value <= 90:
        comment = "かなり高いｗｗｗ"
    else:
        comment = "これはヤバいｗｗｗ"

    embed = discord.Embed(
        title=f"{emoji} {title}",
        description=f"対象：**{user.display_name}**"
    )

    embed.add_field(
        name="判定",
        value=f"# {value}%",
        inline=False
    )

    embed.add_field(
        name="コメント",
        value=comment,
        inline=False
    )

    return embed


# =========================
# 黒歴史
# =========================

@bot.tree.command(name="黒歴史", description="ユーザーの黒歴史を予想します")
@app_commands.describe(user="黒歴史を予想するユーザー")
async def kurorekishi(
    interaction: discord.Interaction,
    user: discord.Member
):

    predictions = [
        "鏡の前で謎のポーズを決めていた",
        "誰もいないところでカッコいいセリフを練習していた",
        "昔のSNSのプロフィールがめちゃくちゃ痛かった",
        "ゲームで負けて本気でキレていた",
        "自分だけの必殺技を考えていた",
        "黒歴史ノートを作っていた",
        "意味不明なあだ名を自分で名乗っていた",
        "昔の写真を見返して自分で恥ずかしくなった",
        "謎のキャラクターになりきっていた",
        "友達に送るつもりのないメッセージを間違えて送った",
        "学校で謎のポーズをしていた",
        "ゲームの名前をめちゃくちゃカッコつけていた",
        "昔の自分を思い出して『なんでやったんだ』となった",
    ]

    embed = discord.Embed(
        title="📕 黒歴史予想",
        description=f"**{user.display_name}** の黒歴史を予想します……"
    )

    embed.add_field(
        name="🔮 予想",
        value=random.choice(predictions),
        inline=False
    )

    embed.set_footer(text="※完全ランダムのネタ予想です")

    await interaction.response.send_message(embed=embed)


# =========================
# 人生終了
# =========================

@bot.tree.command(name="人生終了", description="人生終了の原因を予想します")
@app_commands.describe(user="対象ユーザー")
async def jinsei(
    interaction: discord.Interaction,
    user: discord.Member
):

    reasons = [
        "寝坊",
        "スマホの見すぎ",
        "宿題を忘れる",
        "財布を忘れる",
        "ゲームのやりすぎ",
        "寝落ち",
        "充電切れ",
        "電車・バスに乗り遅れる",
        "お腹が空きすぎる",
        "謎の行動",
        "自分で自分を追い込む",
        "特に理由なし",
    ]

    embed = discord.Embed(
        title="💀 人生終了予想",
        description=f"**{user.display_name}** の人生終了原因を予想……"
    )

    embed.add_field(
        name="💀 原因",
        value=random.choice(reasons),
        inline=False
    )

    embed.set_footer(text="※もちろんネタです")

    await interaction.response.send_message(embed=embed)


# =========================
# 好感度
# =========================

@bot.tree.command(name="好感度", description="好感度を判定します")
@app_commands.describe(user="対象ユーザー")
async def koukando(
    interaction: discord.Interaction,
    user: discord.Member
):

    value = random.randint(0, 100)

    comments = [
        "誰ですか？",
        "知り合いくらい。",
        "普通です。",
        "まあまあ好き。",
        "結構好かれています。",
        "かなり好かれています。",
        "めちゃくちゃ好かれています。",
    ]

    embed = discord.Embed(
        title="❤️ 好感度",
        description=f"**{user.display_name}** の好感度"
    )

    embed.add_field(
        name="❤️ 好感度",
        value=f"# {value}%",
        inline=False
    )

    embed.add_field(
        name="評価",
        value=random.choice(comments),
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# ○○度シリーズ
# =========================

@bot.tree.command(name="イケメン度", description="イケメン度を判定します")
@app_commands.describe(user="対象ユーザー")
async def ikemen(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "イケメン度", "😎")
    )


@bot.tree.command(name="バカ度", description="バカ度を判定します")
@app_commands.describe(user="対象ユーザー")
async def baka(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "バカ度", "🧠")
    )


@bot.tree.command(name="運の良さ", description="運の良さを判定します")
@app_commands.describe(user="対象ユーザー")
async def luck(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "運の良さ", "🍀")
    )


@bot.tree.command(name="厨二病度", description="厨二病度を判定します")
@app_commands.describe(user="対象ユーザー")
async def chuunibyou(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "厨二病度", "⚔️")
    )


@bot.tree.command(name="変人度", description="変人度を判定します")
@app_commands.describe(user="対象ユーザー")
async def henjin(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "変人度", "🗿")
    )


@bot.tree.command(name="人間度", description="人間度を判定します")
@app_commands.describe(user="対象ユーザー")
async def ningen(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "人間度", "👤")
    )


@bot.tree.command(name="犯罪者度", description="犯罪者っぽさをネタ判定します")
@app_commands.describe(user="対象ユーザー")
async def hanzai(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "犯罪者度", "🚓")
    )


@bot.tree.command(name="犬化", description="犬っぽさを判定します")
@app_commands.describe(user="対象ユーザー")
async def inu(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "犬化度", "🐕")
    )


@bot.tree.command(name="陽キャ度", description="陽キャ度を判定します")
@app_commands.describe(user="対象ユーザー")
async def youkyaku(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "陽キャ度", "✨")
    )


@bot.tree.command(name="陰キャ度", description="陰キャ度を判定します")
@app_commands.describe(user="対象ユーザー")
async def inkyaku(interaction, user: discord.Member):
    await interaction.response.send_message(
        embed=percent_embed(user, "陰キャ度", "🌑")
    )


# =========================
# 存在価値
# =========================

@bot.tree.command(name="存在価値", description="存在価値をネタ判定します")
@app_commands.describe(user="対象ユーザー")
async def sonzai(interaction, user: discord.Member):

    values = [
        "Discordにいるだけで意味がある",
        "とりあえず存在している",
        "鯖の重要人物……かもしれない",
        "NPC判定",
        "今日だけ存在価値が高い",
        "謎の存在",
    ]

    embed = discord.Embed(
        title="🗿 存在価値判定",
        description=f"**{user.display_name}**"
    )

    embed.add_field(
        name="判定",
        value=random.choice(values),
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 運勢
# =========================

@bot.tree.command(name="運勢", description="今日の運勢を予想します")
async def unsei(interaction):

    results = [
        "今日は何をしても普通。",
        "今日は謎の幸運が起きます。",
        "スマホを落とさないように。",
        "誰かから連絡が来るかも。",
        "今日は早く寝ましょう。",
        "何かを忘れる可能性があります。",
        "特に何も起きません。",
    ]

    embed = discord.Embed(
        title="🔮 今日の運勢",
        description=random.choice(results)
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 逮捕
# =========================

@bot.tree.command(name="逮捕", description="罪状を予想して逮捕します")
@app_commands.describe(user="逮捕するユーザー")
async def taiho(interaction, user: discord.Member):

    crimes = [
        "存在した罪",
        "寝坊した罪",
        "Discordを開きすぎた罪",
        "しょうもない発言をした罪",
        "意味不明な行動をした罪",
        "ゲームをやりすぎた罪",
        "急に黙った罪",
    ]

    embed = discord.Embed(
        title="🚓 逮捕",
        description=f"**{user.display_name}** を逮捕しました。"
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

@bot.tree.command(name="裁判", description="裁判結果を予想します")
@app_commands.describe(user="裁判するユーザー")
async def saiban(interaction, user: discord.Member):

    crimes = [
        "寝坊罪",
        "Discord中毒罪",
        "謎行動罪",
        "ゲームやりすぎ罪",
        "存在罪",
        "しょうもない発言罪",
    ]

    result = random.choice(["有罪 ⚖️", "無罪 ⚖️"])

    embed = discord.Embed(
        title="⚖️ Discord裁判所",
        description=f"被告：**{user.display_name}**"
    )

    embed.add_field(
        name="罪状予想",
        value=random.choice(crimes),
        inline=False
    )

    embed.add_field(
        name="判決",
        value=f"# {result}",
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 予言
# =========================

@bot.tree.command(name="予言", description="未来を予想します")
@app_commands.describe(user="予言するユーザー")
async def yogen(interaction, user: discord.Member):

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
        description=f"**{user.display_name}** の未来を予想……"
    )

    embed.add_field(
        name="予言",
        value=random.choice(predictions),
        inline=False
    )

    await interaction.response.send_message(embed=embed)


# =========================
# 死亡
# =========================

@bot.tree.command(name="死亡", description="ネタとして死因を予想します")
@app_commands.describe(user="対象ユーザー")
async def shibou(interaction, user: discord.Member):

    causes = [
        "眠気に負けました。",
        "スマホを見すぎました。",
        "お腹が空きすぎました。",
        "Discordをやりすぎました。",
        "寝落ちしました。",
        "充電切れで力尽きました。",
        "特に理由はありません。",
    ]

    embed = discord.Embed(
        title="💀 死亡予想",
        description=f"**{user.display_name}** の死因を予想……"
    )

    embed.add_field(
        name="死因",
        value=random.choice(causes),
        inline=False
    )

    embed.set_footer(text="※完全なネタです")

    await interaction.response.send_message(embed=embed)


# =========================
# Bot起動
# =========================

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN が設定されていません。")

bot.run(TOKEN)
