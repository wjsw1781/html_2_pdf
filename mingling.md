1下载ads-cli  放到home下
wget https://quark.aoss.cn-sh-01.sensecoreapi-oss.cn/ads-cli/release/latest/ads-cli
mv ads-cli ~/ads-cli

2赋予ads-cli可运行权限
chmod 777 ~/ads-cli


3运行 sync_s3_to_oss.sh 脚本
~/ads-cli  sync  s3://Q9NBPHFD3GK5LD9MK6XZ:GKUO7fg8GM5PZwZaQfMnti0jXrCHIxIrbur9BUPq@llm-ft.10.140.27.
254:80/ oss://
LTAI5tBshkhqEQmANgtCCjy1:sHWQzEuzurZ1AGTsXb4J6MmyiOpwYE@oss-dataplatform.oss-cn-wulanchabu.aliyuncs.com/
llm-ft/



<!-- 编辑repo -->
sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-cli]
name=Google Cloud CLI
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM


<!-- 配置yum代理 -->
    sudo vi /etc/yum.conf
    proxy=http://your-proxy-server:port/

<!-- 开始安装 -->

sudo yum install google-cloud-cli


curl -sLo- https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh | bash




~/sensesync --threads=300  --delete-src  --exclude='.gstmp'  cp  /nvme/wzq/ulpl/datasets/  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-raw-snew.10.140.31.254:80/ULIP/ >> /
nvme/wzq/ulpl/mvlog.log 2>&1 

<!-- 进程过滤 强杀 -->

 ps aux | grep 'gsutil' | awk '{print }' | xargs kill -9

 ps aux | grep 'spider_baike' | awk '{print }' | xargs kill -9
<!-- 下载google 存储桶 -->
 nohup gsutil -q -m cp -r  'gs://sfr-ulip-code-release-research/shapenet-55/only_rgb_depth_images' /nvme/
wzq/ulpl/datasets/ > output.log 2>&
1 &





start /B /min cmd.exe /C 'cd D:rojects
ode_electron_yk && jupyter notebook > log.txt 2>&1'


cat > ~/.wgetrc <<EOF
http_proxy=http://10.1.11.100:8086/
https_proxy=http://10.1.11.100:8086/
HTTP_PROXY=http://10.1.11.100:8086/
HTTPS_PROXY=http://10.1.11.100:8086/
use_proxy=on
EOF


cat > ~/.wgetrc <<EOF
http_proxy=http://10.1.11.100:8086/
https_proxy=http://10.1.11.100:8086/
HTTP_PROXY=http://10.1.11.100:8086/
HTTPS_PROXY=http://10.1.11.100:8086/
use_proxy=off
EOF



export http_proxy=http://10.1.11.100:8086/
export https_proxy=http://10.1.11.100:8086/
export HTTP_PROXY=http://10.1.11.100:8086/
export HTTPS_PROXY=http://10.1.11.100:8086/
export use_proxy=on


unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset HTTPS_PROXY
export use_proxy=off








['s3://llm-process-snew/cn-sft-exam/clean/v014/',
's3://llm-process-snew/cn-exam-multip-choice/clean/',
's3://llm-process-snew/cn-sft-exam-panduanti/clean/v009/',
's3://llm-process-snew/cn-sft-exam-tiankong/clean/v010/',
's3://llm-process-snew/cn-sft-exam-multipquiz/clean/v003/',
's3://llm-process-snew/cn-sft-exam-xiezuo-dange/clean/v005/',
's3://llm-process-snew/cn-sft-exam-manytiankong/clean/v002/',
's3://llm-process-snew/cn-sft-exam-multipquiz/clean/v003/']
'

s3://llm-process-snew/artofproblemsolving/


<!-- p----to---snew -->
~/sensesync --threads=300    cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@public-dataset.10.135.3.252:80/
UnifiedQA/  s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-ft.10.140.31.254:80/
pre/raw/public-datasets/v0522/

s3://public-dataset/UnifiedQA/
s3://llm-ft/pre/raw/public-datasets/v0522/


<!-- 解压命令 -->
tar -xf /nvme/wzq/unzip_taisu_wukong/scenenetrgb/SceneNet-train.tar.gz -C ./
tar -xf /nvme/wzq/unzip_taisu_wukong/scenenetrgb/SceneNetRGBD-val.tar.gz -C ./
tar -xf /nvme/wzq/unzip_taisu_wukong/scenenetrgb/train_protobufs.tar.gz -C ./


<!-- 凯士佳  数据移动 -->

git_hub_issue_ksj

