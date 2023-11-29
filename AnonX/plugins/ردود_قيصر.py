from pyrogram.types import Message
from database import del_db_lockwelcome, get_db_lockwelcome, set_db_lockwelcome, get_db_lockbye, set_db_lockbye, \
    del_db_lockbye


########################################################################################################################
########################################################################################################################

async def lock_lockwelcome_open(m: Message):
    del_db_lockwelcome(m.chat.id)
    await m.reply_text("◍ تم فتح الترحيب\n√", reply_to_message_id=m.message_id)


async def lock_lockwelcome_close(m: Message):
    if get_db_lockwelcome(m.chat.id) is None:
        set_db_lockwelcome("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الترحيب\n√", reply_to_message_id=m.message_id)
        return
    else:
        for per in get_db_lockwelcome(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ الترحيب مقفول بالفعل\n√", reply_to_message_id=m.message_id)
                return
        set_db_lockwelcome("yes", m.chat.id)
        await m.reply_text("◍ تم قفل الترحيب\n√", reply_to_message_id=m.message_id)
        return


def lock_lockwelcome_test(m: Message):
    leader = True
    if get_db_lockwelcome(m.chat.id) is None:
        leader = True
    else:
        for per in get_db_lockwelcome(m.chat.id):
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_lockbye_open(m: Message):
    del_db_lockbye(m.chat.id)
    await m.reply_text("◍ تم فتح المغادره\n√", reply_to_message_id=m.message_id)


async def lock_lockbye_close(m: Message):
    if get_db_lockbye(m.chat.id) is None:
        set_db_lockbye("yes", m.chat.id)
        await m.reply_text("◍ تم قفل المغادره\n√", reply_to_message_id=m.message_id)
        return
    else:
        for per in get_db_lockbye(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("◍ المغادره مقفوله بالفعل\n√", reply_to_message_id=m.message_id)
                return
        set_db_lockbye("yes", m.chat.id)
        await m.reply_text("◍ تم قفل المغادره\n√", reply_to_message_id=m.message_id)
        return


def lock_lockbye_test(m: Message):
    leader = True
    if get_db_lockbye(m.chat.id) is None:
        leader = True
    else:
        for per in get_db_lockbye(m.chat.id):
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################
