# pip install opencv-contrib-python==4.5.4.60 
# pip install easyocr

import easyocr
import cv2
import numpy as np

class myocr:
    def __init__(self, file_path, THRESHOLD):
        self._file_path = file_path
        self._img = None
        self._THRESHOLD = THRESHOLD # 최소 정확도 기준
        self._center = []
        self._ocrReader = easyocr.Reader(['ko', 'en']) # easyocr 작업시 선택 할 언어
        self.__ocrResult = '' # 추출된 단어를 담을 문자열 (은닉)
    
    @property
    def ocrResult(self): return self.__ocrResult
    
    @ocrResult.setter
    def ocrResult(self, value): self.__ocrResult += value
    
    # 이미지 읽기
    def read_image(self):
        self._img = cv2.imread(self._file_path) # cv2로 이미지파일 read
        x, y, _ = self._img.shape # image 크기
        self._center.append(int(x/2)) # 중심점 x 
        self._center.append(int(y/2)) # 중심점 y
        cv2.circle(self._img, (self._center[1], self._center[0]), 5, (255,255,0), cv2.FILLED, cv2.LINE_AA) # 중심점 그리기

    # 결과를 보여주는 함수
    def show_image(self):
        cv2.imshow('result_image', cv2.resize(self._img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA))
        cv2.waitKey(4000)
        cv2.destroyAllWindows()
    
    # 이미지 전처리 함수
    def image_preprocessing(self):
        self._img = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY) # RGB -> Gray
        return self._img

    # 기본 Thresholding
    def base_thresholding(self):
        ret, thresh1 = cv2.threshold(self._img, 127, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(self._img, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh3 = cv2.threshold(self._img, 127, 255, cv2.THRESH_TRUNC) # out
        ret, thresh4 = cv2.threshold(self._img, 127, 255, cv2.THRESH_TOZERO)
        ret, thresh5 = cv2.threshold(self._img, 127, 255, cv2.THRESH_TOZERO_INV) # out 
        titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
        images = [self.image_preprocessing(), thresh1, thresh2, thresh3, thresh4, thresh5]

        return titles, images

    # ocr 작업 프로세스 함수
    def ocr_process(self):
        print("RPA S맨 : 이미지에서 텍스트 추출 작업 진행중입니다.")
        if ('.jpg' not in self._file_path.lower()) and ('.png' not in self._file_path.lower()): return ["Need to image file"] # 이미지 파일이 아닌 경우 바로 종료
        
        self.read_image() # 이미지 읽어오기
        self.image_preprocessing() # 이미지 전처리
        result = self._ocrReader.readtext(self._img) # OCR Text 읽기

        for bbox, text, conf in result: # bbox(해당 text의 위치), text(추출된 문자), conf(정확도)
            if conf >= self._THRESHOLD: # conf(정확도)가 THRESHOLD 이상일 때만 리스트에 s담는다.
                self.ocrResult = text # Setter로 결과값 넣어주기
                cv2.rectangle(self._img, pt1=(int(bbox[0][0]), int(bbox[0][1])), pt2=(int(bbox[2][0]), int(bbox[2][1])), color=(0, 255, 0), thickness=3) # image에 사각형 표시

        print("RPA S맨 : 이미지에서 텍스트 추출 작업 완료.")
        self.show_image() # 결과 보기


if __name__ == '__main__':
    myocr_ = myocr('./data/bills_sample1.jpg', 0.3)
    myocr_.ocr_process() # ocr 작업 시작
    print(myocr_.ocrResult)