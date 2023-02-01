from pdf2image import convert_from_path

# Is poppler installed and in PATH 에러 발생시 -> poppler설치하여 해결 (https://github.com/oschwartz10612/poppler-windows/releases/)
# 압축해제 후 poppler_path 경로로 옮기기

def PdfToImage(filepath): # PDF -> IMG 파일로 변환
    print("RPA S맨 : PDF파일 -> Image파일 변환중입니다.")
    print(filepath)
    if ".pdf" not in filepath: # filepath가 pdf파일이 아닌경우는 바로 종료
        return
    img_paths = [] # img로 변환 된 경로를 담을 LIST
    pages = convert_from_path(filepath, poppler_path='C:/Program Files/poppler/Library/bin') # pdf파일에서 page별로 객체를 나눠줌

    for idx, page in enumerate(pages): 
        page.save(filepath.replace(".pdf", "")+str(idx+1)+".jpg", "JPEG") # 파일명 : pdf 파일명+idx로 생성
        img_paths.append(filepath.replace(".pdf", "")+str(idx+1)+".jpg") # list에 담아줌

    print("RPA S맨 : PDF파일 -> Image파일 변환완료.")
    return img_paths # 변환된 image 경로 LIST를 반환

if __name__ == '__main__':
    print(PdfToImage('./data/bills_sample.pdf'))