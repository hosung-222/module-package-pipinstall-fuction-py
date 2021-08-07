#구글에서 pypi검색 pypi.org사이트 
#beautifulsoup4 다운후 터미널에 넣기

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#pip list 터미널에 입력시 깔려있는  pip정보 알려줌
#pip show beautifulsoup4  - 상세 정보
#pip install --upgrade beautifulsoup4 - 업데이트
#pip uninstall beautifulsoup4 - 삭제