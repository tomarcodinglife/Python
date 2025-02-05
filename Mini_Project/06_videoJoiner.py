from moviepy import VideoFileClip, concatenate_videoclips


video01 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/01. C++ Course launch   Chai aur C++.mp4")
video02 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/02. Going in depth of Hello World   chai aur C++.mp4")
video03 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/03. Variables and constants in c++.mp4")
video04 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/04. Data types and challenges in C++.mp4")
video05 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/05. Operators and challenges in cpp.mp4")
# video06 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/06. Conditionals and challenges in c++.mp4")
# video07 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/07. Loops in C++.mp4")
# video08 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/08. Functions in c++.mp4")
# video09 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/09. Object Oriented Programming in C++.mp4")
# video10 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/10. Array, dynamic memory and Pointers in Cpp.mp4")
# video11 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/11. Constructor, destructor and Copy Constructor in C++.mp4")
# video12 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/12. Friend Keyword in C++.mp4")
# video13 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/13. Getter Setter and delegating constructor.mp4")
# video14 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/14. Encapsulation, Abstract class, virtual function in c++")
# video15 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/15. Inheritance and final keyword in c++")
# video16 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/16. Building an online store with STL in c++")
# video17 = VideoFileClip("D:/SKS/Video/01. Programming Languages/01 CPP/17. Building Employee Management with STL in C++")

final_clip = concatenate_videoclips(video01, video02, video03, video04, video05)

final_clip.write.videofile("C:/Users/PC/OneDrive/Documents/Python/Mini_Project/outputVideo01.mp4")