from datetime import datetime, time
import os
import subprocess
import schedule

EXIT_MAIN: bool = False
EXIT: bool = False
COUNT: int = 0

def add_error(error_str: str)-> None:
    """_summary_

    Args:
        error_str (str): _description_
    """

    error_file_path: str = os.getcwd + '/speedtest-data/error.txt'

    with open(error_file_path, 'a') as error_file:
            error_file.write(error_str.decode('utf-8'))
            error_file.close()
            EXIT = True
            EXIT_MAIN = True
            return
    
def add_csv_line(output:str) -> None:

    data_file_path: str = os.getcwd() + '/speedtest-data/speedtest_data.csv'
    with open(data_file_path,'a') as csv_file:
        csv_file.write(output)
        csv_file.close()
        return

def speed_test_loop() -> None:

    path_to_exe: str = os.getcwd() + '/speedtest.exe'
    server_id: int = 57814

    ## run wine .exe -s {server_id} -f csv and append
    speedtest_cm: str = f'wine {path_to_exe} -s {server_id} -f csv'

    datetime_csv: datetime = datetime.now() #get timestamp right before func call
    timestamp: float = datetime.timestamp(datetime_csv)

    proc_server_list = subprocess.Popen(speedtest_cm,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = proc_server_list.communicate()

    if(errors):
        add_error(errors)

    else:
        #decode output from bytes to string and replace the windows line termination
        output = output.decode('utf-8')
        output = output.replace('\r\n','\n')
        output = output[:-1] #remove last \n
        output = f'{output},"{timestamp}","{datetime_csv}"\n'
        print(repr(output))

        #append output to csv_file
        add_csv_line(output)

    COUNT =+ 1
    return

def start_programs(max_repetitions_speedtest:int) -> None:
   

    #open youtube video in firefox (surpress errors by redirecting to DEVNULL)
    video_url: str = 'https://www.youtube.com/watch?v=gYFQcOFUnqU'
    subprocess.Popen('firefox ' + video_url, shell=True, stderr= subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    #schedule speedtest to run every 10 minutes
    schedule.every(10).minutes.do(speed_test_loop)
    #schedule.every(1).minutes.do(speed_test_loop) [FOR TESTING]

    while EXIT == False and COUNT < max_repetitions_speedtest:
        schedule.run_pending()

    EXIT_MAIN = True
    return

def main():
    #schedule job to run at 1 AM
    schedule.every().day.at('01:00:00').do(start_programs(25))
    #schedule.every().hour.do(start_programs(3)) [FOR TESTING]
    
    timeout:int = 4*60*60 #set a timeout for 4 hours
    timeout_start:time = time.time()

    while EXIT_MAIN == False and time.time() < timeout_start + timeout:
        schedule.run_pending()
    return

if __name__ == "__main__":
    main()