aws s3 --profile pjq  cp KSJ.Shanghai_AI_Lab.github_issue.2023063011.json  s3://llm-private-datasets/
git_hub_issue_ksj/ 补充错误的jsonl
s3://llm-private-datasets/midjourney/

aws s3 --profile snew cp /nvme/wzq/2023-09-05-1/weixin_page.2015-12-13.tsv s3://llm-process-snew/
weixin_enroll/test/2015/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/
s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-datasets.10.135.3.252:80/
git_hub_issue_ksj/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/
image_data/  s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-datasets.10.
135.3.252:80/midjourney/image_data/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPj1213wzwzBLJQ@sq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.
254:80/all.jsonl  s3://

<!-- 懒人听书 -->
~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/lrts/  
s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-datasets.10.135.3.252:80/
lrts/mp3/
s3://llm-private-datasets/lrts/mp3/


~/sensesync --threads=300  --delete-src  cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.
3.252:80/lrts/mp3/audio_202308/ s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.3.252:80/
lrts_all/audio_202308/


~/sensesync --threads=300  --delete-src  cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.
3.252:80/lrts/mp3/code_202308/ s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.3.252:80/
lrts_all/code_202308/


~/sensesync --threads=300  --delete-src  cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.
3.252:80/lrts/mp3/jsonl_202308/ s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.3.252:80/
lrts_all/jsonl_202308/

application_1687844242610_0459

sudo ssh -i id_rsa.spark root@10.140.0.104
yarn logs -applicationId application_1682509651585_0508 > wx0508.log
scp -i id_rsa.spark  root@10.140.0.104:/root/wxformat0508.log ./wxformat0508.log

<!-- 统计s3中的文件后缀名 -->
aws s3 --profile snew ls s3://dataset-upload1/lrts/ | awk -F'.' '{if (NF > 1) {print NF}}' | sort | uniq 
-c
53592

[snew]
type = s3
provider = Ceph
access_key_id = SLFOD89FY5RPKJ03BJAE
secret_access_key = 016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG
endpoint = http://10.140.27.254:80
acl = private

[ppp]
type = s3
provider = Ceph
access_key_id = SLFOD89FY5RPKJ03BJAE
secret_access_key = 016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG
endpoint = http://10.135.3.248:80
acl = private

s3://dataset-upload/outputs/quanzhishi/
s3://dataset-upload/outputs/5sing/
s3://llm-private-datasets/quanzhishi-lihe/


rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload/outputs/
quanzhishi/ ppp:llm-private-datasets/
quanzhishi-lihe/
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload/outputs/
5sing/ ppp:llm-private-datasets/
5sing-lihe/


rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload/outputs/
bilibili/ ppp:llm-private-datasets/
bilibili-lihe/
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload/outputs/
douyin/ ppp:llm-private-datasets/
douyin-lihe/

rclone copy --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload/outputs/bilibili/ 
ppp:llm-private-datasets/bilibili-lihe/

 aws s3 --profile snew ls s3://dataset-upload/outputs/bilibili/videos/ | wc -l       193790
aws s3 --profile pjq ls s3://llm-private-datasets/bilibili-lihe/videos/ | wc -l      193790

aws s3 --profile snew ls s3://dataset-upload/outputs/douyin/videos/ | wc -l          1429269
aws s3 --profile pjq ls s3://llm-private-datasets/douyin-lihe/videos/ | wc -l        3048749
/nvme/wzq/lojts/all_testcase


rclone copy   --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload1/lrts/ 
ppp:llm-raw-audio/lrts/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/all.
jsonl  s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-datasets.10.135.3.
252:80/midjourney/

s3://dataset-upload/outputs/cctv_lanmu/
s3://llm-private-dataset-snew/cctv_lanmu-lihe/

~/sensesync --threads=100  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload.10.140.31.254:80/outputs/
cctv_lanmu/  s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-dataset-snew.
10.140.31.254:80/cctv_lanmu-lihe/

<!-- 懒人听书 -->
~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/lrts/  
s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-raw-audio.10.135.3.252:80/lrts/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/lrts/  
s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-datasets.10.135.3.252:80/
lrts/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/qtfm/  
s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-raw-audio.10.135.3.252:80/qtfm/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/qtfm/  
s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-datasets.10.135.3.252:80/
qtfm/

for i in {1..10}; do nohup python3 wiki_en_spider_patch.py i > /dev/null 2>&1 & done
for i in {1..10}; do nohup python3 spider_cnwiki.py i > /dev/null 2>&1 & done


for i in {1..10}; do  nohup python /nvme/wzq/templates/图片下载.py > /dev/null 2>&1 &  done


