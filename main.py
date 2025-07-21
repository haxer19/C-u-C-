import os,json,random,asyncio,logging
from discord.ext import commands
from updater import _check_update_,_check_v_

_check_update_()

with open("config.json", "r") as config_file:
    config = json.load(config_file)

TOKEN = config["TOKEN"]
PREFIX = config["PREFIX"]
TienThanh=commands.Bot(command_prefix=PREFIX, self_bot=True)
TienThanh.remove_command("help")

_botID_=1293109493948878929
banca=1393234820271968467 
_idkenh_=None
running=True
_tinnhan_=None
logging.getLogger("discord.gateway").setLevel(logging.ERROR)
logging.getLogger("discord.state").setLevel(logging.ERROR)
logging.getLogger("discord").setLevel(logging.ERROR)

@TienThanh.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    global _idkenh_
    local=_check_v_()
    print(f"""
    \n
          -> Câu Cá PNV - {local} (Test)
          - Author: Tien Thanh
          - Login User: @{TienThanh.user}
          - Test gửi fb qua server C4F
    \n""")
    _idkenh_=int(input("Nhập ID kênh:\n>> "))
    asyncio.create_task(_td_câucá_())

def _daytuido_(embed):
    try:
        text = ""
        if embed.author and embed.author.name:
            text += embed.author.name.lower()
        if embed.title:
            text += embed.title.lower()
        if embed.description:
            text += embed.description.lower()
        
        return any(keyword in text for keyword in [
            "túi cá của bạn đã đầy",
            "túi của bạn đã đầy",
            "hết chỗ chứa",
            "sức chứa hiện tại",
            "không thể vớt thêm sò"
        ])
    except:
        return False

async def _tdBáncá_():
    try:
        channel = await TienThanh.fetch_channel(banca)
        sent = await channel.send("fs banca")

        def check_banca_reply(msg):
            try:
                return (
                    msg.author.id == _botID_ and msg.reference and msg.reference.message_id == sent.id and msg.embeds and msg.embeds[0].author and "cửa hàng bán cá" in msg.embeds[0].author.name.lower())
            except:
                return False

        reply = await TienThanh.wait_for("message", check=check_banca_reply)
        if reply.components:
            try:
                Fbutton = reply.components[0].children[0]
                await asyncio.sleep(1.5)
                await Fbutton.click()
            except:
                pass
    except:
        pass

async def _td_câucá_():
    global running, _tinnhan_
    try:
        guild=await TienThanh.fetch_guild(755793441287438469)
        channel=await TienThanh.fetch_channel(_idkenh_)
        print(f"[ Auto Farm ] > {guild.name} | Kênh: {channel.name}")
    except Exception as e:
        running = False
        return

    _kiểmtra_=0

    while running:
        try:
            _kiểmtra_+=1
            if _kiểmtra_%20==0:
                kt_td=await channel.send("fs tuido")
            
            sent_msg = await channel.send("fs cauca")
        except:
            await asyncio.sleep(5)
            continue
        
        def kt_rep1(msg):
            try:
                return (msg.author.id == _botID_ and msg.reference and msg.reference.message_id == sent_msg.id and msg.embeds and msg.embeds[0].author and "Đang thả mồi câu" in msg.embeds[0].author.name)
            except:
                return False

        try:
            reply_msg = await TienThanh.wait_for("message", check=kt_rep1)
            _tinnhan_ = reply_msg
        except:
            continue

        def _lắng_nghe_(before,after):
            try:
                return ( after.id == _tinnhan_.id and after.embeds and after.embeds[0].author and "Cá đã cắn câu" in after.embeds[0].author.name)
            except:
                return False

        try:
            before,after = await TienThanh.wait_for("message_edit", check=_lắng_nghe_)
        except:
            continue

        embed = after.embeds[0]

        if embed.title and "Không đủ mồi" in embed.title:
            running = False
            break

        if _daytuido_(embed):
            await _tdBáncá_()
            await asyncio.sleep(3)
            continue

        try:
            if after.components:
                try:
                    _chọn14_ = after.components[0].children
                    _số_nút_=len(_chọn14_)
                    if _số_nút_==1:
                        __tỉ_lệ__=[100]
                    elif _số_nút_==2:
                        __tỉ_lệ__=[69,84]  
                    elif _số_nút_==3:
                        __tỉ_lệ__=[45,79,38]  
                    elif _số_nút_==4:
                        __tỉ_lệ__=[54,85,68,78]
                        
                    chosen=random.choices(_chọn14_,weights=__tỉ_lệ__,k=1)[0]
                    await chosen.click()
                except:
                    continue
        except:
            continue

        def _dấuhiệu_(before,after):
            try:
                return (after.id == _tinnhan_.id and after.embeds and ("Câu Thành Công" in after.embeds[0].author.name or "Cá Đã Chạy Mất" in after.embeds[0].author.name))
            except:
                return False

        try:
            await TienThanh.wait_for("message_edit", check=_dấuhiệu_)
            await asyncio.sleep(3)
            await channel.send("fs votso")
            def _kiểmtra_rep_(msg): return (msg.author.id == _botID_ and msg.embeds and _daytuido_(msg.embeds[0]))
            try:
                votso_msg = await TienThanh.wait_for("message", check=_kiểmtra_rep_, timeout=5)
                await _tdBáncá_()
            except asyncio.TimeoutError:
                continue
        except:
            pass
        
        await asyncio.sleep(random.randint(3, 6))


TienThanh.run(TOKEN)
