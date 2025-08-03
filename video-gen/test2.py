# from text_to_video_zero.pipeline import TextToVideoPipeline
# pipe = TextToVideoPipeline(model_id="runwayml/stable-diffusion-v1-5")
#
# video_path = pipe.generate("a dragon flying over a mountain")
# print("video saved at:", video_path)


from text_to_video_zero.pipeline import TextToVideoPipeline
pipe = TextToVideoPipeline(model_id="runwayml/stable-diffusion-v1-5")

video_path = pipe.generate("a dragon flying over a mountain")
print("video saved at:", video_path)