~/sensesync --threads=300  cp  /nvme/wzq/xmly/mp3_data/  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-raw-audio.
0
135.3.252:80/raw-xmly/mp3_data/

        res={}
        try_time=0
        max_try=3
        while try_time<max_try:
            try:
                proxy=rs.get_proxy_random()
                response = requests.post('https://api.loj.ac/api/submission/querySubmission', 
cookies=cookies, headers=headers, 
proxies=proxy,json=json_data)
                res=response.json()

                if res!={} and 'error' not in res:
                    break
            except Exception as ee:
                print(ee)
                continue
        if res=={}:
            logger.error(f'获取失败  {problemDisplayId}')
            return



pjq --->  snew

rclone copy   --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 pjq:public-dataset/Flan_V2 
snew:llm-ft/pre/raw/public-datasets/
Flan_v2


部署rsyncd服务
每台电脑少都有 rsync命令 但是不一定有rsyncd服务  需要自己安装并配置conf  最后是用systemctl 启动

rsync -avz rsync://rsyncd@10.140.0.66:80/backup ./


高中学库宝
s3://llm-private-datasets/gaozhong-xuekubao/
rclone move --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 /nvme/wzq/unzip_cp_s3_path/
unzip/ pjq:llm-private-datasets/
gaozhong-xuekubao/unzip/
rclone move --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0  /nvme/wzq/unzip_cp_s3_path/
zip/ pjq:llm-private-datasets/
gaozhong-xuekubao/zip/
rclone ls  pjq:llm-private-datasets/gaozhong-xuekubao/zip/

rclone move --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 /nvme/wzq/unzip_cp_s3_path/
logs/ pjq:llm-private-datasets/
gaozhong-xuekubao/logs/


19921001

rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 /nvme/wzq/lojts/all_testcase/  
snew://llm-process-snew/loj/
all_testcase/

<!-- weread 数据转移 -->
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload1/weread/ 
ppp:llm-private-datasets/weread_ksj/
mp3/

nohup ~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@dataset-upload1.10.140.31.254:80/
weread/  s3://SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@llm-private-datasets.10.135.
0
252:80/weread_ksj/mp3/ & 






db.getCollection('zhongguo_da_baikequanshu').aggregate([
  {
    group: {
      _id: 'step',
      count: { sum: 1 }
    }
  }
])
~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection opaczjlib 
--out opaczjlib.jsonl
~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
royalsocietypublishing_detail --out royalsocietypublishing_detail.jsonl
encyclopediaofmath
s2, s3://llm-private-dataset-snew/zhejiangtushuguan/meta_data/

~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
fandong_news_db --collection 
dajiyuan_info --out dajiyuan_info.jsonl     2023822  120G


wget --no-check-certificate  https://kaldir.vc.in.tum.de/matterport/v1/scans/5q7pvUzZiYa/
matterport_depth_images.zip  -c -P  5q7pvUzZiYa/  
wget --no-check-certificate  https://kaldir.vc.in.tum.de/matterport/v1/scans/5q7pvUzZiYa/
matterport_color_images.zip  -c -P 5q7pvUzZiYa/
wget --no-check-certificate  https://kaldir.vc.in.tum.de/matterport/v1/scans/5LpN3gDmAk7/
matterport_depth_images.zip  -c -P 5LpN3gDmAk7/ 
wget --no-check-certificate  https://ftp.ncbi.nlm.nih.gov/pubchem/RDF/descriptor/substance/
pc_descr_SubstanceVersion_type_000001.ttl.gz  -c 

~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
fandong_news_db --collection 
dajiyuan_info --out dajiyuan_info.jsonl     2023822  120G
~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
fandong_news_db --collection 
renminbao_info --out renminbao_info.jsonl   131571   17G
          310090   108G
git filter-branch --force --index-filter 
,
  'git rm --cached --ignore-unmatch parse_zh_jsonl/jsonl/20230906/10_140_84_10_39182_1693964399000.jsonl.
fE4f4Bce' 
,
  --prune-empty --tag-name-filter cat -- --all

~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
fandong_news_db --collection 
rfi_info --out rfi_info.jsonl               310090   108G
aws s3 --profile s2 mv /nvme/wzq/rfi_info.jsonl s3://llm-private-dataset-snew/sensitive_web/rfi_info.

aws s3 --profile s2 mv /nvme/wzq/taduwenxue_queue.jsonl  s3://llm-private-dataset-snew/ta_du_wenxue/
jsonl/ 

~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
--out opaczjlib_gz.jsonl
~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
zhongguo_dabaike2023_dazhong --out zhongguo_dabaike2023_dazhong.jsonl

