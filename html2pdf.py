


# -*- coding: utf-8 -*-
import json
import shutil
import sys,os
import threading

from loguru import logger
basedir = os.path.dirname(__file__)
parent_dir = os.path.dirname(basedir)
when_import_the_module_the_path=os.path.dirname(__file__)

project_dir=basedir 
# 遍历所有父节点目录 如果存在readme.md文件 就返回那个目录
while True:
    if os.path.exists(os.path.join(project_dir, 'readme.md')):
        break
    project_dir = os.path.dirname(project_dir)
    if project_dir==os.path.dirname(project_dir):
        raise ValueError('未找到项目根目录')

sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))
sys.path.append(os.path.dirname(os.path.dirname(parent_dir)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(parent_dir))))

myenv=f'{project_dir}/myenv/Lib/site-packages/'
sys.path.append(myenv)


os.chdir(basedir)

print('basedir-------------->',basedir)
sys.path.append(basedir)
import os
import signal
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

from loguru import logger
signal_on = True
def close(signum, frame):
    global signal_on, executor
    signal_on = False
    print(f'closing spider by signal {signum}')
    try:
        active_count = executor._threads.__len__()  # 活动线程数
        queue_size = executor._work_queue.qsize()  # 工作队列大小
        print(f'executor status: 活动线程数 ={active_count}, 工作队列大小={queue_size}')
    except Exception as e:
        pass
signal.signal(signal.SIGINT, close)
signal.signal(signal.SIGTERM, close)



from app_tabs_control import get_chrome_page
from DrissionPage._pages.chromium_tab import ChromiumTab



def tell_to_wx_group(info):
    import requests
    data={
    'msgtype': 'text',
    'text': {
        'content': info,

    }
    }

    url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8e42f959-654d-4fd2-b1f5-11247ccf47d8'
    try:
        requests.post(url=url,json=data)
    except Exception as e:
        logger.error(f'  发送微信群消息失败  {e}  ')	


def cp_s3_file(aws_config,in_s3_file):
    local_base_s3_file=os.path.abspath(f'./{os.path.basename(in_s3_file)}')
    if os.path.exists(local_base_s3_file):
        return local_base_s3_file
    
    cmds=f'aws s3 --profile {aws_config} cp {in_s3_file} {local_base_s3_file}'
    for i in range(10):
        status=os.system(cmds)
        if status==0:
            return local_base_s3_file
    tell_to_wx_group(f'  {cmds}  执行失败 批量转化html--->pdf 第一步要先把jsonl下载到本地  ')
    return False


def pdfbinary_2_base_64(pdf_binary):
    import base64
    pdf_binary_base64=base64.b64encode(pdf_binary).decode('utf-8')
    return pdf_binary_base64


def get_queue_list():
    import queue

    q = queue.Queue()
    return q



def html_to_pdf(josnl):
    global all_tabs,result_queue,error_queue
    tid = int(str(threading.current_thread()._name).split('_')[-1])
    current_tab :ChromiumTab =all_tabs[tid]
    item=json.loads(josnl)

    new_html=item['new_html']
    track_id=item['track_id']

    temp_html_file=f'{os.path.abspath(f"./temp_html/{track_id}.html")}'
    with open(temp_html_file,'w',encoding='utf-8') as ff:
        ff.write(new_html)

    try:
        current_tab.get(temp_html_file,show_errmsg=True,timeout=3)
        pdf_binary=current_tab.save(as_pdf=True)
        pdf_base64=pdfbinary_2_base_64(pdf_binary)
        item['pdf_base64']=pdf_base64
        new_josnl=json.dumps(item,ensure_ascii=False)

        result_queue.put(new_josnl)

        logger.success(f'  {temp_html_file}  执行成功   ')

    except Exception as e:
        logger.error(f'  {temp_html_file}  执行失败  {e}  ')
        item['error_msg']=str(e)
        new_josnl=json.dumps(item,ensure_ascii=False)

        error_queue.put(item)
        return
    

