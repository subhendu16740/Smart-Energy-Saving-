# Smart-Energy-Saving

# Notification to student
  Our idea is focussed on saving the power consumption in hostels of educational institute. We plan on installing a cost effective system which will notify the student about power wastage in his room. 
We’ll develop a real-time automatic notification alert system for saving electricity by detection of human using computer vision. We’ll use a Raspberry Pi with OpenCV libraries installed along with piCam to detect the person’s presence, and let the user choose one of the actions listed in the notification. We’ll carry out detection of a human body in OpenCV in python using haar cascades.
Our idea is to install a IOT-based cost effective system which will do the following things :-
1. Notify the student of power wastage during his absence through a very simple android app.
2. We’ll select a threshold amount of time after which the student will be notified that he forgot to turn off the appliances and he’s supposed to turn them off save energy and money.
3. The notification will include the amount of energy consumed since he last received the notification and predicted amount of money that may cost him given that he forgets to turn off the appliances. 
So to deal with this, we’ll first list out all the appliances (input a dataset with a list of appliances along with their power ratings) that are typically used in our institute’s hostel along with their power ratings and make a pie chart with the help of that table. We’ll be using the matplotlib and plotly libraries in python to make the pie chart. This part of our model will be responsible for selection of 2 appliances with the highest percentage of area occupied in the pie chart made above. 
The model will be highly inefficient if it turns off the appliances even if the user is undetected for a second. So we’ll need a threshold time. And after a given threshold time, say 20 minutes, if the student is still undetected, then we’ll send the student a notification to let him know that he forgot to turn off the appliances. 
It is commonly observed that there is a linear relation between the energy being consumed/wasted and the amount of money that it will cost us. Energy consumed (power * time) is directly proportional to the amount of extra money it will cost the institute. So we’ll make our project with that assumption in our mind. The machine learning strategy that we’ll be using here is multiple linear regression  to predict the amount of money that may cost the institute if student forgets to turn off the appliances. The predicted amount of money depends on the energy consumption of the appliances. The android app will receive the notification. The student gets two choices –
1.	Switch off the appliances
2.	I am still here (in case the user doesn’t want to turn them off)
Default case : No action will be taken, since the user has intentionally left them turned on for his own use.
The user then makes appropriate choice and signals are send to raspberry module for further action.
