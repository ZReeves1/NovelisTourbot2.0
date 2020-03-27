#include <string>
#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>
#include <geometry_msgs/Twist.h>

geometry_msgs::Twist move;

void cmdVelCallback(const geometry_msgs::Twist& vel_cmd){
    ROS_INFO("I heard: [%f]", vel_cmd.linear.y);
    std::cout << "Twist Received " << std::endl;
    move = vel_cmd; 
  
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "state_publisher");
    ros::init(argc, argv, "cmd_vel_listener");
    ros::NodeHandle n;
    ros::NodeHandle cvl;
    ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1);
    ros::Subscriber sub = cvl.subscribe("/cmd_vel", 1000, cmdVelCallback);
    tf::TransformBroadcaster broadcaster;
    ros::Rate loop_rate(30);

    const double degree = M_PI/180;

    // robot state
    double tilt = 0, tinc = degree, swivel=0, angle=0, height=0, hinc=0.005;
    double newx = 0, newy=0, newth = 0;
    double oldx = 0, oldy = 0, oldth = 0;
    
    // message declarations
    geometry_msgs::TransformStamped odom_trans;
    sensor_msgs::JointState joint_state;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "base_link";

    while (ros::ok()) {
/*
        //update joint_state
        joint_state.header.stamp = ros::Time::now();
        joint_state.name.resize(3);
        joint_state.position.resize(3);
        joint_state.name[0] ="swivel";
        joint_state.position[0] = swivel;
        joint_state.name[1] ="tilt";
        joint_state.position[1] = tilt;
        joint_state.name[2] ="periscope";
        joint_state.position[2] = height;
*/

        // update transform
        // (moving in a circle with radius=2)

        newx = move.linear.x;
        newy = move.linear.y;
	newth = move.angular.z;
        odom_trans.header.stamp = ros::Time::now();
        odom_trans.transform.translation.x = newx-oldx;
        odom_trans.transform.translation.y = newy-oldy;
        odom_trans.transform.translation.z = 0.08;
        odom_trans.transform.rotation = tf::createQuaternionMsgFromYaw(newth-oldth);

        //send the joint state and transform
        //joint_pub.publish(joint_state);
        broadcaster.sendTransform(odom_trans);

        // Create new robot state
        //tilt += tinc;
        //if (tilt<-.5 || tilt>0) tinc *= -1;
        //height += hinc;
        //if (height>.2 || height<0) hinc *= -1;
        //swivel += degree;
        angle += degree/4;
        oldx = newx;
        oldy = newy;
        oldth = newth;
        // This will adjust as needed per iteration
        loop_rate.sleep();
    }


    return 0;
}

