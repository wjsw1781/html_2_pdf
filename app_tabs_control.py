
import os
import platform
import random
import time
from DrissionPage import ChromiumOptions, ChromiumPage
from loguru import logger
from random_user_agent.user_agent import UserAgent

from random_user_agent.params import  OperatingSystem


operating_systems = [OperatingSystem.WINDOWS.value]   

UA = UserAgent(limit=100,operating_systems=operating_systems)


def get_chrome_page(pid_user_data_path,wutou=True,user_port=9222,co=None):
    try:
        if co==None:
            if platform.system() == 'Windows':
                co = ChromiumOptions().set_user_data_path(pid_user_data_path).set_local_port(user_port)
            else:
                co = ChromiumOptions().set_browser_path('/usr/bin/google-chrome').set_user_data_path(pid_user_data_path).set_local_port(user_port)
            if wutou:
                co.headless()
            co.set_retry(0)
            # user_agent = UA.get_random_user_agent()
            user_agent =f"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.9) Gecko/20100101 Goanna/3.2 Firefox/{random.randint(45, 50)}.9 PaleMoon/{random.randint(2, 27)}.3.0"
            co.set_user_agent(user_agent)
            co.set_pref(arg='profile.default_content_settings.popups', value='0')
            co.set_argument('--hide-crash-restore-bubble')
        page = ChromiumPage(co)
        page.set.window.max()
        page.set.download_path(f'{pid_user_data_path}/download/')

        time.sleep(5)

        return page
    except Exception as e:
        stop_pid_by_port=f"""netstat -pltun | grep {user_port}  | awk '{{print $7}}'   | awk -F '/' '{{print $1}}'  | xargs kill -9 """
        for i in range(3):
            os.system(stop_pid_by_port)
        raise e



