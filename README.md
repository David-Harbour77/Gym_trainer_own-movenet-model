# Gym_trainer_own-movenet-model

## Introduction

This is the official code of **Deep Dual Consecutive Network for Human Pose Estimation.**

Multi-frame human pose estimation in complicated situations is challenging. Although state-of-the-art human joints detectors have demonstrated remarkable results for static images, their performances come short when we apply these models to video sequences. Prevalent shortcomings include the failure to handle motion blur, video defocus, or pose occlusions, arising from the inability in capturing the temporal dependency among video frames. On the other hand, directly employing conventional recurrent neural networks incurs empirical difficulties in modeling spatial contexts, especially for dealing with pose occlusions. In this paper, we propose a novel multi-frame human pose estimation framework, leveraging abundant temporal cues between video frames to facilitate keypoint detection. Three modular components are designed in our framework. A Pose Temporal Merger encodes keypoint spatiotemporal context to generate effective searching scopes while a Pose Residual Fusion module computes weighted pose residuals in dual directions. These are then processed via our Pose Correction Network for efficient refining of pose estimations. Our method ranks No.1 in the Multi-frame Person Pose Estimation Challenge on the large-scale benchmark datasets PoseTrack2017 and PoseTrack2018. We have released our code, hoping to inspire future research.



![](docs/images/Pipeline.png)



## Visual Results

 <video id="video" controls="" preload="none">     <source id="mp4" src="exe-count(improve).mp4" type="video/mp4"> </video>

#### Mediepipe : movenet


<p align='center'>
	<img src="./exe-count(improve).gif" style="zoom:100%;" />
</p>

#### On PoseTrack


<p align='center'>
	<img src="./mediapipe vs movenet.gif" style="zoom:100%;" />
</p>

