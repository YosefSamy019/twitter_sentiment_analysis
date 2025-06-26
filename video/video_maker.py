from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import cv2

class VideoMaker:
    def __init__(self, video_name, fps = 30,resize_shape = None):
        self.video_name = video_name
        self.fps = fps
        self.frames = []
        self.resize_shape = resize_shape

    def len(self):
        return len(self.frames)

    def append(self, frame):
        self.frames.append(frame)
        
        if self.resize_shape != None:
            self.frames[-1] = cv2.resize(self.frames[-1], self.resize_shape)

    def clear_frames(self):
        self.frames.clear()


    def setText(self, text, txt_position=(0,0), 
                frame_index = -1, scale = 1, 
                color = (255, 0, 0), thickness = 2,
                font = cv2.FONT_HERSHEY_SIMPLEX):  
            
            frame = self.frames[frame_index]
            cv2.putText(frame, text, txt_position, font, scale, color, thickness)
        
        
    def setTextToFrames(self, text, txt_position=(0,0), 
                frame_index_list = range(0,5,2), scale = 1, 
                color = (255, 0, 0), thickness = 2,
                font = cv2.FONT_HERSHEY_SIMPLEX):  
            
            for i in list(frame_index_list):
                self.setText(text, txt_position, i, scale, color, thickness, font)    

    def export(self):
        clip = ImageSequenceClip(self.frames, fps=self.fps)
        clip.write_videofile(self.video_name+'.mp4')
    

        
    def path(self):
        return self.video_name  +'.mp4'
