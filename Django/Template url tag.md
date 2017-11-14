# Template url tag
--------------------

### Template tag?
* Template 안에서 사용되는 django tag
* {% 태그명 [값] %} 형태로 사용
* ex: url, block, load 등

## url
### 역할
* url의 하드코딩을 방지 -> url 구조 변경시 수정요소를 줄여주는 역할
* urlconf.py의 url중 해당하는 url을 불러와 렌더링 후 Client에게 Response

### 사용법
* {% url "name" [값] %}
* name은 urlconf.py에서 각각의 url의 name값을 의미

### 값 전달 방법
* urlconf.py의 url의 regex의 key 이름 = value 형태로 작성
* ex: r'^search/(?P<keyword>[a-zA-Z]+)/$' => {% url 'search' keyword=temp %}

### 참고자료
* https://stackoverflow.com/questions/25345392/how-to-add-url-parameters-to-django-template-url-tag