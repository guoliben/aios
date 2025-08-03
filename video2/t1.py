import os

# 使用大陆镜像源
os.environ['MODELSCOPE_HUB_MIRROR'] = 'https://modelscope.cn'
os.environ["CURL_CA_BUNDLE"] = ""

from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

# 更换成 damo 稳定模型
p = pipeline('text-to-video-synthesis', 'damo/text-to-video-synthesis')

test_text = {
    'text': 'A panda eating bamboo on a rock.',
}

output_video_path = p(test_text, output_video='./output.mp4')

print('生成完毕:', output_video_path[OutputKeys.OUTPUT_VIDEO])