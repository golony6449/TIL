# Django with axios

## 개요
* axios는 Vue.js에서 사용되는 ajax 형의 서비스에 사용되는 모듈
* 비동기식 통신을 위한 모듈로 보임

## 발생한 문제
* 프론트엔드에서 해당 모듈을 사용해 Document Example에 적힌대로 POST 요청
* 백엔드에서 이전에 했던 형태로 값 접근 시도
* 해당 key가 없다는 에러 발생 (`request.POST`는 Dict 자료형)
* `console.log`, `request.POST.keys()`를 이용해 확인해 보아도 JS에서는 값이 출력 되고, POST에는 아무런 자료도 들어있지 않음
* Fiddler를 이용해 송수신 패킷을 확인 ==> 패킷상에서는 값이 확인 됨

### 코드
```javascript
axios({
          method: 'post',
          url: 'http://find_relation',
          data:
            {
              journalism: this.journalismName,
              iframeInfo: this.pageData
            }
        })
        .then(function(response) {console.log(response);})
        .catch(function(error) {console.log(error);}
        );
```
```python
request.POST['jouralism']
```

## Solution
* axios는 JSON으로 Serialize 한다고 함 (Github issue)
* JSON으로 Serialize한 경우는 request의 body 필드에 담겨있음 (From Stackoverflow)
* 이 Body를 json으로 Deserialize해 사용하면 됨

* 일반적인 요청과 axios상에서의 요청을 패킷단에서 비교해보니 일반적인 요청은 `&`를 이용한 GET method에서 볼수 있는 형식을 보이고, axios의 요청은 json 포멧으로 되어있음을 확인

## Reference
* axios의 serialize: https://github.com/axios/axios/issues/304#issuecomment-215129729
* JSON처리: https://stackoverflow.com/questions/24068576/how-to-receive-json-data-using-http-post-request-in-django-1-6
