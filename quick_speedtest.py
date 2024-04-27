from datetime import datetime, timedelta
import os
import subprocess
import schedule

EXIT_MAIN: bool = False
EXIT: bool = False
COUNT_BRAGA: int = 0
COUNT_AVEIRO: int = 0

def add_error(error_str: str)-> None:

    error_file_path: str = os.getcwd() + '/speedtest-data/error.txt'

    with open(error_file_path, 'a') as error_file:
            error_file.write(error_str.decode('utf-8'))
            error_file.close()
            EXIT = True
            EXIT_MAIN = True
            return
    
def add_csv_line(output:str, data_file_path:str) -> None:
    with open(data_file_path,'a') as csv_file:
        csv_file.write(output)
        csv_file.close()
        return

def speed_test_loop(server_id:int, data_file_path:str, tag:str) -> None:

    path_to_exe: str = os.getcwd() + '/speedtest.exe'

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

        #append output to csv_file
        add_csv_line(output, data_file_path=data_file_path)

    if(tag == 'Braga'):
        COUNT_BRAGA =+ 1
    else:
        COUNT_AVEIRO =+ 1
    return

def start_programs(max_repetitions_speedtest:int) -> None:
   

    #open youtube video in firefox (surpress errors by redirecting to DEVNULL)
    video_url: str = 'https://www.youtube.com/watch?v=gYFQcOFUnqU'
    firefox = subprocess.Popen('firefox ' + video_url, shell=True, stderr= subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    #schedule speedtest to run every 2 minutes
    data_file_path_braga: str = os.getcwd() + '/speedtest-data/speedtest_data_braga.csv'
    data_file_path_aveiro: str = os.getcwd() + '/speedtest-data/speedtest_data_aveiro.csv'

    schedule.every(2).minutes.do(speed_test_loop,server_id=57814, data_file_path=data_file_path_braga,tag='Braga').tag('Braga') #Braga
    schedule.every(2).minutes.do(speed_test_loop,server_id= 54303, data_file_path=data_file_path_aveiro,tag='Aveiro').tag('Aveiro') #Aveiro

    #schedule.every(1).minutes.do(speed_test_loop) [FOR TESTING]

    while EXIT == False:
        if(COUNT_BRAGA > max_repetitions_speedtest):
            schedule.cancel_job('Braga')
        if(COUNT_AVEIRO > max_repetitions_speedtest):
            schedule.cancel_job('Aveiro')
        schedule.run_pending()

    EXIT_MAIN = True
    firefox.kill()
    return

def main():
    #schedule job to run at 1 AM for 30 minutes
    schedule.every().day.at('13:30').until(timedelta(minutes=30)).do(start_programs(15)).tag('main-job')
    #schedule.every().hour.do(start_programs(3)) [FOR TESTING]

    while EXIT_MAIN == False:
        schedule.run_pending()
    return

if __name__ == "__main__":
    main()