~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection zhihu_huati 
--out zhihu_huati.jsonl     

~/mongoexport --host 10.140.0.61 --port 27017 -u root -p pjlab_mongo --authenticationDatabase=admin --db 
zhiqiang --collection 
daying_baikequanshu -q '{'step': {'gt': 3}}'  --limit 100 --out exported_data.jsonl


~/mongoexport --host 10.140.0.61 --port 27017 -u root -p pjlab_mongo --authenticationDatabase=admin --db 
zhiqiang --collection 
daying_baikequanshu -q '{'step': {'gt': 3}}'  --out exported_data.jsonl


~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
--out 


~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
--out opaczjlib_nb.jsonl

~/mongoexport --host 10.140.0.61 --port 27017 -u root -p pjlab_mongo --authenticationDatabase=admin --db 
zhiqiang --collection 
daying_baikequanshu -q '{'step':8}'  --out exported_data.jsonl
~/mongoexport --host 10.140.0.61 --port 27017 -u root -p pjlab_mongo --authenticationDatabase=admin --db 
zhiqiang --collection 
taduwenxue_queue -q '{'step':2}'  --limit 100 --out exported_data.jsonl



~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
daying_baikequanshu --out daying_baikequanshu.jsonl

~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
--out opaczjlib_hz.jsonl

~/mongoexport --host 10.140.0.61 --port 27017  -u root -p pjlab_mongo --authenticationDatabase=admin 
zhiqiang --collection 
--out opaczjlib_sz.jsonl
s3://llm-process-snew/zhongguo_da_baikequanshu/jsonl2/


s3://mllm-raw/zhongguo_dabaike/




rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:llm-process-snew/
zhongguo_da_baikequanshu/jsonl2/ 
snew:mllm-raw/zhongguo_dabaike/
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload/outputs/
bilibili/videos_0802/ 
ppp:llm-private-datasets/bilibili-lihe/videos/

