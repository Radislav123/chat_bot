from datetime import datetime, timedelta, time
from timeloop import Timeloop
from service import *


tl = Timeloop()
zero_time = time()
rest_from = time(hour = 21)
rest_to = time(hour = 9)
# At this hour users with 24-hour timer period will receive theirs broadcasts
hour_delta = 12


def add_jobs(chats_ids):
    # Use protected method because public does not have arguments for executable
    tl._add_job(broadcast_course_fragments, timedelta(hours = 1), chats_ids)


def broadcast_course_fragments(chats_ids):
    for chat_id in chats_ids:
        if (datetime.now().hour + hour_delta) % chats_ids[chat_id] == 0:
            bot.send_message(chat_id, BROADCAST_ADDITIONAL_TEXT + get_random_course_fragment())
