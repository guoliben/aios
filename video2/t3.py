from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

p = pipeline('text-to-video-synthesis', 'iic/text-to-video-synthesis')
test_text = {
        'text': 'A panda eating bamboo on a rock.',
    }
output_video_path = p(test_text, output_video='./output.mp4')[OutputKeys.OUTPUT_VIDEO]
print('output_video_path:', output_video_path)