def queue_to_local_to_s3(aws_config,out_s3_file):
    base_name=os.path.basename(out_s3_file)
    output_local_file=os.path.abspath(f'./output_jsonl/{base_name}')

    with open(output_local_file,'w',encoding='utf-8') as ff:
        while not result_queue.empty():
            new_josnl=result_queue.get()
            ff.write(new_josnl+'\n')

    cmds=f'aws s3 --profile {aws_config} mv {output_local_file} {out_s3_file}'
    
    for i in range(10):
        status=os.system(cmds)
        if status==0:
            return True
    tell_to_wx_group(f'  {cmds}  执行失败 批量转化html--->pdf jsonl 推送到s3上  ')
    return False

def error_queue_to_local_to_s3(aws_config,error_out_s3_file):
    base_name=os.path.basename(error_out_s3_file)
    output_local_file=os.path.abspath(f'./error_jsonl/{base_name}')

    with open(output_local_file,'w',encoding='utf-8') as ff:
        while not result_queue.empty():
            new_josnl=result_queue.get()
            ff.write(new_josnl+'\n')

    cmds=f'aws s3 --profile {aws_config} mv {output_local_file} {error_out_s3_file}'
    
    for i in range(10):
        status=os.system(cmds)
        if status==0:
            return True
    tell_to_wx_group(f'  {cmds}  执行失败 批量转化html--->pdf jsonl 推送到s3上  ')
    return False


aws_config='dataproc_out'
in_s3_file='s3://llm-pdf-text/20240624/after_tiqu_html_content_then_pdf/v003/part-667957fa7be8-004719.jsonl'
out_s3_file='s3://llm-pdf-text/20240624/after_html_save_pdf_ok/v003/part-667957fa7be8-004719.jsonl'
error_out_s3_file='s3://llm-pdf-text/20240624/after_html_save_pdf_error/v003/part-667957fa7be8-004719.jsonl'


# 线程数量
max_work = 10

# 进程标识
process_num=100
# 关闭无头    # 开启无头
wutou=False
wutou=True

# 拉起chrome进程
pid_user_data_path=os.path.abspath(f'./user_data/{process_num}')
page=get_chrome_page(pid_user_data_path,wutou=wutou,user_port=9222+process_num)


#工作节点tab
all_tabs=[]
for i in range(max_work):
    all_tabs.append(page.new_tab())

# 结果保存队列 线程安全
result_queue = get_queue_list()
# 失败保存队列线程  
error_queue = get_queue_list()

# 线程池
executor = ThreadPoolExecutor(max_work)


# 准备工作目录
os.makedirs(os.path.abspath('./temp_html/'), exist_ok=True)
os.makedirs(os.path.abspath('./error_jsonl/'), exist_ok=True)
os.makedirs(os.path.abspath('./output_jsonl/'), exist_ok=True)
os.makedirs(os.path.abspath('./user_data/'), exist_ok=True)

if __name__ == '__main__':

    local_base_s3_file=cp_s3_file(aws_config,in_s3_file)
    if not local_base_s3_file:
        raise ValueError('  cp_s3_file  执行失败  ')
    
    all_josnl=open(local_base_s3_file,'r',encoding='utf-8')

    for i,josnl in enumerate(all_josnl):

        while executor._work_queue.qsize() > max_work:
            logger.info(f'<----  线程池已满  ----> { executor._work_queue.qsize() } 完成个数 {result_queue.qsize()}  失败个数 {error_queue.qsize()}')
            time.sleep(2)
            time.sleep(2)
            continue

        if not signal_on:
            logger.info('<----  退出线程池  ----> ')
            break


        executor.submit(html_to_pdf, josnl,)


    executor.shutdown(wait=True)
    all_josnl.close()

    # 处理成功队列
    queue_to_local_to_s3(aws_config,out_s3_file)
    # 处理失败队列
    error_queue_to_local_to_s3(aws_config,error_out_s3_file)

    
    # 删除本地文件
    os.remove(local_base_s3_file)
    
    # 批量删除本地文件夹
    shutil.rmtree(os.path.abspath('./temp_html/'), ignore_errors=True)

    logger.info(' control c  ----> ')
    logger.info('<----  退出线程池  ----> ')
    os._exit(0)


"""

aws s3 --profile dataproc_out ls s3://llm-pdf-text/20240624/after_tiqu_html_content_then_pdf/v003/part-667957fa7be8-004719.jsonl

"""















