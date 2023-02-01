import os
import pandas as pd

class RPA:
    def __init__(self, rpa_connection):
        self._rpa_connection = rpa_connection
        self._main_path = pd.read_excel(self._rpa_connection)['정보'][0] # Uipath에서 해당 파일을 Update 함 (본인 안건 번호로 ex SW_MD_P1S4)
        self._input_path = os.path.join(self._main_path, "input")
        self._output_path = os.path.join(self._main_path, "output")
        self._master_path = os.path.join(self._main_path, "Master")
        self._temp_path = os.path.join(self._main_path, "Temp")
        self._python_output_path = os.path.join(self._main_path, "PythonOutput") # Python 자동화 수행 후 결과파일을 남겨놓을 경로
    
    def get_input_files(self): # full 경로 반환
        return [os.path.join(self._input_path, file) for file in os.listdir(self._input_path)]

    def get_output_files(self): # full 경로 반환
        return [os.path.join(self._output_path, file) for file in os.listdir(self._output_path)]

    def get_master_files(self): # full 경로 반환
        return [os.path.join(self._master_path, file) for file in os.listdir(self._master_path)]
    
    def get_temp_files(self): # full 경로 반환
        return [os.path.join(self._temp_path, file) for file in os.listdir(self._temp_path)]