outputs/bilibili/videos_0802/*.mp4
s3://dataset-upload1/nowcoder/jsonl
s3://llm-process-snew/nowcoder/jsonl/
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload1/nowcoder/
jsonl/ ppp:llm-private-datasets/
nowcoder/
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload1/nowcoder/
jsonl/ snew:llm-process-snew/
nowcoder/



s3://dataset-upload1/unsplash/image_20231020/   -->  s3://llm-private-dataset-snew/
image/

s3://dataset-upload1/unsplash/jsonl_20231020/  -->  s3://llm-private-dataset-snew/unsplash_img-kaishijia/
jsonl/

~/sensesync --threads=300 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload1.10.140.27.254:80/unsplash/
image_20231020/   s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-dataset-snew.10.140.27.254:80/
unsplash_img-kaishijia/image/

 ~/ads-cli --threads=300 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload1.10.140.27.254:80/unsplash/
image_20231020/   s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-dataset-snew.10.140.27.254:80/
unsplash_img-kaishijia/image/

~/sensesync --threads=300 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload1.10.140.27.254:80/unsplash/
jsonl_20231020/   s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-dataset-snew.10.140.27.254:80/
unsplash_img-kaishijia/jsonl/

~/sensesync --threads=300  cp  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@public-dataset.140.206.95.35:30000/CO3Dv2/
data/ ./
~/sensesync --threads=300  cp ./CO3Dv2/  s3://
SLFOD89FY5RPKJ03BJAE:016DkJPjsq1xIxhGEdFfCfXrDm3FEfS1ZeyVTjTG@public-dataset.140.206.95.
35:30000/CO3Dv2/data/

ppp:llm-private-datasets/bilibili-lihe/bilibili_video_2306.jsonl

--recursive --exclude '*' --include '*.mp4' 

aws --profile up s3 ls s3://dataset-upload/2/

rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload/2/ 
snew:llm-private-dataset-snew/midu/zip/


db.getCollection('lunwen_pjlab_queue').find({step:4})

s3://dataset-upload1/atcode/ 
s3://llm-private-datasets/atcoder/
s3://llm-process-snew/atcoder/

s3://dataset-upload1/codeforces/
s3://llm-private-datasets/codeforces/
s3://llm-process-snew/codeforces/
/nvme/wzq/sensesync --threads=300 cp  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@dataset-upload1.10.140.31.254:80/
atcode/  s3://3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-process-snew.10.140.31.
254:80/atcoder/


while true;do aws s3 --profile pjq mv /nvme/wzq/nssd/files/ s3://llm-private-datasets/nssd/files/ 
--recursive;sleep 3600;done;







/nvme/wzq/sensesync --threads=300 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload1.10.140.31.254:80/
nowcoder/  s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-process-snew.10.140.31.
254:80/nowcoder/

rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload1/atcode/ 
ppp:llm-private-datasets/atcoder/
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 ppp:llm-private-datasets/
atcoder/ snew:llm-process-snew/atcoder/

rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 snew:dataset-upload1/
codeforces/ ppp:llm-private-datasets/
codeforces/
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 ppp:llm-private-datasets/
codeforces/ snew:llm-process-snew/
codeforces/

prefix='s3://llm-common-crawl/crawl-data/' && aws s3 --profile perf ls prefix | awk  -v prefix=prefix '
,{print prefix }' > /nvme/wzq/
mv_perf_p_snew_2_new/perf_cc
prefix='s3://llm-common-crawl/crawl-data/' && aws s3 --profile pjq ls prefix | awk  -v prefix=prefix '
,{print prefix }' > /nvme/wzq/
mv_perf_p_snew_2_new/pjq_cc
prefix='s3://mllm-raw-media/' && aws s3 --profile s2 ls prefix | awk  -v prefix=prefix '{print prefix }' 
> /nvme/wzq/
mv_perf_p_snew_2_new/snew_media



<!-- 常用  mongo数据库查询   -->

db.getCollection('zhongguo_da_baikequanshu').find({

entry_path:{regex:/专题板块/}

})
.count()



db.getCollection('zhongguo_dabaike2023_zhuanye_quanbu').updateMany(
{step:1}, 
{
set:{step:0}
});

db.getCollection('zhongguo_dabaike2023_zhuanye_quanbu').deleteMany(
  { step: 5 }
);

db.getCollection('zhongguo_dabaike2023_zhuanye_quanbu').find({extro:{exists:false}})
.count();

db.getCollection('zhongguo_da_baikequanshu').find({img_list:{ne:[]}})
.count();


db.getCollection('zhongguo_dabaike_zhuanti_quanbu').updateMany({}, {set: {
step: 0
}});


db.getCollection('zhongguo_dabaike_zhuanti_quanbu').find().forEach(function(doc) {
    var urlValue = doc.item['URL'];
    db.getCollection('zhongguo_dabaike_zhuanti_quanbu').updateOne({ _id: doc._id }, { set: { url: 
urlValue } });
});


db.getCollection('zhongguo_dabaike_zhuanti_quanbu').aggregate([
  {
    group: {
      _id: 'step',
      count: { sum: 1 }
    }
  }
])



<!-- 常用  mongo数据库查询   -->





logger_file_name=f'./logs/{os.path.basename(__file__)}_log.log'
logger.add(logger_file_name, format='{time} {level} {message}')


git config --global http.proxy 10.1.11.100:8086 
git config --global https.proxy 10.1.11.100:8086 


git config user.name 'wzq'
git config user.password '1213wzwz'
git config user.email '1781591279@qq.com'
git config  credential.helper store



git config user.name 'wjsw1781'
git config user.password '1781wjsw'
git config user.email '1781591279@qq.com'
git config  credential.helper store



git config user.name 'wangzhiqiang'
git config user.password '1213wzwzBLJQ@'
git config user.email '1781591279@qq.com'
git config  credential.helper store


# 4.修改git用户名、密码、邮箱的配置（跟设置语法一样，没有用户名就添加，有了用户名就修改）
$ git config user.name 'freedom'


# 4.修改git用户名、密码、邮箱的配置（全局配置）
$ git config --global user.name 'freedom'


# 5.删除git用户名、密码、邮箱的配置
8.218.13.95
RUY3NzBBNzUtOTUzMC00@pass2022


8.218.62.26
root
NTAwODBGOUQtNjk5NS
rclone copy --progress --transfers 100 --checkers 50 --s3-upload-cutoff 0 s2:s3://
llm-private-dataset-snew/dianzishu_zhongwenzaixian/数图镜
,像/ ppp:llm-private-datasets/5sing-lihe/

s3://llm-common-crawl/crawl-data/CC-MAIN-2017-22/

/nvme/wzq/sensesync --threads=300 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-dataset-snew.10.140.31.
254:80/dianzishu_zhongwenzaixian/数图镜像/  s3://
5IUH4LWIJPE05J6GAJT7:DOoX3TS7JD2wTOJRWCOnmiP9PMN3nTSNYT5NhKkK@dataset-upload7.10.140.31.
254:80/数图镜像/


task_log/weixin-article/enroll/    1693966206.0783684.log


 aws s3 --profile snew cp /nvme/wzq/weixin_page.2015-06-06 s3://llm-process-snew/weixin_enroll/test/
2015/   271272
 aws s3 --profile snew cp /nvme/wzq/weixin_page.2023-06-06 s3://llm-process-snew/weixin_enroll/test/
2023/   


s3://llm-process-snew/wexin_raw_text/


s3://llm-raw-pnorm/llm-raw-cn-weixin/2023-09-05-1/

s3://llm-process-pnorm/weixin-article/



44G                   wexin_raw_text   45056M
43.7 GiB              enroll                  0.99
1.2 GiB               format                  0.02
616.4 MiB             pre-clean               0.013
621.0 MiB             clean                   0.014


s3://llm-process-snew/weixin-article/enroll/


c
aws s3 --profile snew  ls s3://llm-process-snew/weixin-article/enroll/  --human --summarize
2733494593
    92232445
2141262148             9.9 TiB

aws s3 --profile snew  ls s3://llm-process-snew/weixin-article/pre-clean/v006/  --human   --summarize
2141262148
      0
2141262148             8.7 TiB



aws s3 --profile snew  ls  s3://llm-process-snew/weixin-article/clean/v017/  --human   --summarize

2141262148
144354465
1996907683      8.8 TiB



 aws s3 --profile snew  ls  s3://llm-process-snew/weixin-article/dedup/  --human   --summarize

<!-- lihe li'he 中国语言-->
s3://dataset-upload/outputs/zhongguoyuyan/
s3://llm-process-snew/zhongguoyuyan-lihe/

~/sensesync --threads=100 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload.10.140.27.254:80/outputs/
zhongguoyuyan/ s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.
0
135.3.252:80/zhongguoyuyan-lihe/

~/sensesync --threads=300 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload.10.140.27.254:80/outputs/
zhongguoyuyan/ s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-raw-audio.10.135.3.
252:80/zhongguoyuyan-lihe/

aws s3  --endpoint-url=http://p-ceph-norm-inside.pjlab.org.cn --profile pnorm ls s3://llm-common-crawl/
crawl-data/ 
aws s3   --endpoint-url=http://p-ceph-perf-inside.pjlab.org.cn/ --profile perf ls s3://llm-common-crawl/
crawl-data/  

aws s3   --endpoint-url=http://10.140.86.196  --profile pnorm ls s3://llm-common-crawl/crawl-data

~/sensesync --threads=100 sync  s3://
7X9CWNHIVOHH3LXRD5WK:IHLyTsv7h4ArzReLWUGZNKvwqB7CMrRi6e7ZyUt0@llm-common-crawl.p-ceph-norm-inside.
org.cn s3://7X9CWNHIVOHH3LXRD5WK:IHLyTsv7h4ArzReLWUGZNKvwqB7CMrRi6e7ZyUt0@llm-common-crawl.
p-ceph-perf-inside.pjlab.org.cn

s3://dataset-upload/outputs/cctv_lanmu       s3://llm-private-datasets/cctv_lanmu-lihe/        124.132 
s3://dataset-upload/outputs/cctv_pianku      s3://llm-private-datasets/cctv_pianku-lihe/       6.291 GiB
s3://dataset-upload/outputs/cctv_duanshipin  s3://llm-private-datasets/cctv_duanshipin-lihe/   1.217 GiB
s3://dataset-upload/outputs/mp3jam           s3://llm-private-datasets/mp3jam-lihe/            64.698 GiB
s3://dataset-upload1/cnki                    s3://llm-private-datasets/cnki-ksj/               48.345 GiB


s3://dataset-upload/outputs/jamendo/         s3://public-dataset-snew/jamendo-lihe/

~/sensesync --threads=100 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload.10.140.27.254:80/outputs/
jamendo/ s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@public-dataset-snew.10.140.
0
254:80/jamendo-lihe/

s3://llm-private-dataset-snew/guangzhoutushuguan/meta_data/
s3://llm-private-dataset-snew/hangzhoutushuguan/meta_data/
s3://llm-private-dataset-snew/suzhoutushuguan/meta_data/


~/sensesync --threads=100 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload.10.140.27.254:80/outputs/
cctv_lanmu/ s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.
135.3.248:80/cctv_lanmu-lihe/
~/sensesync --threads=100 cp s3://ai2-public-datasets/satlas/  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.3.248:80/
cctv_lanmu-lihe/

~/sensesync --threads=100 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload.10.140.27.254:80/outputs/
cctv_pianku/ s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.
135.3.248:80/cctv_pianku-lihe/

~/sensesync --threads=100 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload.10.140.27.254:80/outputs/
cctv_duanshipin/ s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.
10.135.3.248:80/
cctv_duanshipin-lihe/


~/sensesync --threads=100 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload.10.140.27.254:80/outputs/
mp3jam/ s3://KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@llm-private-datasets.10.135.3.
248:80/mp3jam-lihe/


~/sensesync --threads=100 cp  s3://
KROZ7YKP0MJ6ZBFQUSE6:6P1291IuEghmerVNDTlxUqGwx9L6HIKBKmSOlPu7@dataset-upload1.10.140.27.254:80/cnki/ 
aws s3 sync s3://ai2-public-datasets/satlas/ -  --no-sign-request --profile awspublic | aws s3 sync - 
s3://public-dataset-snew/satlas/ 
--profile s2

s3://public-dataset-snew/OpenOrca/

s3://llm-ft/pre/raw/public-datasets/v0918/OpenOrca/
s3://llm-ft/pre/raw/public-datasets/v0918/ultrachat/
s3://llm-ft/pre/raw/public-datasets/v0918/Open-Platypus/
s3://llm-ft/pre/raw/public-datasets/v0918/MathInstruct/


~/sensesync --threads=100 cp  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset-snew.10.140.27.254:80/
OpenOrca/ s3://3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-ft.10.140.27.254:80/pre/
raw/public-datasets/v0918/OpenOrca/


~/sensesync --threads=100 cp  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset-snew.10.140.27.254:80/
ultrachat/ s3://3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-ft.10.140.27.254:80/
raw/public-datasets/v0918/
ultrachat/


~/sensesync --threads=100 cp  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset-snew.10.140.27.254:80/
Open-Platypus/ s3://3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-ft.10.140.27.
254
Open-Platypus/



s3://llm-private-dataset-snew/yiqing-yangshiwang/原始粗剪文稿x44/
s3://llm-private-dataset-snew/yiqing-yangshiwang/粗剪文稿x116/

s3://llm-private-dataset-snew/videos-yangshiwang/原始粗剪文稿x44/
s3://llm-private-dataset-snew/videos-yangshiwang/粗剪文稿x116/

~/sensesync --threads=100 sync  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-private-dataset-snew.10.140.27.
254
140.27
254:80/videos-yangshiwang/原始粗剪文稿x44/

~/sensesync --threads=100 sync  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-private-dataset-snew.10.140.27.
254
0
254:80/videos-yangshiwang/粗剪文稿x116/

~/sensesync --threads=100 sync  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-private-dataset-snew.10.140.27.
254
videos-yangshiwang/疫情汇总/


~/sensesync --threads=300 cp  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset.10.135.3.253:80/hdvila/aa 
s3://7X9CWNHIVOHH3LXRD5WK:IHLyTsv7h4ArzReLWUGZNKvwqB7CMrRi6e7ZyUt0@llm-process-pperf.10.140.86.207:80/
hdvila/aa


D:ds-cli.exe --threads=300 sync 'F:情汇总 s3://
3
aws s3 --profile ppp --endpoint-url http://140.206.95.35:30000  sync s3://public-dataset/wujiang_satlas/

~/ads-cli --threads=20 sync ./wujiang/   s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset.140.206.95.
35:30000/wujiang_satlas/




-cli.exe --threads=300 sync D:视紧急 s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@llm-private-dataset-snew.10.140.
27.254:80/yiqing-yangshiwang/

s3://public-dataset/hdvila/
s3://public-dataset/COYO-700M/


aws s3 --profile perf    ls s3://llm-weixin/unar/  --human |  grep 'weixin_page.2021'  | awk '{sum += } 
END {print sum/1024}'

aws s3 --profile perf    ls s3://llm-weixin/weixin-article/enroll/ | grep -i 'sum'   
==============================
      rows: 2158581352  2158581352
     bytes: {'sum': 546539271193988, 'min': 12689, 'max': 15738789, 'cnt': 2158581352, 'avg': 253193.733}
    cbytes: {'sum': 487559853099080, 'min': 11802, 'max': 11603668, 'cnt': 2158581352, 'avg': 225870.502}
     files: 470717
   dropped: 574913241
 sub_paths: {}
==============================

s3://public-dataset/YT-Temporal-media/videos/


split -l 200000 -d --additional-suffix=.jsonl opaczjlib_gz.jsonl opaczjlib_gz_




19.2MiB	936			'原始爬取路径 pnorm s3://crawl-data/baeldung/original_jsonl/
格式转换路径 pnorm s3://crawl-data/baeldung/format_jsonl/
pip install xonsh

pip3 install  xonsh loguru --proxy=http://10.1.11.100:8086 

pip install awscli==1.16.6 -i https://pypi.tuna.tsinghua.edu.cn/simple  --proxy=http://10.1.11.100:8086 

pip install awscli-plugin-endpoint -i https://pypi.tuna.tsinghua.edu.cn/simple --proxy=http://10.1.11.100:8086 

aws configure set plugins.endpoint awscli_plugin_endpoint


git 移除已经追踪的文件
git ls-files --full-name | grep wiki_git | xargs git rm --cached

~/ads-cli --threads=100  cp  s3://
I9FS5NXG0G3MZ9VL8QFI:Jhj1mIrkhuWxFhxbald80DhhOCSbatZrkQXY58f7@public-dataset.10.135.3.248:80/makeuseof/
raw-images/ s3://OA8AZVFH6110XW4A51NX:aZ5XfNpTZ8xSAa9lcs7MhYAy7wGr3WAzhzO5AfR8@crawl-data.10.140.86.
161:80/makeuseof/raw-images/


~/ads-cli   cp  s3://I9FS5NXG0G3MZ9VL8QFI:Jhj1mIrkhuWxFhxbald80DhhOCSbatZrkQXY58f7@public-dataset.10.135.
3.248:80/makeuseof/raw-images/
00904dfec4d5606cb55ef9ef926b379c5737669cf4a3212ae1d5f3f3e9e2f862 ./

s5cmd --credentials-file ~/.aws/credentials --profile ~/.aws/config ls s3://my-company-bucket/

///////////////////////////////////////////////////////////////////////////////////////////////
aws_access_key_id = 7X9CWNHIVOHH3LXRD5WK
aws_secret_access_key = IHLyTsv7h4ArzReLWUGZNKvwqB7CMrRi6e7ZyUt0

aws_access_key_id = 3IMPDVQE98DCLAFZZLH1
aws_secret_access_key = sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi


s3://data_temp/YT-Temporal-media/

s3://public-dataset/YT-Temporal-media/

perf----------------------->p  2个
snew----------------------->p  1个 就是那个180m s3://public-dataset-snew/youtobe_media/videos/


s3://public-dataset/YT-Temporal-media/

~/ads-cli --threads=100  sync  s3://
4CZLCQ4I3246LCWV4NGH:frEPkjqOHRtNeDqjijV59ANAi589zFMmjiErOJig@data_temp.10.140.86.209/
YT-Temporal-media/  s3://3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset.10.
135.3.248:80/YT-Temporal-media/

~/ads-cli --threads=100  sync  s3://
7X9CWNHIVOHH3LXRD5WK:IHLyTsv7h4ArzReLWUGZNKvwqB7CMrRi6e7ZyUt0@public-dataset.10.140.86.209/
YT-Temporal-media/  s3://3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset.10.
135.3.248:80/YT-Temporal-media/



~/ads-cli --threads=100  sync  s3://
3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset-snew.10.140.27.254:80/
youtobe_media/videos/  s3://3IMPDVQE98DCLAFZZLH1:sBfzmuzAf9sAjlUjjw33IPBvT11pNgotdUfs1igi@public-dataset.
10.135.3.248:80/YT-Temporal-media/
videos/


///////////////////////////////////////////////
~/ads-cli --threads=100  sync  s3://
7X9CWNHIVOHH3LXRD5WK:IHLyTsv7h4ArzReLWUGZNKvwqB7CMrRi6e7ZyUt0@llm-tokens-pperf.10.140.86.211/ s3://
OA8AZVFH6110XW4A51NX:aZ5XfNpTZ8xSAa9lcs7MhYAy7wGr3WAzhzO5AfR8@llm-tokens-pperf.10.140.86.171:80/




<!-- 完全以主分支为主 -->
git fetch origin
git reset --hard origin/main
<!-- 或者用这个 -->
git fetch origin
git reset --hard origin/master





~/sensesync138 put  s3://7X9CWNHIVOHH3LXRD5WK:IHLyTsv7h4ArzReLWUGZNKvwqB7CMrRi6e7ZyUt0@llm-tokens-pperf.
10.140.86.211/
1025_v7_tokenized_913_safe_data/
_SUMMARY_rows_4292204834_bytes_21090571851382_tokens_3869209194003_files_5344 s3://
OA8AZVFH6110XW4A51NX:aZ5XfNpTZ8xSAa9lcs7MhYAy7wGr3WAzhzO5AfR8@llm-tokens-pperf.10.140.86.171:80/
1025_v7_tokenized_913_safe_data/
_SUMMARY_rows_4292204834_bytes_21090571851382_tokens_3869209194003_files_5344