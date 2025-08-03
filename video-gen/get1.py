from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

pipe = pipeline(task=Tasks.text_to_video_synthesis, model='damo/text-to-video-synthesis')
# pipe = pipeline(task=Tasks.text_to_video_synthesis, model='camenduru/text2video-zero')
pipe("一只猫坐在窗台上晒太阳")
