import time
from image_operations import create_text_to_image, generate_image
from utility_operations import test_internet_speed, get_drive_letter

def main():
    if input("Have you connected the Busy Tag device? (y/n): ").strip().lower() == 'y':
        drive_letter = get_drive_letter()
    else:
        print("Please connect the Busy Tag device and restart the program.")
        return

    while True:
        download_speed, upload_speed = test_internet_speed()
        generate_image(download_speed, upload_speed, drive_letter)

        repeat = input("Do you want to repeat the test? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()