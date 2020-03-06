# Model in Django

## 외래키 지정시 'related_name'

* 예: `user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=comment)`
* 참조 대상이 되는 모델에 `related_name`으로 지정한 명칭이 생긴다는 느낌인 것으로 보임
* [참고자료](https://fabl1106.github.io/django/2019/05/27/Django-26.-장고-related_name-설정방법.html)

