# Replit downloader

Downloads all replits from your account.

## How to Find Your Cookie and User-agent
1. Log into your replit account
2. Open developer tools by right clicking and selecting inspect, or by using the keyboard shortcut Ctrl Shift J (Windows) or Cmd Option J (Mac)
![Screen Shot 2022-05-29 at 8 21 35 PM](https://user-images.githubusercontent.com/47932418/170900880-88961dc9-90f5-4d18-b509-ce60122a1dfd.png)

3. Select the Network tab on the top of the developer tools window
![Screen Shot 2022-05-29 at 8 23 12 PM](https://user-images.githubusercontent.com/47932418/170901329-6c258e3e-8035-4440-913a-bd6c0b9ca1ac.png)

4. Refresh Screen
5. Click on any of the rows named graphql from the table
![Screen Shot 2022-05-29 at 8 25 16 PM](https://user-images.githubusercontent.com/47932418/170901341-aaa98982-4445-404e-b102-f1cc186989b2.png)

6. Select the Headers tab on the right of the table
![Screen Shot 2022-05-30 at 10 46 49 AM](https://user-images.githubusercontent.com/47932418/171026752-dd76c54b-c1a4-41d7-b691-082582ea9f5c.png)

7. Scroll down until you find your cookie and user-agent
![Screen Shot 2022-05-30 at 10 48 58 AM](https://user-images.githubusercontent.com/47932418/171026756-e3ca17a7-e01e-4c1a-953a-44b7a10e4c6d.png)


## How to Run the Program
1. Clone this repository
2. Go to your terminal/console. Make sure you have python3 installed
3. Enter the local directory where you have cloned the repository
4. Run ```pip install -r requirements.txt``` to install the dependencies
5. First, run ```main.py``` using ```python3 main.py "your cookie in double quotes" "your user-agent in double quotes"``` to download all files and folders from your replit account. It supports recursive folder structure, and will create a folder called Files to store the downloaded zip files
6. Next, run ```unzipper.py``` using ```python3 unzipper.py``` to unzip the downloaded files. The new files will be moved to a folder called Replits. The Files folder containing the zip files will be deleted after. 
