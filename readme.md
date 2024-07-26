# Internet Speed Test

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

This project measures the internet speed (both download and upload) and displays the results on a Busy Tag device. The results are rendered as an image and saved to the Busy Tag device's drive.

## Project Purpose

The main goal of this project is to:
	
- Test and measure the current internet download and upload speeds.

- Generate an image displaying the measured speeds.

- Allow users to repeat the test and update the image as needed.

## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.6 or higher
- `Pillow` (PIL Fork) - Python Imaging Library
- `speedtest-cli` package
- An active internet connection to test the speeds.

## Installation
 
  To get started with this Python script, follow these steps:

1. **Clone the repository:**
   First, clone the repository from GitHub to your local machine.
   ```
   git clone https://github.com/busy-tag/Internet_speed_test.git
2. Navigate to the cloned repository:

	```
	cd Internet_speed_test
	```
3. Install the required dependencies:
	Use `pip` to install the necessary packages.
	
	```
	pip install speedtest-cli Pillow
	```

4. Ensure the default font file `MontserratBlack-3zOvZ.ttf` is in the project directory.

## Configuration

The script provides several customizable parameters:
 
• **Drive Letter:** Prompted input for the drive letter where the Busy Tag device is located (e.g., `D`).

• **Text Content:** Displays location and temperature data.

• **Font Size and Colors:** Predefined but can be modified in the script.


## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python main.py
```
2. **Provide Drive Letter:**
   
    The script will prompt you to enter the drive letter assigned to the Busy Tag device. Enter the letter (e.g., `D`) and press Enter.
         
3. **Script Operation:**

	The script will test the current internet download and upload speeds, and generate an image (`speed_data.png`) displaying these speeds. You will be prompted to repeat the test if desired.
	
4. **Output:**
	
	The generated image will be saved in the specified directory (e.g., `D:`) and will be updated every 10 minutes.
	
### Example

After running the script, you should see output similar to this in your terminal:
```
Have you connected the Busy Tag device? (y/n): y
Please enter the drive letter assigned to Busy Tag device (e.g., D): D
Testing download speed...
Download speed: 73.50 Mbps
Testing upload speed...
Upload speed: 37.50 Mbps
Do you want to repeat the test? (y/n): n
Exiting the program.
```

And an image (speed_data.png) will be saved in the specified directory (e.g., D:), displaying the following information:
```
Download speed:
73.50 Mb/s
Upload speed:
37.50 Mb/s
```

Sample:

<img src="/speed_data_sample.png" alt="alt Sample Image" width="480" height="560"/>

### Troubleshooting ###

If you encounter any issues, ensure:

All Python packages are installed correctly.

The font file (`MontserratBlack-3zOvZ.ttf`) is present in the project directory.

You have an active internet connection.

The drive letter is correct and the Busy Tag device is connected.

For any additional help, please open an issue in the repository or contact the maintainer.
