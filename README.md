# XHRToCSV
parses an HAR file to create a report with the list of XHR requests made and their respective response time.

Only supports Google Chrome Browser as of Now.

Requirements : Python 3.X installed.

Procedure :

Open the developer tools and Networks Tab.

![image](https://user-images.githubusercontent.com/19332610/114358325-6c546c00-9b90-11eb-9733-7a85b62c38f7.png)

Perform all the browsers actions.
Click on the Download Icon in the Network Tab.

![image](https://user-images.githubusercontent.com/19332610/114358429-89893a80-9b90-11eb-9693-e5383ed73e88.png)

Save the image in the same folder as this script.

Run the Script by executing the command ```python requestList.py```
if you have multiple versions of python installed, run ``python3 requestList.py```

For Linux and Mac, Run ```python3 requestList.py```
