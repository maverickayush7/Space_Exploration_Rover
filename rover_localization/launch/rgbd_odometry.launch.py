from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    parameters = [
        {
            "frame_id": "base_link",
            "subscribe_depth": True,
            "subscribe_rgb": True,
            "approx_sync": True,
            "approx_sync_max_interval": 0.01,
            "publish_tf": False,
            "wait_imu_to_init": False,
            "publish_null_when_lost": False,
            "qos": 2,
            "qos_camera_info": 2,
            # 0=TORO, 1=g2o, 2=GTSAM and 3=Ceres
            "Optimizer/Strategy": "2",
            "Optimizer/GravitySigma": "0.0",
            # 0=Frame-to-Map (F2M) 1=Frame-to-Frame (F2F) 2=Fovis 3=viso2 4=DVO-SLAM 5=ORB_SLAM2 6=OKVIS 7=LOAM 8=MSCKF_VIO 9=VINS-Fusion 10=OpenVINS 11=FLOAM 12=Open3D
            "Odom/Strategy": "0",
            "Odom/ResetCountdown": "1",
            "Odom/Holonomic": "false",
            # 0=No filtering 1=Kalman filtering 2=Particle filtering
            "Odom/FilteringStrategy": "1",
            "Odom/ParticleSize": "500",
            "Odom/GuessMotion": "true",
            "Odom/AlignWithGround": "false",
            "OdomF2M/MaxSize": "5000",
            "OdomF2M/ScanMaxSize": "5000",
            "GFTT/MinDistance": "7.0",
            "GFTT/QualityLevel": "0.001",
            "GFTT/BlockSize": "3",
            "GFTT/UseHarrisDetector": "true",
            "GFTT/K": "0.04",
            "SURF/Extended": "true",
            "SURF/HessianThreshold": "500",
            "SURF/Octaves": "4",
            "SURF/OctaveLayers": "4",
            "SURF/Upright": "false",
            "SURF/GpuVersion": "false",
            "SURF/GpuKeypointsRatio": "0.01",
            "SIFT/NFeatures": "1000",
            "SIFT/NOctaveLayers": "4",
            "SIFT/RootSIFT": "false",
            "FREAK/OrientationNormalized": "true",
            "FREAK/ScaleNormalized": "true",
            "FREAK/PatternScale": "30",
            "FREAK/NOctaves": "4",
            "KAZE/Extended": "true",
            "KAZE/Upright": "false",
            "KAZE/NOctaves": "4",
            "KAZE/NOctaveLayers": "4",
            # 0=DIFF_PM_G1, 1=DIFF_PM_G2, 2=DIFF_WEICKERT or 3=DIFF_CHARBONNIER
            "KAZE/Diffusivity": "1",
            "BRIEF/Bytes": "64",
            # Motion estimation approach: 0:3D->3D, 1:3D->2D (PnP), 2:2D->2D (Epipolar Geometry)
            "Vis/EstimationType": "1",
            "Vis/ForwardEstOnly": "true",
            # 0=SURF 1=SIFT 2=ORB 3=FAST/FREAK 4=FAST/BRIEF 5=GFTT/FREAK 6=GFTT/BRIEF 7=BRISK 8=GFTT/ORB 9=KAZE 10=ORB-OCTREE 11=SuperPoint 12=SURF/FREAK 13=GFTT/DAISY 14=SURF/DAISY 15=PyDetector
            "Vis/FeatureType": "8",
            "Vis/DepthAsMask": "true",
            "Vis/CorGuessWinSize": "40",
            "Vis/MaxFeatures": "0",
            "Vis/MinDepth": "0.0",
            "Vis/MaxDepth": "0.0",
            # 0=Features Matching, 1=Optical Flow
            "Vis/CorType": "0",
            # kNNFlannNaive=0, kNNFlannKdTree=1, kNNFlannLSH=2, kNNBruteForce=3, kNNBruteForceGPU=4, BruteForceCrossCheck=5, SuperGlue=6, GMS=7
            "Vis/CorNNType": "1",
        }
    ]

    remappings = [
        ("rgb/image", "camera/image_raw"),
        ("rgb/camera_info", "camera/camera_info"),
        ("depth/image", "camera/depth/image_raw"),
        ("imu", "imu"),
        ("odom", "odom_rgbd"),
    ]

    return LaunchDescription(
        [
            Node(
                package="rtabmap_odom",
                executable="rgbd_odometry",
                output="log",
                parameters=parameters,
                remappings=remappings,
                arguments=["--ros-args", "--log-level", "Error"],
            ),
        ]
    )
