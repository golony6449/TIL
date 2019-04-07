# Kubernetes Dashboard Login

## 설치

* ```
  kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended/kubernetes-dashboard.yaml
  ```

## 실행

* `kubectl proxy`



## Token 찾기

1. `  kubectl get serviceaccount default -o yaml`
2. `secrets` 항목의 `name` 값 확인
3.   `kubectl describe secret (name값)`



## 참고자료

* <https://blog.cjred.net/entry/kubernetes-Dashboard-%EC%84%A4%EC%B9%98%EC%99%80-%EB%A1%9C%EA%B7%B8%EC%9D%B8>