import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000
    print(f"Download speed: {download_speed:.2f} Mbps")
    
    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000
    print(f"Upload speed: {upload_speed:.2f} Mbps")

    return download_speed, upload_speed

def get_drive_letter():
    while True:
        drive_letter = input("Please enter the drive letter assigned to Busy Tag device (e.g., D): ").strip().upper()
        if len(drive_letter) == 1 and drive_letter.isalpha():
            return drive_letter
        else:
            print("Invalid drive letter. Please enter a single letter (e.g., D).")