
# Automated TollGate Collection System Using Vehicle Number Plate Recognition

This automated toll gate system uses OCR and YOLOv8 for real-time vehicle detection, integrating UPI payments and SMS notifications for quick, cashless transactions. It enhances user convenience, reduces traffic congestion, and ensures scalability, accuracy, and security at toll gates.




## Acknowledgements

 - [LinkPayment deployed in netlify](https://linkpayment.netlify.app)
 - [Twilio link](https://login.twilio.com/u/signup?state=hKFo2SBNanloQU42bndVSXVQNk1faThycmlMUFQ5R2xQRmJiSqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFNBVFFMNU1KQThGQ1h3b0YyU1dtejBxTnk3NDhXNG40o2NpZNkgTW05M1lTTDVSclpmNzdobUlKZFI3QktZYjZPOXV1cks) create an account for sending link via SMS to target.

 


## Demo

Raw image input:

![Overview Image](https://github.com/Akhilad12/Automated-Toll-collection-System-system/blob/main/Test3.jpg?raw=true)

Processed Output:

![Overview Image](https://github.com/Akhilad12/Automated-Toll-collection-System-system/blob/main/train/Test3.jpg?raw=true)

Video input:

[Watch the demo video](https://github.com/Akhilad12/Automated-Toll-collection-System-system/raw/main/train32/Test_1.mp4)


## Installation

Install the required modules listed in the requirements.txt file 

```bash
  pip install -r requirements.txt
```


## Roadmap

- To perform Detection and Recognition (YOLOv8 + easyOCR) run the below command:

```bash
  python predict_modified.py model='ultralytics/runs/detect/train_model/weights/best.pt' source='test_vid.mp4'
```
- Create a twilio account (free version available trial)[https://login.twilio.com/u/signup?state=hKFo2SBNanloQU42bndVSXVQNk1faThycmlMUFQ5R2xQRmJiSqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFNBVFFMNU1KQThGQ1h3b0YyU1dtejBxTnk3NDhXNG40o2NpZNkgTW05M1lTTDVSclpmNzdobUlKZFI3QktZYjZPOXV1cks]

- Enter that account details like phno and  account id's to the api.py file as specified.

- Clone the LinkPay[git clone https://github.com/ptprashanttripathi/linkpe.git]

    1. Change the working directory

    ```bash
     cd linkpe
    ```
    2. Install dependencies
    ```bash
     npm install
    ```
    3. Run the app
    ```bash
     npm start
    ```

- Enter the Upi details and the copy the generated link and paste it in the api.py as mentioned.
- Run api.py file after adding all the required details into the code like upi details, twilio account details 

    ```bash
     python api.py
    ```

- Enter the lisence plate number and the function that fetched respective phone number of it from the dataset.

    ```bash
     http://127.0.0.1:5000/send_payment_link/Enter_license_plate_number
    ```

- You can see a confirmation message in the window and also a SMS with the payment link sent to the target phone number.

     
![Overview Image](https://github.com/Akhilad12/Automated-Toll-collection-System-system/blob/main/Screenshots/confirmation_msg.jpg?raw=true)

- UPI link will be sent to target via twilio api

![Overview Image](https://github.com/Akhilad12/Automated-Toll-collection-System-system/blob/main/Screenshots/SMS_for_Payment.jpg?raw=true)

- Click on that link to proceed with the payment via your prefered phone pay app

![Overview Image](https://github.com/Akhilad12/Automated-Toll-collection-System-system/blob/main/Screenshots/Payment_screenshot.jpg?raw=true)




## 🚀 About Me
Greetings! I'm Akhila, a dedicated student with a strong passion for web development. My ambition is to excel as a Full Stack Developer, where I strive to harmonize creativity and technology to innovate and deliver cutting-edge solutions.

email me for any feedback -->akhilad367@gmail.com
## 🔗 Links


[![LinkedIn](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akhila-d-935ab6212/)

