# pyinstaller -F 파일명.py --collect-all easyocr
from RPA import RPA
from myOCR import myocr
from PdfToImage import PdfToImage
import pandas as pd
import os

CONNECTION_PATH = "D:/Uipath/PythonData/PythonConnection.xlsx" # 해당 경로 고정

def write_result_toExcel(result, RPAobject):
    column_name = ['page', 'result']
    df = pd.DataFrame(result, columns=column_name)
    df.to_excel(os.path.join(RPAobject._output_path, "result.xlsx"))

def main_process(RPAobject):
    input_files = RPAobject.get_input_files()
    if len(input_files) == 0: # input파일이 없는 경우 바로 종료
        raise Exception("input파일이 없습니다.")
    convert_images = PdfToImage(input_files[0]) # 첫번째 파일 가져오기(full 경로)) 
    
    result = []
    for number, image in enumerate(convert_images):
        myocr_ = myocr(image, 0.3) # image, threshold
        myocr_.ocr_process() # ocr 작업 시작
        result.append([number+1, myocr_.ocrResult]) # page number, ocr 결과
    write_result_toExcel(result, RPAobject)
    
if __name__ == '__main__':
    try:
        myRPA = RPA(CONNECTION_PATH)
    except:
        raise Exception(CONNECTION_PATH+" 파일을 확인해주세요.")
    
    print("Python RPA 수행 시작")
    main_process(myRPA)
    print("Python RPA 수행 완료")