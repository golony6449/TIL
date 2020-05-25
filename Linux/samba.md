# Samba on Linux

## Symbolic Link 접속시 Access Denied

* 기본적으로 심볼릭 링크를 타고 들어갈수 없도록 설정됨
* `smb.conf`에 관련 설정 추가 후 서비스 재시작

```
[global]
follow symlinks = yes
wide links = yes
unix extensions = no
```

* https://m.blog.naver.com/PostView.nhn?blogId=zeta0807&logNo=221414394900&proxyReferer=https:%2F%2Fwww.google.com%2F
* https://ubuntuforums.org/showthread.php?t=1728541